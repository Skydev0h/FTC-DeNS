pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";
import "./D4Base.sol";

contract D4Root is ID4Root {

    uint16 public m_version = 1;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Code

    TvmCell public base_code;        // 0
    TvmCell public certificate_code; // 1
    TvmCell public auction_code;     // 2
    TvmCell public user_code;        // 3

    uint32 public base_revision;
    uint32 public certificate_revision;
    uint32 public auction_revision;
    uint32 public user_revision;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Variables

    address public owner; // -99: external (Sys.ExternalMetaChain)
    address public pending_owner; // upgrade-volatile
    uint32 public owner_transfer_deadline; // upgrade-volatile
    uint32 public relinquish_owner_deadline; // upgrade-volatile

    address public smv_root;
    uint32 public no_auctions_until;

    uint8 public admin_enabled;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Constructor

    constructor()
        public
    {
        require(tvm.pubkey() != 0, Errors.initialOwnerMissing);
        require(msg.pubkey() == tvm.pubkey(), Errors.onlyOwnerAccepted);
        tvm.accept();
        owner = address.makeAddrStd(Sys.ExternalMetaChain, tvm.pubkey());
        no_auctions_until = 0;
        admin_enabled = 0xFF;
        tvm.setPubkey(0);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Modifiers

    modifier onlyOwner()
    {
        if (owner.wid == Sys.ExternalMetaChain)
            require(msg.pubkey() == owner.value, Errors.onlyOwnerAccepted);
        else
            require(msg.sender == owner, Errors.onlyOwnerAccepted);
        tvm.accept();
        _;
    }

    modifier onlyPendingOwner()
    {
        require(Now() <= owner_transfer_deadline, Errors.ownerTransferMissDeadline);
        if (pending_owner.wid == Sys.ExternalMetaChain)
            require(msg.pubkey() == pending_owner.value, Errors.onlyPendingOwnerAccepted);
        else
            require(msg.sender == pending_owner, Errors.onlyPendingOwnerAccepted);
        tvm.accept();
        _;
    }

    modifier onlySmvRoot()
    {
        require(msg.sender == smv_root, Errors.onlySmvRootAccepted);
        tvm.accept();
        _;
    }

    modifier adminEnabled(uint8 flag)
    {
        require((admin_enabled & flag) == flag, Errors.adminFlagDisabled);
        _;
    }

    function verifyInteraction(uint8 ct_type, string name, address parent)
        internal view
    {
        require(msg.sender == _resolveContract(ct_type, name, parent),
            Errors.interactionWrongSender);
        //if (revision != 0) {
        //    (TvmCell ncode, uint32 nrev) = _retrieveCode(ct_type);
        //    require(revision >= nrev, Errors.interactionOutdated);
        //}
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Receive and fallback

    receive()
        external pure
    {

    }

    fallback()
        external pure
    {
        revert(Errors.fallbackForbidden);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // System: onBounce handler

    /*
    onBounce(TvmSlice slice)
        external
    {
        uint32 functionId = slice.decode(uint32);

    }
    */

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Administration

    function dropAdminFlag(uint8 flags)
        external override
        onlyOwner
    {
        admin_enabled = (admin_enabled & (~flags));
        emit adminFlagDropped(flags, admin_enabled);
    }

    function adminDeploy(string name, address set_owner, uint32 set_expiry)
        external view override
        onlyOwner adminEnabled(AFlags.deploy)
    {
        TvmBuilder param;
        param.store(set_owner, set_expiry);
        _deployContract(Base.cert, name, address(this), param.toCell());
        emit adminDeployed(name, set_owner, set_expiry);
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    function adminReserve(string name)
        external view override
        onlyOwner adminEnabled(AFlags.reserve)
    {
        TvmBuilder param;
        param.store(Sys.ReserveNOWDuration);
        param.store(address(0));
        _deployContract(Base.auct, name, address(this), param.toCell());
        emit adminReserved(name);
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    function adminChown(string name, address set_owner)
        external view override
        onlyOwner adminEnabled(AFlags.chown)
    {
        ID4Cert(_resolveContract(Base.cert, name, address(this))).applyAuctionResult{
            callback:  D4Root.applyAuctionCallback,
               value:  Sys.CallValue,
                flag:  Flags.addTransactionFees
        }(set_owner, 0);
        emit adminChowned(name, set_owner);
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    function adminChexp(string name, uint32 set_expiry)
        external view override
        onlyOwner adminEnabled(AFlags.chexp)
    {
        ID4Cert(_resolveContract(Base.cert, name, address(this))).applyAuctionResult{
            callback:  D4Root.applyAuctionCallback,
               value:  Sys.CallValue,
                flag:  Flags.addTransactionFees
        }(address(0), set_expiry);
        emit adminChexped(name, set_expiry);
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
    }

    function adminUpgradeUser(address target)
        external view override
        onlyOwner adminEnabled(AFlags.upuser)
    {
        TvmCell ncode; uint32 nrev;
        (ncode, nrev) = _retrieveCode(Base.user);
        IUpgradable(target).upgrade
            {value: 0, bounce: true, flag: Flags.messageValue}
            (ncode, nrev);
        emit adminUpgradedUser(target);
    }

    function adminUpgradeCert(address target)
        external view override
        onlyOwner adminEnabled(AFlags.upcert)
    {
        TvmCell ncode; uint32 nrev;
        (ncode, nrev) = _retrieveCode(Base.cert);
        IUpgradable(target).upgrade
            {value: 0, bounce: true, flag: Flags.messageValue}
            (ncode, nrev);
        emit adminUpgradedCert(target);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // SMV

    function onProposalPassed(ProposalInfo proposalInfo)
        external override
        onlySmvRoot
    {
        TvmCell c = proposalInfo.specific;
        if (proposalInfo.proposalType == ProposalType.SetCode) {
            SetCodeProposalSpecific c_setCode = c.toSlice().decode(SetCodeProposalSpecific);
            TvmCell code = c_setCode.code;
            uint256 chash = tvm.hash(code);
            uint8 ct = c_setCode.ContractType;
            emit smvCodeUpgrade(ct, chash);
            if (ct == Base.cert) {
                certificate_code = code;
                certificate_revision = Now();
                return;
            }
            if (ct == Base.auct) {
                auction_code = code;
                auction_revision = Now();
                return;
            }
            if (ct == Base.user) {
                user_code = code;
                user_revision = Now();
                return;
            }
            if (ct == Base.root) {
                _upgrade(code);
                return;
            }
            return;
        }
        if (proposalInfo.proposalType == ProposalType.Reserve) {
            ReserveProposalSpecific c_reserve = c.toSlice().decode(ReserveProposalSpecific);
            ID4Auct(_resolveContract(Base.auct, c_reserve.name, address(this))).commit(true);
            emit smvReserveCommit(c_reserve.name, true);
            return;
        }
        if (proposalInfo.proposalType == ProposalType.SetOwner) {
            SetOwnerProposalSpecific c_sown = c.toSlice().decode(SetOwnerProposalSpecific);
            //deployCertificate(c_depcrt.name, c_depcrt.owner, uint32(c_depcrt.ts), address(this));
            setReservedOwner(c_sown.name, c_sown.owner, uint32(c_sown.ts));
            emit smvSetOwner(c_sown.name, c_sown.owner, uint32(c_sown.ts));
            return;
        }
        if (proposalInfo.proposalType == ProposalType.SetRootOwner) {
            SetRootOwnerProposalSpecific c_setown = c.toSlice().decode(SetRootOwnerProposalSpecific);
            owner = address.makeAddrStd(Sys.ExternalMetaChain, c_setown.pubkey);
            pending_owner = address(0);
            owner_transfer_deadline = 0;
            relinquish_owner_deadline = 0;
            emit smvSetRootOwner(owner);
            return;
        }
    }

    function onProposalRejected(ProposalInfo proposalInfo)
        external override
        onlySmvRoot
    {
        TvmCell c = proposalInfo.specific;
        if (proposalInfo.proposalType == ProposalType.Reserve) {
            ReserveProposalSpecific c_reserve = c.toSlice().decode(ReserveProposalSpecific);
            ID4Auct(_resolveContract(Base.auct, c_reserve.name, address(this))).commit(false);
            emit smvReserveCommit(c_reserve.name, false);
        }
    }

    function onProposalDeploy(address, ProposalType proposalType, TvmCell specific)
        external override
        onlySmvRoot
    {
        if (proposalType == ProposalType.Reserve) {
            ReserveProposalSpecific c_reserve = specific.toSlice().decode(ReserveProposalSpecific);
            TvmBuilder param;
            param.store(Sys.ReserveDuration);
            param.store(address(0));
            _deployContract(Base.auct, c_reserve.name, address(this), param.toCell());
            emit smvReserveStart(c_reserve.name);
        }
    }

    function setReservedOwner(string name, address new_owner, uint32 new_expiry)
        internal view
    {
        ID4Cert(_resolveContract(Base.cert, name, address(this))).transferOwner
            {value: 0, bounce: false, flag: Flags.messageValue}
            (new_owner, new_expiry);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Direct user interaction

    function deployUserForMe()
        external responsible override
        returns (address user_addr)
    {
        require(msg.sender != address(0), Errors.internalMessageOnly);
        require(msg.value >= Sys.MinimalUserRegister, Errors.messageValueTooLow);
        TvmCell empty;
        address wal = _deployContract(Base.user, "", msg.sender, empty);
        return {value: 0, bounce: false, flag: Flags.messageValue} wal;
    }

    function deployUserForPubKey(uint256 pubkey)
        external responsible override
        returns (address user_addr)
    {
        require(msg.sender != address(0), Errors.internalMessageOnly);
        require(msg.value >= Sys.MinimalUserRegister, Errors.messageValueTooLow);
        TvmCell empty;
        address wal = _deployContract(Base.user, "",
            address.makeAddrStd(Sys.ExternalMetaChain, pubkey), empty);
        return {value: 0, bounce: false, flag: Flags.messageValue} wal;
    }

    function resolveUser(address user)
        public view responsible override
        returns (address user_addr)
    {
        return {value: 0, bounce: false, flag: Flags.messageValue}
            _resolveContract(Base.user, "", user);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Resolve address

    function resolve(uint8 ct_type, string name, address parent)
        public responsible view override
        returns (address res)
    {
        return {value: 0, bounce: false, flag: Flags.messageValue}
            _resolveContract(ct_type, name, parent);
    }

    function resolveFull(uint8 ct_type, string fullname)
        public responsible view override
        returns (address res)
    {
        string st = fullname;
        uint l = st.byteLength();
        uint s = 0;
        address adr = address(this);
        for (uint i = 0; i < l; i++) {
            if (st.substr(i, 1) == "/") {
                adr = _resolveContract(ct_type, st.substr(s, i - s), adr);
                s = i + 1;
            }
        }
        adr = _resolveContract(ct_type, st.substr(s, l - s), adr);
        return {value: 0, bounce: false, flag: Flags.messageValue}
            adr;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // System interaction

    function createAuction(address origin, uint32 revision, string name, uint8 duration)
        external responsible override
        returns (address auction)
    {
        verifyInteraction(Base.user, "", origin);
        require(revision >= user_revision, Errors.interactionOutdated);
        require(duration >= 1, Errors.invalidArgument);
        require(duration <= Sys.MaxDurationValue, Errors.invalidArgument);
        require(Now() >= no_auctions_until, Errors.auctionsAreRestricted);
        TvmBuilder param;
        param.store(duration);
        param.store(msg.sender);
        address auc = _deployContract(Base.auct, name, address(this), param.toCell());
        return {value: 0, bounce: false, flag: Flags.messageValue} auc;
    }

    function resolveAuction(string name)
        public view responsible override
        returns (address auct_addr)
    {
        return {value: 0, bounce: false, flag: Flags.messageValue}
            _resolveContract(Base.auct, name, address(this));
    }

    function onAuctionResult(address winner, uint32 exp, string name, address parent, bool deploy)
        external override
    {
        verifyInteraction(Base.auct, name, parent);
        if (winner != address(this))
            emit auctionResult(name, parent, winner, deploy);
        else
            emit certReserved(name, parent);
        if (deploy) {
            TvmBuilder param;
            param.store(winner, exp);
            /* address crt = */
            _deployContract(Base.cert, name, parent, param.toCell());
            /*
            ID4Cert(crt).applyAuctionResult{
                callback:  D4Root.applyAuctionCallback,
                   value:  Sys.CallValue,
                    flag:  Flags.addTransactionFees
            }(winner, exp);
            */
        }
    }

    function applyAuctionCallback(bool success)
        external
    {

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Subcertificate interaction

    function subCertDepl(string name, address parent, string subname, address new_owner, uint32 expiry)
        external override
    {
        verifyInteraction(Base.cert, name, parent);
        TvmBuilder param; param.store(new_owner, expiry);
        _deployContract(Base.cert, subname, msg.sender, param.toCell());
        IPasser(msg.sender).passToOwner{value: 0, bounce: false, flag: Flags.messageValue}();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Shattered contracts

    function receiveShards(uint8 ct_type, string name, address parent)
        external override
    {
        verifyInteraction(ct_type, name, parent);
        emit contractShattered(ct_type, msg.sender, name, parent);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Internal functions

    function _retrieveCode(uint8 ct_type)
        internal view
        returns (TvmCell ncode, uint32 nrev)
    {
        /**/ if (ct_type == Base.cert)
            { ncode = certificate_code; nrev = certificate_revision; }
        else if (ct_type == Base.auct)
            { ncode = auction_code; nrev = auction_revision; }
        else if (ct_type == Base.user)
            { ncode = user_code; nrev = user_revision; }
        else {
            TvmCell empty; ncode = empty; nrev = 0;
        }
        if (nrev == 0)
            revert(Errors.contractCodeNotInstalled);
    }

    function _deployContract(uint8 ct_type, string name, address parent, TvmCell param)
        internal view
        returns (address)
    {
        TvmCell ncode; uint32 nrev;
        (ncode, nrev) = _retrieveCode(ct_type);
        D4Base p = new D4Base{
            value: Sys.InitialBaseBalance,
            code: base_code,
            varInit: {
                  st_root: address(this),
                  st_type: ct_type,
                  st_name: name,
                st_parent: parent
            },
            flag: Flags.addTransactionFees
        }(ncode, nrev, param);
        return address(p);
    }

    function _resolveContract(uint8 ct_type, string name, address parent)
        internal view
        returns (address)
    {
        TvmCell stateInit = tvm.buildStateInit({
            contr: D4Base,
            code: base_code,
            varInit: {
                  st_root: address(this),
                  st_type: ct_type,
                  st_name: name,
                st_parent: parent
            }
        });
        return address(tvm.hash(stateInit));
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Code installation / update

    // Intentionally kept separate to prevent possible mistakes

    function setBaseCode(TvmCell code) // 0
        external override onlyOwner
    {
        require(base_revision == 0, Errors.baseCannotBeChanged);
        base_code = code; // Once and forever!
        base_revision = Now();
        emit codeUpdated(Base.base, tvm.hash(code));
    }

    function setCertificateCode(TvmCell code) // 1
        external override onlyOwner
    {
        certificate_code = code;
        certificate_revision = Now();
        emit codeUpdated(Base.cert, tvm.hash(code));
    }

    function setAuctionCode(TvmCell code) // 2
        external override onlyOwner
    {
        auction_code = code;
        auction_revision = Now();
        emit codeUpdated(Base.auct, tvm.hash(code));
    }

    function setUserCode(TvmCell code) // 3
        external override onlyOwner
    {
        user_code = code;
        user_revision = Now();
        emit codeUpdated(Base.user, tvm.hash(code));
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Upgrade the root contract

    function setRootCode(TvmCell code) // 255
        external override onlyOwner
    {
        _upgrade(code);
    }

    function _upgrade(TvmCell code)
        internal
    {
        emit rootCodeUpgraded(tvm.hash(tvm.code()), tvm.hash(code));
        tvm.setCurrentCode(code);
        tvm.setcode(code);
        TvmBuilder b;
        b.store(m_version, base_code, certificate_code, auction_code, user_code,
            base_revision, certificate_revision, auction_revision, user_revision,
            owner, smv_root, no_auctions_until, admin_enabled);
        onCodeUpgrade(b.toCell());
    }

    function onCodeUpgrade(TvmCell capsule) internal {}

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Subcontract upgrade routine

    function upgradeMeRequest(uint8 ct_type, uint32 my_revision, uint256 my_hash)
        external override
    {
        TvmCell ncode; uint32 nrev;
        (ncode, nrev) = _retrieveCode(ct_type);
        uint256 newhash = tvm.hash(ncode);
        if ((my_revision >= nrev) || (my_hash == newhash)) {
            IUpgradable(msg.sender).upgradeNotNeeded
                {value: 0, bounce: false, flag: Flags.messageValue}
                ();
            return;
        }
        emit subUpgraded(ct_type, msg.sender, my_revision, nrev, newhash);
        IUpgradable(msg.sender).upgrade
            {value: 0, bounce: false, flag: Flags.messageValue}
            (ncode, nrev);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // SMV configuration

    function assignSmvContract(address smv_addr)
        external override onlyOwner
    {
        emit smvContractConfigured(smv_root, smv_addr);
        smv_root = smv_addr;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Restrict auctions

    function restrictAuctions(uint32 until)
        external override onlyOwner
    {
        no_auctions_until = until;
        emit auctionsRestricted(until);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Ownership

    function getOwner()
        public view responsible override
        returns(address owner_)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            owner;
    }

    function getPendingOwner()
        public view responsible override
        returns(address pending_owner_)
    {
        return {value: 0, bounce: true, flag: Flags.messageValue}
            pending_owner;
    }

    function transferOwner(address new_owner, uint32 deadline)
        external override onlyOwner
    {
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
        owner = pending_owner;
        owner_transfer_deadline = 0;
        pending_owner = address(0);
    }

    function relinquishOwner()
        external override onlyOwner
    {
        if (Now() > relinquish_owner_deadline)
        {
            relinquish_owner_deadline = now + Sys.RelinquishOwnerTimeout;
            emit ownerRelinquishStart(owner, relinquish_owner_deadline);
            return;
        }
        emit ownerRelinquishComplete(owner);
        owner = address(0);
        pending_owner = address(0);
        owner_transfer_deadline = 0;
        relinquish_owner_deadline = 0;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Withdraw excess funds

    function withdrawable()
        public pure override
        returns (uint128 avail)
    {
        return address(this).balance - Sys.MinimalRootBalance;
    }

    function withdraw(address dest, uint128 value)
        external pure override onlyOwner
    {
        require(value <= withdrawable(), Errors.remainingBalanceTooLow);
        emit withdrawn(address(this).balance, value);
        dest.transfer(value, true);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Events

    event codeUpdated(uint8 codeType, uint256 codeHash);
    event subUpgraded(uint8 codeType, address subContract, uint32 from, uint32 to, uint256 newhash);

    event ownerTransferStart(address currentOwner, address nextOwner, uint32 deadline);
    event ownerTransferCancelled(address currentOwner);
    event ownerTransferComplete(address fromOwner, address toOwner);

    event ownerRelinquishStart(address curOwner, uint32 deadline);
    event ownerRelinquishComplete(address oldOwner);

    event smvContractConfigured(address curSMV, address newSMV);

    event withdrawn(uint128 oldBalance, uint128 withdrawn);

    event auctionsRestricted(uint32 until);

    event rootCodeUpgraded(uint256 from, uint256 to);

    event contractShattered(uint8 ct_type, address ct_addr, string name, address parent);

    event auctionResult(string name, address parent, address winner, bool deploy);
    event certReserved(string name, address parent);

    event adminFlagDropped(uint8 which, uint8 remain);
    event adminDeployed(string name, address set_owner, uint32 set_expiry);
    event adminReserved(string name);
    event adminChowned(string name, address set_owner);
    event adminChexped(string name, uint32 set_expiry);
    event adminUpgradedUser(address target);
    event adminUpgradedCert(address target);

    event smvCodeUpgrade(uint8 ct, uint256 chash);
    event smvReserveStart(string name);
    event smvReserveCommit(string name, bool result);
    event smvSetOwner(string name, address set_owner, uint32 set_expiry);
    event smvSetRootOwner(address new_owner);

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Now() for integration testing

    function Now()
        pure virtual internal inline
        returns (uint32)
    {
        return now;
    }

}