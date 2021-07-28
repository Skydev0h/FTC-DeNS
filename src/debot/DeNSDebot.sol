pragma ton-solidity >= 0.45.0;

pragma AbiHeader expire;
pragma AbiHeader time;
pragma AbiHeader pubkey;

import "./DeNSDebotHelper.sol";

interface IMultisig {
    function submitTransaction(
        address  dest,
        uint128 value,
        bool bounce,
        bool allBalance,
        TvmCell payload)
    external returns (uint64 transId);
}

contract DeNSDebot is Debot, Upgradable, Transferable {

    bytes d_icon;
    bytes nonce;
    address root;
    address helper;
    address user_wallet;
    address d4user;
    address certificate;
    address auction;
    bool certificate_deployed;
    bool auction_deployed;
    uint256 user_pubkey;
    uint256 bid_hash;
    uint128 bid_amount;
    TvmCell helper_code;
    TvmCell helper_si;
    uint32 trueFollowUp;
    uint32 falseFollowUp;
    bool d4UserIsDeployed;
    CertInfo certInfo;
    AuctInfo auctInfo;
    string nameToRegister;
    string masterKey;
    uint8 durationToRegister;
    
    function setHelperCode(TvmCell c) external {
        tvm.accept();
        helper_si = c;
    }

    function onCodeUpgrade() internal override {
        tvm.resetStorage();
    }

    function getRequiredInterfaces() public view override returns (uint256[] interfaces) {
        return [ Terminal.ID, AmountInput.ID, ConfirmInput.ID, AddressInput.ID ];
    }

    function getDebotInfo() public functionID(0xDEB) override view returns(
        string name, string version, string publisher, string key, string author,
        address support, string hello, string language, string dabi, bytes icon
    ) {
        name = "DeNS DeBot";
        version = format("{}.{}.{}", 0,0,1);
        publisher = "TON Labs";
        key = "DeNS";
        author = "TON Labs";
        support = address.makeAddrStd(0, 0xe97619544fb5d6115b2188350b1172b70952aac40705272d75f44c4685946fea);
        hello = "Hi, I will help you with decentralised names service.";
        language = "en";
        dabi = m_debotAbi.get();
        icon = d_icon;
    }

    constructor(address _root) public {
        require(user_pubkey != 0);
        require(msg.pubkey() == user_pubkey);
        tvm.accept();
        root = _root;
    }

    function initUserInfo() public {
        UserInfo.getAccount(tvm.functionId(setDefaultAccount));
        UserInfo.getPublicKey(tvm.functionId(setDefaultPubkey));
    }

    function setDefaultAccount(address value) public {
        Terminal.print(0, format("User account {}", value));
        user_wallet = value;
    }

    function setDefaultPubkey(uint256 value) public {
        Terminal.print(0, format("User public key {}", value));
        user_pubkey = value;
        TvmCell si = tvm.insertPubkey(helper_si, user_pubkey);
        helper_code  = si.toSlice().loadRef();
    }

    function setPubkeyInHelper() public {
        IDeNSDebotHelper(helper).setPubkey{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
        }(user_pubkey);
        getD4User();
    }

    function setupD4UserIsDeployed(bool result) public {
        d4UserIsDeployed = result;
    }

    function onError(uint32 sdkError, uint32 exitCode) public {
        exitCode = exitCode; sdkError = sdkError;
        ConfirmInput.get( tvm.functionId(retryTrans), "Transaction failed. Do you want to retry transaction?");
    }

    function retryTrans(bool value) public {
        if (value) {
            Terminal.print(trueFollowUp,"");
        } else {
            start();
        }
    }

    function miResolve() public {
        Terminal.input(tvm.functionId(resolveName), "Name to resolve:", false);
    }

    function resolveCert(string name) public {
        IDeNSDebotHelper(helper).resolveCert{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
        }(name);
        IDeNSDebotHelper(helper).getCertAddress{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(certAddressChecker),
            onErrorId: 0
        }();
    }

    function certAddressChecker(address result) public {
        certificate = result;
        trueFollowUp = tvm.functionId(certInfoExtracter);
        falseFollowUp = tvm.functionId(certUnawailable);
        Sdk.getAccountType(tvm.functionId(checkStatus), result);
    }

    function certUnawailable() public {
        certificate_deployed = false;
    }

    function certInfoExtracter() public {
        certificate_deployed = true;
        ID4Cert(certificate).getInfo{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(certInfoSetter),
            onErrorId: 0
        }();
    }

    function certInfoSetter(CertInfo info) public {
        certInfo = info;
    }

    function resolveAuct(string name) public {
        IDeNSDebotHelper(helper).resolveAuction{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
        }(name);
        IDeNSDebotHelper(helper).getCertAddress{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(auctAddressChecker),
            onErrorId: 0
        }();
    }

    function auctAddressChecker(address result) public {
        auction = result;
        trueFollowUp = tvm.functionId(auctInfoExtracter);
        falseFollowUp = tvm.functionId(auctUnawailable);
        Sdk.getAccountType(tvm.functionId(checkStatus), result);
    }

    function auctUnawailable() public {
        auction_deployed = false;
    }

    function auctInfoSetter(AuctInfo info) public {
        auctInfo = info;
    }

    function auctInfoExtracter() public {
        auction_deployed = true;
        ID4Auct(auction).getInfo{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(auctInfoSetter),
            onErrorId: 0
        }();
    }

    function resolveName(string value) public {
        this.resolveCert(value);
        this.resolveAuct(value);
        if (auction_deployed) {
            Terminal.print(0,format("info.name {}, info.durationYears {}, info.startTime {}, info.bidEnds {}, info.revEnds {}, info.finalizeAfter {}, info.expiryTarget {}", auctInfo.name, auctInfo.durationYears, auctInfo.startTime, auctInfo.bidEnds, auctInfo.revEnds, auctInfo.finalizeAfter, auctInfo.expiryTarget));
        } else {
            Terminal.print(0, "No auctions for specified name deployed.");
        }
        if (certificate_deployed) {
            Terminal.print(0, format("certInfo.name {}, certInfo.parent {}, certInfo.registered {}, certInfo.auctioned {}, certInfo.expires {}", certInfo.name, certInfo.parent, certInfo.registered, certInfo.auctioned, certInfo.expires));
        } else {
            Terminal.print(0, "No certificates for specified name deployed.");
        }
        start();
    }

    function miRegister() public {
        Terminal.input(tvm.functionId(registerName), "Name to register:", false);
    }

    function onBidPaymentSuccess(uint64 transId) public {
        Terminal.print(0, "Bid payment processed.");
        start();
    }

    function biddingChached(bytes output) public {
        trueFollowUp = tvm.functionId(amiBid);
        TvmCell payload = tvm.encodeBody(IDeNSDebotHelper.makeBid, auction, output, bid_hash);
            IMultisig(user_wallet).submitTransaction{
            abiVer: 2,
            extMsg: true,
            sign: true,
            pubkey: user_pubkey,
            time: uint64(now),
            expire: 0,
            callbackId: tvm.functionId(onBidPaymentSuccess),
            onErrorId: tvm.functionId(onError)
        }(helper, bid_amount, true, false, payload);
    }

    function secretBidKeyEntered(string value) public {
        TvmBuilder b1;
        b1.store(value, user_wallet, auction, auctInfo.startTime, d4user);
        uint256 h = tvm.hash(b1.toCell());

        TvmBuilder b2;
        b2.store(h);
        TvmBuilder bmain;
        bmain.storeRef(b2);
        nonce = bmain.toSlice().decode(bytes);
        delete bmain;

        TvmBuilder b3;
        b3.store(auction, auctInfo.startTime, d4user, bid_amount, nonce);
        bid_hash = tvm.hash(b3.toCell());  

        TvmBuilder b4;
        b4.store(bid_amount);
        bmain.storeRef(b4);
        bytes amount = bmain.toSlice().decode(bytes);
        
        Sdk.chacha20(tvm.functionId(biddingChached), amount, nonce, bid_hash);
        
    }

    function bidAmountSet(uint128 value)  public {
        bid_amount = value;
        Terminal.input(tvm.functionId(secretBidKeyEntered), "Enter master key. At least 32 symbols long.", false);
    }

    function amiBid() public {
        AmountInput.get(tvm.functionId(bidAmountSet), "Enter desired bid amount" , 1, Sys.MinumumPossibleBid, 10000);
    }

    function registerDuration(int256 value) public {
        durationToRegister = uint8(value % 2**8);
        processPaymentForAuctionDeploy();
    }

    function onRegistrationPaymentSuccess(uint64 transId) public {
        Terminal.print(tvm.functionId(amiBid), "Auction contract deployment funds sent. Continue by making bid.");
    }

    function processPaymentForAuctionDeploy() public {
        trueFollowUp = tvm.functionId(processPaymentForAuctionDeploy);
        TvmCell payload = tvm.encodeBody(IDeNSDebotHelper.createAuction, nameToRegister, durationToRegister);
            IMultisig(user_wallet).submitTransaction{
            abiVer: 2,
            extMsg: true,
            sign: true,
            pubkey: user_pubkey,
            time: uint64(now),
            expire: 0,
            callbackId: tvm.functionId(onRegistrationPaymentSuccess),
            onErrorId: tvm.functionId(onError)
        }(helper, Sys.MinimalRegNameRequest, true, false, payload);
    }

    function registerName(string value) public {
        nameToRegister = value;
        this.resolveCert(value);
        this.resolveAuct(value);
        if (auction_deployed && auctInfo.bidEnds <= now) {
            Terminal.print(0, "Auction was already running before your request, Bid making is closed.");
            start();
        }
        if (certificate_deployed && certInfo.expires > now + Sys.ExpiringAuctionPermit * 3600 * 24) {
            Terminal.print(0, "Certificate was already deployed before your request and there is more than 28 days till expiration.");
            start();
        }
        if (auction_deployed && auctInfo.bidEnds > now) {
            Terminal.print(0, format("There is auction for the specified name running already, booking duration is set to {}.", auctInfo.durationYears));
            amiBid();
        } else {
            NumberInput.get(tvm.functionId(registerDuration), "Enter desired booking duration in days", 8, 255);
        }
    }

    function amiFinalize() public {
        if (now < auctInfo.revEnds) {
            Terminal.print(0, "It's too early to finalize");
        } else {
            ID4User(d4user).finalize{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
            }(auction);
        }
    }

    function bidRevelation(bytes output) public {
        TvmBuilder b;
        b.store(output);
        TvmBuilder bmain;
        bmain.storeRef(b);
        bid_amount = bmain.toSlice().decode(uint128);
        delete b;
        delete bmain;
        b.store(nonce);
        bmain.storeRef(b);
        uint128 b_nonce = bmain.toSlice().decode(uint128);

        ID4User(d4user).revealBid{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
            }( auction, bid_amount, b_nonce);
    }

    function bidReconstruction(AuctBid res) public {
        bytes    b_data = res.data;
        uint256  b_hash = res.hash;

        TvmBuilder b1;
        b1.store(masterKey, user_wallet, auction, auctInfo.startTime, d4user);
        uint256 h = tvm.hash(b1.toCell());

        TvmBuilder b2;
        b2.store(h);
        TvmBuilder bmain;
        bmain.storeRef(b2);
        nonce = bmain.toSlice().decode(bytes);
        delete bmain;

        TvmBuilder b3;
        b3.store(masterKey, auction, d4user);
        uint256 key = tvm.hash(b3.toCell());
        
        Sdk.chacha20(tvm.functionId(bidRevelation), b_data, nonce, b_hash);
    }

    function bidExists(bool res) public {
        if (res) {
            ID4User(d4user).getBid{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(bidReconstruction),
            onErrorId: 0
            }(auction);
        } else {
            Terminal.print(0, "No bids found for specified auction.");
            start();
        }
    }

    function secretBidRevealKeyEntered(string value) public {
        masterKey = value;
        ID4User(d4user).hasBid{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(bidExists),
            onErrorId: 0
            }(auction);
    }

    function amiReveal() public {
        Terminal.input(tvm.functionId(secretBidRevealKeyEntered), "Enter master key. Same as entered on bid creation.", false);
    }

    function amiWithdraw() public {}

    function auctNameProcessing(string value) public {
        this.resolveAuct(value);
        if (auction_deployed) {
            Menu.select ("Options", "Available debot actions", [
            MenuItem("Bid",         "Make bid",             tvm.functionId(amiBid)),
            MenuItem("Finalize",    "Finalize auction",     tvm.functionId(amiFinalize)),
            MenuItem("Reveal",      "Reveal bid",           tvm.functionId(amiReveal)),
            MenuItem("Withdraw",    "Withdraw bid",         tvm.functionId(amiWithdraw)),
            MenuItem("Quit", "", 0)
            ]);
        } else {
            Terminal.print(0, "There is no auction for the name specified");
            start();
        }
    }

    function miAuction() public {
        Terminal.input(tvm.functionId(auctNameProcessing), "Name for corresponding auction:", false);
    }

    function _displayMenu() private {
        Menu.select ("Options", "Available debot actions", [
            MenuItem("Resolve",     "Resolve name",             tvm.functionId(miResolve)),
            MenuItem("Register",    "Register name",            tvm.functionId(miRegister)),
            MenuItem("Auction",     "Participate in auctions",  tvm.functionId(miAuction)),
            MenuItem("Quit", "", 0)
        ]);
    } 

    function setupD4User(address result) public {
        d4user = result;
        _displayMenu();
    }

    function receiveD4User() public {
        IDeNSDebotHelper(helper).getD4User{
            abiVer: 2,
            extMsg: true,
            sign: true,
            pubkey: user_pubkey,
            time: uint64(now),
            expire: 0,
            callbackId: tvm.functionId(setupD4User),
            onErrorId: 0
        }();
    }

    function onSuccess(uint64 transId) public {
        Terminal.print(tvm.functionId(receiveD4User), "Started DeNS user smart contract deployment");
    }

    function processPaymentForUserDeploy() public {
        trueFollowUp = tvm.functionId(processPaymentForUserDeploy);
        if (!d4UserIsDeployed) {
            TvmCell payload = tvm.encodeBody(IDeNSDebotHelper.createD4User);
            IMultisig(user_wallet).submitTransaction{
            abiVer: 2,
            extMsg: true,
            sign: true,
            pubkey: user_pubkey,
            time: uint64(now),
            expire: 0,
            callbackId: tvm.functionId(onSuccess),
            onErrorId: tvm.functionId(onError)
            }(helper, Sys.MinimalUserRegister, true, false, payload);
        } else {
            receiveD4User();
        }
    }

    function checkD4UserIsDeployed() public {
        IDeNSDebotHelper(helper).isD4Userdeployed{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: user_pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(setupD4UserIsDeployed),
            onErrorId: 0
        }();
    }  

    function getD4User() public {
        this.checkD4UserIsDeployed();
        this.processPaymentForUserDeploy();
    }
    
    function deployHelper() public {
        helper = new DeNSDebotHelper {
            value: 0.1 ton,
            flag: 1,
            code: helper_code,
            pubkey: user_pubkey,
            varInit: {}
        }(user_wallet, root);
        setPubkeyInHelper();
        
    }

    function searchHelper() public {
        trueFollowUp = tvm.functionId(setPubkeyInHelper);
        falseFollowUp = tvm.functionId(deployHelper);
        Sdk.getAccountsDataByHash(tvm.functionId(onAccountsByHash), tvm.hash(helper_code), address(0x0));
    }

    function onAccountsByHash(AccData[] accounts) public {
        if (accounts.length == 0) {
            Terminal.print(falseFollowUp, "");
        } else {
            helper = accounts[0].id;
            Terminal.print(trueFollowUp, "");
        }
    }

    function checkRootInitialized() public {
        falseFollowUp = 0;
        trueFollowUp = tvm.functionId(searchHelper);
        Sdk.getAccountType(tvm.functionId(checkStatus), root);
    }

    function checkStatus(int8 acc_type) public {
        if (acc_type == -1 || acc_type == 0 || acc_type == 2)  {
            Terminal.print(falseFollowUp, "");
        } else {
            Terminal.print(trueFollowUp, "");
        }
    }

    function start() public override {
        this.initUserInfo();
        this.checkRootInitialized();
    }
}