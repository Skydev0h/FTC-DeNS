pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4Cert is ID4Cert, D4Based {

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Variables

    address public owner;
    address public pending_owner; // upgrade-volatile
    uint32 public owner_transfer_deadline; // upgrade-volatile
    uint32 public relinquish_owner_deadline; // upgrade-volatile

    mapping(int16 => address) public value;

    uint32 public registered;
    uint32 public auctioned;
    uint32 public expires;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Constructor

    constructor() public { revert(Errors.directDeployForbidden); }

    function onCodeUpgrade(TvmCell param, TvmCell capsule)
        internal
    {
        require(m_version == Sys.IsContructorCall, Errors.invalidArgument); // v0->1
        tvm.resetStorage();
        TvmSlice s = capsule.toSlice();
        unpackBase(s);
        (owner, expires) = param.toSlice().decode(address, uint32);
        emit initialized(owner, expires);
        if (registered == 0) registered = Now();
        if ((auctioned == 0) && (st_root == st_parent))
             auctioned = Now();
        m_version = 1;
        ID4User(owner).queryCertCallback{value:Sys.CallValue}(getInfo());
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Modifiers

    modifier onlyOwner()
    {
        // FIX: Full access of Certificate as owner after relinquishing
        require(msg.sender == owner && msg.isInternal, Errors.onlyOwnerAccepted);
        tvm.accept();
        _;
    }

    modifier onlyPendingOwner()
    {
        require(Now() <= owner_transfer_deadline, Errors.ownerTransferMissDeadline);
        require(msg.sender == pending_owner && msg.isInternal, Errors.onlyPendingOwnerAccepted);
        tvm.accept();
        _;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Receive and fallback

    receive()
        external pure
    {

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Code upgrade

    function requestUpgrade()
        external view override
        onlyOwner returnRemainder
    {
        uint hash = tvm.hash(tvm.code());
        ID4Root(st_root).upgradeMeRequest
            {value: 0, bounce: true, flag: Flags.messageValue}
            (st_type, m_revision, hash);
        emit upgradeRequested(m_revision, hash);
    }

    function upgrade(TvmCell code, uint32 revision)
        external override
        onlyRoot
    {
        emit upgradeReceived(revision, tvm.hash(code));
        tvm.accept();
        m_revision = revision;
        tvm.setCurrentCode(code);
        tvm.setcode(code);
        TvmCell empty;
        TvmBuilder b = packBase();
        b.store(owner, value, registered, auctioned, expires);
        onCodeUpgrade(empty, b.toCell());
    }

    function upgradeNotNeeded()
        external override
        onlyRoot
    {
        emit alreadyUpToDate();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Query quasistatic information

    function getInfo()
        public responsible view override
        returns (CertInfo info)
    {
        return {value: 0, bounce: false, flag: Flags.messageValue}
        CertInfo(
            0, 0,
            st_name, st_parent,
            registered, auctioned, expires,
            owner
        );
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Values (targets)

    function getValue(int16 index)
        external view responsible override
        returns(address)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            value.at(index);
    }

    function setValue(int16 index, address new_value)
        external override
        onlyOwner returnRemainder
    {
        value[index] = new_value;
        emit valueSet(index, new_value);
    }

    function resetValue(int16 index)
        external override
        onlyOwner returnRemainder
    {
        delete value[index];
        emit valueReset(index);
    }

    function clearValues()
        external override
        onlyOwner returnRemainder
    {
        delete value;
        emit valueCleared();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // System interaction

    function registrationPreflight(uint128 requestId)
        external view responsible override
        returns (uint128 requestId_, uint32 expiry_)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            (requestId, expires);
    }

    function applyAuctionResult(address new_owner, uint32 new_expiry)
        external responsible override
        returns (bool success)
    {
        if (msg.sender != st_root) // Root or Auction
            verifyInteraction(Base.auct, st_name, st_parent);
        tvm.accept(); // Shall not fail because of gas
        emit auctionResultApplied(owner, new_owner, expires, new_expiry);
        address old_owner = owner;
        if ((owner != new_owner) && (new_owner != address(0))) {
            // Tidy up the state
            delete value;
            owner = new_owner;
            pending_owner = address(0);
            owner_transfer_deadline = 0;
            relinquish_owner_deadline = 0;
        }
        auctioned = Now();
        if (new_expiry != 0)
            expires = new_expiry;
        if (st_parent == st_root) {
            ID4User(owner).queryCertCallback{value:Sys.CallValue}(getInfo());
            if (owner != old_owner)
                ID4User(old_owner).queryCertCallback{value:Sys.CallValue}(getInfo());
        }
        return {value: 0, bounce: true, flag: Flags.messageValue}
            true;
    }

    function ensureExpiry(uint32 expiry, bool retval)
        external override
    {
        if (msg.sender != st_root) // Root or Auction
            verifyInteraction(Base.auct, st_name, st_parent);
        expires = math.max(expires, expiry);
        if (st_parent == st_root)
            ID4User(owner).queryCertCallback{value:Sys.CallValue}(getInfo());
        if (retval)
            msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Ownership

    function getOwner()
        external view responsible override
        returns (address owner_)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            owner;
    }

    function getPendingOwner()
        external view responsible override
        returns (address pending_owner_)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            pending_owner;
    }

    function transferOwner(address new_owner, uint32 deadline)
        external override onlyOwner
    {
        if (owner == st_root) {
            owner = new_owner;
            expires = deadline;
            emit reservedOwnerSet(new_owner, deadline);
            ID4User(owner).queryCertCallback{value:Sys.CallValue}(getInfo()); // register in new user (if exists)
            return;
        }
        require(Now() < deadline, Errors.ownerTransferMissDeadline);
        pending_owner = new_owner;
        owner_transfer_deadline = deadline;
        emit ownerTransferStart(owner, new_owner, deadline);
    }

    function cancelTransferOwner()
        external override onlyOwner
    {
        owner_transfer_deadline = 0;
        pending_owner = address(0);
        emit ownerTransferCancelled(owner);
    }

    function acceptTransfer()
        external override onlyPendingOwner
    {
        emit ownerTransferComplete(owner, pending_owner);
        address old_owner = owner;
        owner = pending_owner;
        owner_transfer_deadline = 0;
        pending_owner = address(0);
        if (st_parent == st_root) {
            ID4User(owner).queryCertCallback{value:Sys.CallValue}(getInfo());
            if (owner != old_owner)
                ID4User(old_owner).queryCertCallback{value:Sys.CallValue}(getInfo());
        }
    }

    function relinquishOwner()
        external override onlyOwner
    {
        if (Now() > relinquish_owner_deadline)
        {
            relinquish_owner_deadline = Now() + Sys.RelinquishOwnerTimeout;
            emit ownerRelinquishStart(owner, relinquish_owner_deadline);
            return;
        }
        emit ownerRelinquishComplete(owner);
        address old_owner = owner;
        owner = address(0);
        pending_owner = address(0);
        owner_transfer_deadline = 0;
        relinquish_owner_deadline = 0;
        if (st_parent == st_root)
            ID4User(old_owner).queryCertCallback{value:Sys.CallValue}(getInfo());
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Prolong / subcert

    function requestProlong()
        external view override
        onlyOwner
    {
        ID4Auct(_resolveContract(Base.auct, st_name, st_parent)).prolong
            {value: 0, bounce: true, flag: Flags.messageValue}();
    }

    function deploySub(string name)
        external override
        onlyOwner
    {
        // It may bounce if name is not allowed
        ID4Root(st_root).subCertDepl
            {value: 0, bounce: true, flag: Flags.messageValue}
            (st_name, st_parent, name, owner, expires);
    }

    function syncSub(string name)
        external override
        onlyOwner
    {
        address addr = _resolveContract(Base.cert, name, address(this));
        ID4Cert(addr).subSynchronize
            {value: 0, bounce: true, flag: Flags.messageValue}
            (owner, expires);
    }

    function subSynchronize(address new_owner, uint32 new_expiry)
        external override
        onlyParent
    {
        if (owner != new_owner) {
            // FIX: Improve sub synchronize for Certificates
            owner = new_owner;
            pending_owner = address(0);
            owner_transfer_deadline = 0;
            relinquish_owner_deadline = 0;
        }
        expires = new_expiry;
        emit synchronized(new_owner, new_expiry);
        // ID4Cert(msg.sender).passToOwner{value: 0, bounce: false, flag: Flags.messageValue}();
        passToOwner(); // can now return directly
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Football

    onBounce(TvmSlice slice)
        external
    {
        uint32 functionId = slice.decode(uint32);
        if (functionId == tvm.functionId(ID4Auct.prolong))        { passToOwner(); }
        if (functionId == tvm.functionId(ID4Root.subCertDepl))    { passToOwner(); }
        if (functionId == tvm.functionId(ID4Cert.subSynchronize)) { passToOwner(); }
    }

    function passToOwner()
        public override
    {
        // owner.transfer({value: 0, bounce: false, flag: Flags.messageValue});
        IPasser(owner).passToOwner{value: 0, bounce: false, flag: Flags.messageValue}();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Withdraw excess funds

    function withdrawExcess(address dest, uint128 amount)
        external pure override onlyOwner
    {
        require(
            address(this).balance - amount >= Sys.MinimalCertBalance,
            Errors.remainingBalanceTooLow);
        emit excessBalanceWithdrawn(address(this).balance, amount);
        dest.transfer(amount, true);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Events

    event ownerTransferStart(address currentOwner, address nextOwner, uint32 deadline);
    event ownerTransferCancelled(address currentOwner);
    event ownerTransferComplete(address fromOwner, address toOwner);

    event ownerRelinquishStart(address curOwner, uint32 deadline);
    event ownerRelinquishComplete(address oldOwner);

    event excessBalanceWithdrawn(uint128 oldBalance, uint128 withdrawn);

    event valueSet(int16 index, address value);
    event valueReset(int16 index);
    event valueCleared();

    event upgradeRequested(uint32 my_rev, uint256 my_hash);
    event upgradeReceived(uint32 new_rev, uint256 new_hash);
    event alreadyUpToDate();

    event auctionResultApplied(address curOwner, address newOwner, uint32 curExpiry, uint32 newExpiry);
    event prolongRequested(uint128 value);

    event initialized(address initOwner, uint32 initExpiry);
    event synchronized(address syncOwner, uint32 syncExpiry);

    event reservedOwnerSet(address new_owner, uint32 new_expiry);

}
