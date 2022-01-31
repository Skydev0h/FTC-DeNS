pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4Auct is ID4Auct, D4Based {

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Variables

    // bool public isFragile;
    // bool public isReady;

    uint32 public startTime;
    uint32 public bidEnds;
    uint32 public revEnds;

    uint8  public durationYears;
    // uint8  public ctorDuration;

    uint32 public expiryBase;
    uint32 public expiryTarget;
    uint32 public finalizeAfter;

    address public instigator;

    // Statistics

    uint32 public bids;
    uint32 public revs;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Revealing

    address public top1;
    uint128 public amt1;

    address public top2;
    uint128 public amt2;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Constructor

    constructor() public { revert(Errors.directDeployForbidden); }

    function onCodeUpgrade(TvmCell param, TvmCell capsule)
        internal
    {
        require(m_version == Sys.IsContructorCall, Errors.invalidArgument);
        tvm.resetStorage();
        TvmSlice s = capsule.toSlice();
        unpackBase(s);
        TvmSlice sl = param.toSlice();
        durationYears = sl.loadUnsigned(8);
        instigator = sl.decode(address);
        m_version = 1;
        // isFragile = isReady = false;
        // startTime = bidEnds = revEnds = expiryBase = expiryTarget = finalizeAfter = 0;
        // top1 = top2 = address(0); amt1 = amt2 = 0;
        // bids = revs = 0;
        IRegPre(_resolveContract(Base.cert, st_name, st_parent)).registrationPreflight{
            callback:  D4Auct.registrationPreflightCallback,
               value:  Sys.CallValue,
                flag:  Flags.addTransactionFees
        }(0);
    }

    /* modifier notFragile() {
        require(!isFragile, Errors.contractIsFragile);
        _;
    } */

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function registrationPreflightCallback(uint128, uint32 expiry_)
        external override
        // notFragile
    {
        verifyInteraction(Base.cert, st_name, st_parent);
        if (expiry_ == 0) // D4Base
            IDestructible(msg.sender).destroy();
        if ((Now() >= expiry_) || (expiry_ - Now() < Sys.ExpiringAuctionPermit)) {
            // isReady = true;
            expiryBase = expiry_;
            configure();
            return;
        }
        // isFragile = true; // Certificate exists and is not expiring soon
        destroy();
    }

    onBounce(TvmSlice slice)
        external
    {
        uint32 functionId = slice.decode(uint32);
        if (functionId == tvm.functionId(IRegPre.registrationPreflight)) {
            uint32 callbackFunctionId = slice.loadUnsigned(32);
            verifyInteraction(Base.cert, st_name, st_parent);
            if (callbackFunctionId == tvm.functionId(D4Auct.registrationPreflightCallback))
                // if (!isFragile) { isReady = true; }
                configure();
        }
        if (functionId == tvm.functionId(ID4Cert.applyAuctionResult)) {
            uint32 callbackFunctionId = slice.loadUnsigned(32);
            verifyInteraction(Base.cert, st_name, st_parent);
            if (callbackFunctionId == tvm.functionId(D4Auct.applyAuctionCallback))
                requestCertificateDeploy();
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Query quasistatic information

    function getInfo()
        public responsible view override
        returns (AuctInfo info)
    {
        return {value: 0, bounce: false, flag: Flags.messageValue}
        AuctInfo(
            0, 0,
            st_name, st_parent,
            durationYears, startTime,
            bidEnds, revEnds,
            finalizeAfter, expiryTarget
        );
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function configure() //(address user, uint8 duration)
        internal // public override // notFragile
    {
        tvm.accept();
        // if (msg.sender != address(this))
        //     verifyInteraction(Base.user, "", user);
        // uint8 duration = ctorDuration;
        // require(isReady, Errors.contractNotReady);
        // require(durationYears == 0, Errors.alreadyInitialized);
        if (durationYears == Sys.ReserveDuration) {
            reserve();
            return;
        }
        if (durationYears == Sys.ReserveNOWDuration) {
            reserve();
            _commit(true);
            return;
        }
        // require(durationYears >= 1, Errors.invalidArgument);
        // require(durationYears <= Sys.MaxDurationValue, Errors.invalidArgument);
        durationYears = math.min(math.max(durationYears, uint8(1)), Sys.MaxDurationValue);
        // durationYears = duration;
        startTime = Now();
        uint32 dur = math.min(durationYears, Sys.MaxTimingYearsPeriod);
        bidEnds = startTime + Sys.BidPeriodPerYear * dur;
        revEnds = bidEnds + Sys.RevealPeriodPerYear * dur;
        uint256 exp = uint256(math.max(revEnds, expiryBase)) +
                      uint256(durationYears) * uint256(365 days);
        if (exp > Sys.MaxU32) exp = Sys.MaxU32;
        expiryTarget = uint32(exp);
        if (expiryBase > 0) {
            finalizeAfter = math.max(revEnds, expiryBase) + Sys.ProlongGrace;
            ID4Cert(_resolveContract(Base.cert, st_name, st_parent)).ensureExpiry
                {value: 0, bounce: true, flag: Flags.messageValue}
                (finalizeAfter + Sys.ReAuctionGrace, true);
        }
        if (instigator != address(0))
        {
            ID4User(instigator).queryAuctCallback{value:Sys.CallValue}(getInfo());
        }
    }

    function reserve()
        internal
    {
        if (expiryBase > 0) {
            // Impossible to reserve already existing certificate even if expiring
            destroy();
        }
        startTime = bidEnds = expiryTarget = Sys.MaxU32;
        revEnds = finalizeAfter = Now() + Sys.ReserveSafetyTimeout;
    }

    function commit(bool result)
        public view override
        onlyRoot
    {
        tvm.accept();
        require(startTime == Sys.MaxU32, Errors.methodIsNotCallable);
        _commit(result);
    }

    function _commit(bool result)
        internal view
    {
        if (result)
            ID4Root(st_root).onAuctionResult
                {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
                (st_root, expiryTarget, st_name, st_parent, true);
        else
            destroy();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function accountBid(address user)
        external override
        // notFragile // startTime <= Now() < bidEnds
    {
        verifyInteraction(Base.user, "", user);
        require(Now() >= startTime, Errors.bidWasMadeTooEarly);
        require(Now() < bidEnds, Errors.bidWasMadeTooLate);
        bids += 1;
        emit bidPlaced(msg.sender);
        // msg.sender.transfer({value: 0, bounce: false, flag: Flags.messageValue});
        IPasser(msg.sender).passToOwner{value: 0, bounce: false, flag: Flags.messageValue}();
    }

    function revealBid(address user, uint32 bid_time, uint128 amount, uint128 nonce, uint256 prover)
        external override
        // notFragile // bidEnds <= Now() < revEnds
    {
        verifyInteraction(Base.user, "", user);
        require(bid_time >= startTime, Errors.bidWasMadeTooEarly);
        require(bid_time < bidEnds, Errors.bidWasMadeTooLate);
        require(Now() >= bidEnds, Errors.invalidTimePhase);
        require(Now() < revEnds, Errors.invalidTimePhase);
        // Verify proof //
        TvmBuilder b;
        b.store(address(this), startTime, user, amount, nonce);
        uint256 verifier = tvm.hash(b.toCell());
        require(prover == verifier, Errors.bidProofInvalid);
        require(msg.value >= amount + Sys.AddToReveal, Errors.messageValueTooLow);
        revs += 1;
        emit bidRevealed(msg.sender, amount);
        ID4User(msg.sender).bidRevealComplete{value: Sys.CallValue}();
        uint128 bal = address(this).balance - msg.value;
        if (amount <= amt2) {
            ID4User(msg.sender).addLocked{value: amount, bounce: false}(revEnds, st_name, st_parent);
            // msg.sender.transfer({value: 0, bounce: false, flag: Flags.messageValue});
            tvm.rawReserve(bal, 0);
            msg.sender.transfer({value: 0, bounce: false, flag: Flags.contractBalance});
            return;
        }
        if (amount <= amt1) {
            top2 = msg.sender;
            amt2 = amount;
            emit topUpdated(2, top2, amt2);
            ID4User(msg.sender).addLocked{value: amount, bounce: false}(revEnds, st_name, st_parent);
            // msg.sender.transfer({value: 0, bounce: false, flag: Flags.messageValue});
            tvm.rawReserve(bal, 0);
            msg.sender.transfer({value: 0, bounce: false, flag: Flags.contractBalance});
            return;
        }
        if (amt1 != 0) {
            // XXX: Break auction using a small bid
            // Audit suggests call flag: 1, why? It should not error out code 37!
            ID4User(top1).addLocked{value: amt1, bounce: false}(revEnds, st_name, st_parent);
            top2 = top1;
            amt2 = amt1;
            emit topUpdated(2, top2, amt2);
            bal -= amt1;
        }
        top1 = msg.sender;
        amt1 = amount;
        emit topUpdated(1, top1, amt1);
        tvm.rawReserve(bal + amount, 0);
        msg.sender.transfer({value: 0, bounce: false, flag: Flags.contractBalance});
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function requiredAmountForProlong()
        public view responsible override
        returns (uint128 amount)
    {
        uint128 prolongRequired = amt1 - amt2;
        if (prolongRequired == 0)
            prolongRequired = amt1;
        prolongRequired = Sys.ProlongMultiplier * prolongRequired
                          / Sys.ProlongDivisor;
        return prolongRequired;
    }

    function prolong()
        external override
    {
        // Can be asked by cert owner only
        verifyInteraction(Base.cert, st_name, st_parent);
        require(Now() >= revEnds, Errors.invalidTimePhase);
        // require(Now() < finalizeAfter, Errors.invalidTimePhase);
        // Certificate owner can request prolong until auction is finalized by someone
        uint128 prolongRequired = requiredAmountForProlong();
        require(msg.value >= prolongRequired + Sys.AddToProlong, Errors.messageValueTooLow);
        if (amt1 != 0) {
            ID4User(top1).addLocked{value: amt1, bounce: false}(revEnds, st_name, st_parent);
            // top1 = top2 = address(0);
            // amt1 = amt2 = 0;
        }
        emit certProlonged(prolongRequired);
        ID4Cert(_resolveContract(Base.cert, st_name, st_parent)).ensureExpiry
            {value: msg.value - prolongRequired, bounce: false}(expiryTarget, false);
        // isFragile = true;
        destroy();
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function finalize(address user)
        external override
        // notFragile
    {
        if (msg.sender != st_root)
            verifyInteraction(Base.user, "", user);
        require(Now() >= math.max(revEnds, finalizeAfter), Errors.invalidTimePhase);
        if (amt1 == 0) {
            // Failed
            emit auctionFailed();
            msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
            ID4Root(st_root).onAuctionResult
                {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
                (address(0), expiryTarget, st_name, st_parent, false);
            return;
        }
        uint128 paid = amt1;
        if (amt2 > 0) {
            uint128 rem = amt1 - amt2;
            paid = amt2;
            if (rem > 0) {
                top1.transfer({value: rem, bounce: true});
            }
        }
        finalizeAfter = Sys.MaxU32;  // prevent re-entry while waiting for response
        emit auctionSucceded(top1, paid);
        msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
        if (expiryBase > 0) {
            // Updating an existing contract
            // msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
            ID4Cert(_resolveContract(Base.cert, st_name, st_parent)).applyAuctionResult{
                callback:  D4Auct.applyAuctionCallback,
                   value:  Sys.CallValue,
                    flag:  Flags.addTransactionFees
            }(top1, expiryTarget);
            // ID4Root(st_root).onAuctionResult
            //     {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
            //     (top1, expiryTarget, st_name, st_parent, false);
        } else {
            // Deploying a new contract
            // msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
            requestCertificateDeploy();
        }
        // msg.sender.transfer({value: 0, bounce: true, flag: Flags.messageValue});
        // tvm.rawReserve(address(this).balance - msg.value, 0);
        // msg.sender.transfer({value: 0, bounce: false, flag: Flags.contractBalance});
    }

    function applyAuctionCallback(bool success)
        external view
    {
        verifyInteraction(Base.cert, st_name, st_parent);
        if (!success) {
            // Certificate rejects auction result (???)
            top1.transfer({value: (amt2 == 0) ? amt1 : amt2, bounce: true});
            emit auctionRejected(top1);
            ID4Root(st_root).onAuctionResult
                {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
                (address(0), expiryTarget, st_name, st_parent, false);
            return;
        }
        // isFragile = true;
        ID4Root(st_root).onAuctionResult
            {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
            (top1, expiryTarget, st_name, st_parent, false);
    }

    function requestCertificateDeploy()
        internal view // bounce
    {
        ID4Root(st_root).onAuctionResult
            {value: 0, bounce: false, flag: Flags.sendAllThenDestroy}
            (top1, expiryTarget, st_name, st_parent, true);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    function destroy() // shatter
        internal view // public view override
    {
        // require(isFragile, Errors.contractNotFragile);
        ID4Root(st_root).receiveShards{
             value:  0,
            bounce:  false,
              flag:  Flags.sendAllThenDestroy
        } (st_type, st_name, st_parent);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Events

    event topUpdated(uint8 num, address user, uint128 amount);
    event bidPlaced(address user);
    event bidRevealed(address user, uint128 amount);

    event certProlonged(uint128 price);

    event auctionFailed();
    event auctionSucceded(address winner, uint128 paid);
    event auctionRejected(address winner);

}