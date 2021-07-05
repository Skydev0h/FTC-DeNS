pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4User is ID4User, D4Based {

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Variables

    mapping(uint32 => uint128) public fundLocks;
    uint32 public minLockTime;
    uint128 public totalLocked;

    bytes public masterKey;

    mapping(uint32  => address ) public auctBook;
    mapping(address => AuctInfo) public auctInfo;
    mapping(address => AuctBid ) public auctBids;

    mapping(uint32  => address ) public certBook;
    mapping(address => CertInfo) public certInfo;

    uint32 public auctBookNext;
    uint32 public certBookNext;

    uint128 call_value;
    uint8 call_flag;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Modifiers

    modifier onlyOwner {
        if (st_parent.wid == Sys.ExternalMetaChain)
            require(msg.pubkey() == st_parent.value, Errors.onlyOwnerAccepted);
        else
            require(msg.sender == st_parent, Errors.onlyOwnerAccepted);
        tvm.accept();
        _;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Constructor

    constructor() public { revert(Errors.directDeployForbidden); }

    function onCodeUpgrade(TvmCell, TvmCell capsule)
        internal
    {
        require(m_version == Sys.IsContructorCall, Errors.invalidArgument); // v0->1
        tvm.resetStorage();
        TvmSlice s = capsule.toSlice();
        unpackBase(s);
        m_version = 1;
        if (st_parent.wid == Sys.ExternalMetaChain) {
            call_value = Sys.CallValue;
            call_flag = 0;
        } else {
            call_value = 0;
            call_flag = Flags.messageValue;
        }
    }

    function setMasterKey(bytes newMasterKey)
        external override
        onlyOwner
    {
        masterKey = newMasterKey;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Code upgrade

    function requestUpgrade()
        external view override
        onlyOwner returnRemainder
    {
        uint hash = tvm.hash(tvm.code());
        ID4Root(st_root).upgradeMeRequest
            {value: call_value, bounce: true, flag: call_flag}
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
        b.store(fundLocks, minLockTime, totalLocked, masterKey,
            auctBook, auctInfo, auctBids, certBook, certInfo,
            certBookNext, auctBookNext);
        onCodeUpgrade(empty, b.toCell());
    }

    function upgradeNotNeeded()
        external override
        onlyRoot
    {
        emit alreadyUpToDate();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Create auction

    function createAuction(string name, uint8 duration)
        external view override
        onlyOwner
    {
        ID4Root(st_root).createAuction{
            callback:  D4User.createAuctionCallback,
               value:  call_value,
                flag:  call_flag
        } (st_parent, m_revision, name, duration);
    }

    function createAuctionCallback(address auction)
        external view
        onlyRoot
    {
        st_root;
        ID4Auct(auction).getInfo{
            callback:  D4User.queryAuctCallback,
               value:  0,
                flag:  Flags.messageValue
        }();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Perform bid

    function makeBid(address auction, bytes data, uint256 hash)
        external override
        onlyOwner
    {
        if (st_parent.wid != Sys.ExternalMetaChain)
            require(msg.value >= Sys.MinimumMakeBid, Errors.messageValueTooLow);
        AuctInfo info = auctInfo[auction];
        uint32 tnow = Now();
        require(tnow >= info.startTime, Errors.invalidTimePhase);
        require(tnow < info.bidEnds, Errors.invalidTimePhase);
        optional(AuctBid) bid = auctBids.fetch(auction);
        if (!bid.hasValue()) { // a new bid (not updating old one)
            ID4Auct(auction).accountBid{value: Sys.CallValue}(st_parent); // TODO: ts4 not calling?
        }
        auctBids[auction] = AuctBid(tnow, data, hash);
    }

    event debug(AuctBid arg);

    function revealBid(address auction, uint128 amount, uint128 nonce)
        external override
        onlyOwner
    {
        if (st_parent.wid != Sys.ExternalMetaChain)
            require(msg.value >= amount + Sys.AddToReveal, Errors.messageValueTooLow);
        AuctInfo info = auctInfo[auction];
        require(Now() >= info.bidEnds, Errors.invalidTimePhase);
        require(Now() < info.revEnds, Errors.invalidTimePhase);
        AuctBid bid = auctBids[auction];
        if (st_parent.wid != Sys.ExternalMetaChain)
            ID4Auct(auction).revealBid {value: 0, bounce: true, flag: Flags.messageValue + Flags.addFees}
                (st_parent, bid.time, amount, nonce, bid.hash);
        else
            ID4Auct(auction).revealBid {value: amount + Sys.AddToReveal, bounce: true, flag: Flags.addFees}
                (st_parent, bid.time, amount, nonce, bid.hash);
    }

    function bidRevealComplete()
        external override
    {
        AuctInfo info = auctInfo[msg.sender];
        verifyInteraction(Base.auct, info.name, info.parent);
        delete auctBids[msg.sender];
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    function finalize(address auction)
        external override
        onlyOwner
    {
        ID4Auct(auction).finalize{value: call_value, bounce: true, flag: call_flag}(st_parent);
    }

    function utilBidHash(address auction, uint32 startTime, address user, uint128 amount, uint256 nonce)
        external pure
        returns (uint256)
    {
        TvmBuilder b;
        b.store(auction, startTime, user, amount, nonce);
        return tvm.hash(b.toCell());
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Working with books

    function queryCert(address target)
        external view override
        onlyOwner
    {
        ID4Cert(target).getInfo{
            callback:  D4User.queryCertCallback,
               value:  call_value,
                flag:  call_flag
        }();
    }

    function queryAuct(address target)
        external view override
        onlyOwner
    {
        ID4Auct(target).getInfo{
            callback:  D4User.queryAuctCallback,
               value:  call_value,
                flag:  call_flag
        }();
    }

    function forgetCert(address target)
        external override
        onlyOwner
    {
        CertInfo info = certInfo[target];
        delete certBook[info.id];
        delete certInfo[target];
    }

    function forgetAuct(address target)
        external override
        onlyOwner
    {
        AuctInfo info = auctInfo[target];
        optional(AuctBid) bid = auctBids.fetch(target);
        if (bid.hasValue())
            require(Now() >= info.revEnds, Errors.cantForgetActiveBid);
        delete auctBook[info.id];
        delete auctInfo[target];
        if (bid.hasValue())
            delete auctBids[target];
    }

    function queryCertCallback(CertInfo info)
        external
    {
        verifyInteraction(Base.cert, info.name, info.parent);
        tvm.accept();
        info.sync = Now();
        optional(CertInfo) old = certInfo.fetch(msg.sender);
        if (old.hasValue())
            info.id = old.get().id;
        else {
            info.id = (certBookNext++);
            certBook[info.id] = msg.sender;
        }
        certInfo[msg.sender] = info;
    }

    function queryAuctCallback(AuctInfo info)
        external override
    {
        verifyInteraction(Base.auct, info.name, info.parent);
        tvm.accept();
        info.sync = Now();
        optional(AuctInfo) old = auctInfo.fetch(msg.sender);
        if (old.hasValue())
            info.id = old.get().id;
        else {
            info.id = (auctBookNext++);
            auctBook[info.id] = msg.sender;
        }
        auctInfo[msg.sender] = info;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Proxy (cert)

    function setValue(address target, int16 index, address new_value)
        external view override
        onlyOwner
    {
        ID4Cert(target).setValue {value: call_value, bounce: true, flag: call_flag}
                        (index, new_value);
    }

    function resetValue(address target, int16 index)
        external view override
        onlyOwner
    {
        ID4Cert(target).resetValue {value: call_value, bounce: true, flag: call_flag}
                        (index);
    }

    function clearValues(address target)
        external view override
        onlyOwner
    {
        ID4Cert(target).clearValues {value: call_value, bounce: true, flag: call_flag}
                        ();
    }

    function certWithdrawExcess(address target, uint128 amount)
        external view override
        onlyOwner
    {
        ID4Cert(target).withdrawExcess {value: call_value, bounce: true, flag: call_flag}
                        (call_value == 0 ? msg.sender : address(this), amount);
    }

    function certRequestUpgrade(address target)
        external view override
        onlyOwner
    {
        ID4Cert(target).requestUpgrade {value: call_value, bounce: true, flag: call_flag}
                        ();
    }

    function requestProlong(address target)
        external view override
        onlyOwner
    {
        ID4Cert(target).requestProlong {value: call_value, bounce: true, flag: call_flag}
                        ();
    }

    function deploySub(address target, string name)
        external view override
        onlyOwner
    {
        ID4Cert(target).deploySub {value: call_value, bounce: true, flag: call_flag}
                        (name);
    }

    function syncSub(address target, string name)
        external view override
        onlyOwner
    {
        ID4Cert(target).syncSub {value: call_value, bounce: true, flag: call_flag}
                        (name);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Funds lock

    function addLocked(uint32 until, string name, address parent)
        external override
    {
        if (msg.sender != st_root)
            verifyInteraction(Base.auct, name, parent); // Hard
        //    if (msg.sender != _resolveContract(Base.auct, name, parent))
        //        return; // Soft
        if (until <= Now()) return;
        optional(uint128) currently = fundLocks.fetch(until);
        if (currently.hasValue()) {
            fundLocks[until] = currently.get() + msg.value;
        } else {
            fundLocks[until] = msg.value;
        }
        totalLocked += msg.value;
        if (until < minLockTime)
            minLockTime = until;
    }

    function withdrawable()
        public view override
        returns (uint128 avail)
    {
        uint128 bal = address(this).balance;
        uint128 tvl = totalLocked;
        uint32 tnow = Now();
        if (tnow >= minLockTime) {
            optional(uint32, uint128) min = fundLocks.min();
            while (min.hasValue()) {
                (uint32 ts, uint128 val) = min.get();
                if (tnow >= ts) {
                    tvl -= val;
                    min = fundLocks.next(ts);
                }
                else
                    min.reset();
            }
        }
        return bal - Sys.MinimalUserBalance - tvl;
    }

    function sweepLocks()
        external override
    {
        uint32 tnow = Now();
        if (tnow >= minLockTime) {
            optional(uint32, uint128) min = fundLocks.min();
            while (min.hasValue()) {
                (uint32 ts, uint128 val) = min.get();
                if (tnow >= ts) {
                    delete fundLocks[ts];
                    totalLocked -= val;
                    min = fundLocks.min();
                    if (!min.hasValue())
                        minLockTime = Sys.MaxU32;
                }
                else {
                    minLockTime = ts;
                    min.reset();
                }
            }
            if (totalLocked == 0)
                minLockTime = Sys.MaxU32;
        }
    }

    function withdraw(address dest, uint128 value)
        external view override onlyOwner
    {
        require(value <= withdrawable(), Errors.remainingBalanceTooLow);
        emit withdrawn(address(this).balance, value);
        dest.transfer(value, true);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Football

    onBounce(TvmSlice slice)
        external
    {
        uint32 functionId = slice.decode(uint32);
        if (functionId == tvm.functionId(ID4Auct.revealBid)) {
            passToOwner();
        }
    }

    function passToOwner()
        public override
    {
        if (st_parent.wid != Sys.ExternalMetaChain)
            st_parent.transfer({value: 0, bounce: false, flag: Flags.messageValue});
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Events

    event withdrawn(uint128 oldBalance, uint128 withdrawn);

    event upgradeRequested(uint32 my_rev, uint256 my_hash);
    event upgradeReceived(uint32 new_rev, uint256 new_hash);
    event alreadyUpToDate();

}