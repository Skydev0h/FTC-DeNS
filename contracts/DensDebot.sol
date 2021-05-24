pragma ton-solidity >=0.42.0;
pragma AbiHeader expire;
pragma AbiHeader time;
pragma AbiHeader pubkey;

import "ui/AddressInput.sol";
import "ui/AmountInput.sol";
import "ui/ConfirmInput.sol";
import "ui/Debot.sol";
import "ui/Menu.sol";
import "ui/Sdk.sol";
import "ui/Terminal.sol";
import "ui/Transferable.sol";
import "ui/Upgradable.sol";
import "ui/NumberInput.sol";
import "./DeNSRoot.sol";

import "./Interfaces.sol";
import "./Libraries.sol";
import "./Structures.sol";

contract DeNSDebot is Debot, Upgradable, Transferable, IDataStructs {
    address root;
    bytes nIcon;
    address currentResolvedAuction;
    address currentResolvedCertificate;
    address currentResolvedBid;
    address msigWallet;
    string targetSCname;
    uint32 targetFunctionToRun;
    int8 accTypeForCheck;
    string nameToRegister;
    int currentCertExpireDays;
    RegRequest request;
    uint128 bidAmount;
    uint256 nonce;

    constructor(address _root) public {
        require(tvm.pubkey() != 0);
        require(msg.pubkey() == tvm.pubkey());
        tvm.accept();
        root = _root;
    }

    function generateHash(address bidder, uint128 amount, uint256 nonc) private returns(uint256)
    {
        TvmBuilder b; b.store(bidder, amount, nonc);
        uint256 rhash = tvm.hash(b.toCell());
        return rhash;
    }

    function onCodeUpgrade() internal override {
        tvm.resetStorage();
    }

    function getRequiredInterfaces() public view override returns (uint256[] interfaces) {
        return [ Terminal.ID, AmountInput.ID, ConfirmInput.ID, AddressInput.ID ];
    }

    function getDebotInfo() public functionID(0xDEB) override view returns(
        string name, string version, string publisher, string caption, string author,
        address support, string hello, string language, string dabi, bytes icon
    ) {
        name = "DeNS interactions";
        version = format("{}.{}.{}", 0,0,1);
        publisher = "TON Labs";
        caption = "DeBot for DeNS";
        author = "TON Labs";
        support = address.makeAddrStd(0, 0x97619544fb5d6115b2188350b1172b70952aac40705272d75f44c4685946fea);
        hello = "Hi, I will help you with DeNS manipulations.";
        language = "en";
        dabi = m_debotAbi.get();
        icon = nIcon;
    }

    function start() public override {
        Terminal.print(0, "Welcome to the DeNS debot!");
        Terminal.print(0, "Please select your option:");
        Menu.select ("Options", "Available debot actions", [
            MenuItem("Resolve",     "Resolve name",             tvm.functionId(miResolve)),
            MenuItem("Register",    "Register name",            tvm.functionId(miRegister)),
            MenuItem("Auction",     "Participate in auctions",  tvm.functionId(miAuction)),
            MenuItem("Quit", "", 0)
        ]);
    }

    function miResolve(uint32 index) public {
            require(index >= 0);
            Terminal.input(tvm.functionId(resolveName), "Name to resolve:", false);
    }

    function resolveName(string value) public {
        this.resolveCertByName(value);
        if (this.checkStatus()) {
            resolveOfExistingCert(currentResolvedCertificate);
        }
        this.resolveAucByName(value);
        if (this.checkStatus()) {
            optional(uint256) pubkey;
            IDensAuction(currentResolvedAuction).start{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(printAuctionStartData),
                onErrorId: 0
            }();

            IDensAuction(currentResolvedAuction).expiry{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(printAuctionExpiryData),
                onErrorId: 0
            }();
        }
        this.start();
    }

    function printAuctionStartData(uint32 start) {
        Terminal.print(0, format("Start of auction at time {}", start));
    }

    function printAuctionExpiryData(uint32 expiry) {
        Terminal.print(0, format("Auction expires at {}", expiry));
    }

    function resolveCertByName(string value) public {
        targetSCname = "Certificate";
        optional(uint256) pubkey;
        IDensRoot(root).resolve{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(onResolve),
                onErrorId: 0
            }(value);
    }

    function resolveAucByName(string value) public {
        targetSCname = "Auction";
        optional(uint256) pubkey;
        IDensRoot(root).auction{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(onResolve),
                onErrorId: 0
            }(value);
    }

    function onResolve(address value0) public {
        if (targetSCname == "Certificate") {
            currentResolvedCertificate = value0;
        }
        if (targetSCname == "Auction") {
            currentResolvedAuction = value0;
        }
        Sdk.getAccountType(tvm.functionId(setAccTypeResult), value0);
    }

    function setAccTypeResult(int8 acc_type) {
        accTypeForCheck = acc_type;
    }

    function checkStatus() public returns (bool) {
        if (accTypeForCheck == -1)  {
            Terminal.print(0, format("{} does not exist.", targetSCname));
            return false;
        }
        if (accTypeForCheck == 0) {
            Terminal.print(0, format("{} exists", targetSCname));
            return true;
        }
    }

    function resolveOfExistingCert(address value) public {
        Terminal.print(0, "Requesting value...");
        IDensCertificate(value).whois{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(onResolveWhois),
            onErrorId: 0
        }();
        return;
    }

    function onResolveWhois(Whois value0) public {
        Terminal.print(0, "Received information:");
        Terminal.print(0, format("Owner: {}", value0.owner));
        Terminal.print(0, format("Registered: {}s ago", now - value0.registered));
        currentCertExpireDays = (int(value0.expiry) - int(now)) / 86400;
        Terminal.print(0, format("Expires: in {}d", currentCertExpireDays));
        Terminal.print(0, format("Address value (request result):\n{}", value0.value));
    }

    function enterMsigWallet() {
        AddressInput.get(tvm.functionId(saveAndVerifyWallet), "Please enter adress of multisig wallet");
    }
    
    function saveAndVerifyWallet(address value) public {
        Sdk.getAccountType(tvm.functionId(checkWalletStatus), value);
        msigWallet = value;
    }

    function checkWalletStatus(int8 acc_type) public {
        if (!_checkActiveStatus(acc_type)) {
            Terminal.print(0, "Can't proceed with this wallet.");
            start();
        }
        Sdk.getAccountCodeHash(tvm.functionId(checkWalletHash), m_wallet);
    }

    function checkWalletHash(uint256 code_hash) public {
        // safe msig
        if (code_hash != 0x80d6c47c4a25543c9b397b71716f3fae1e2c5d247174c52e2c19bd896442b105 &&
        // surf msig
            code_hash != 0x207dc560c5956de1a2c1479356f8f3ee70a59767db2bf4788b1d61ad42cdad82 &&
        // 24 msig
            code_hash != 0x7d0996943406f7d62a4ff291b1228bf06ebd3e048b58436c5b70fb77ff8b4bf2 &&
        // 24 setcode msig
            code_hash != 0xa491804ca55dd5b28cffdff48cb34142930999621a54acee6be83c342051d884 &&
        // setcode msig
            code_hash != 0xe2b60b6b602c10ced7ea8ede4bdf96342c97570a3798066f3fb50a4b2b27a208) {
            start();
        }
        Terminal.print(targetFunctionToRun,"");
    }

    function _checkActiveStatus(int8 acc_type) private returns (bool) {
        if (acc_type == -1)  {
            Terminal.print(0, obj + "Wallet is inactive");
            return false;
        }
        if (acc_type == 0) {
            Terminal.print(0, obj + "Wallet is uninitialized");
            return false;
        }
        if (acc_type == 2) {
            Terminal.print(0, obj + "Wallet is frozen");
            return false;
        }
        return true;
    }

    function miRegister(uint32 index) public {
        require(index >= 0);
        Terminal.input(tvm.functionId(readDesiredName), "Enter name to register:", false);
    }

    function readDesiredName(string value) public {
        nameToRegister = value;
        resolveCertByName(value);
        if (this.checkStatus()) {
            resolveOfExistingCert(currentResolvedCertificate);
            if (currentCertExpireDays > 28) {
                Terminal.print(tvm.functionId(start), format("Name {} can't be registered", nameToRegister));
            }
        }
        this.resolveAucByName(value);
        if (this.checkStatus()) {
            Terminal.print(0, "Auction for name was already running.")
            optional(uint256) pubkey;
            IDensAuction(currentResolvedAuction).expiry{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(checkAucNotExpired),
                onErrorId: 0
            }();
        }
    }

    function checkAucNotExpired(uint32 expiry) {
        if (expire > now) {
            Terminal.print(tvm.functionId(), "Auction is currently running. Want to participate?");
            Menu.select ("Options", "Available debot actions", [
            MenuItem("Participate", "Participate in Auction",   tvm.functionId(participateInAuction)),
            MenuItem("Main menu",   "Go to main menu",          tvm.functionId(start))
        } else {
            _registerName(nameToRegister);
        }
    }

    function _registerName(string value) private {
        request.name = value;
        NumberInput.get(tvm.functionId(setRequestedDuration), "Please enter desired duration (in years):", 1, 100);
    }
    
    function setRequestedDuration(uint32 value) public {
        request.duration = value;
        AmountInput.get(tvm.functionId(setHashedAmount), "Please enter desired amount for the bid:", 9, 1, 1e13);
    }

    function setHashedAmount(uint128 value) public {
        bidAmount = value;
        nonce = rnd.next();
        AddressInput.get(tvm.functionId(userAddressSpecified), "Please select wallet address you want to use:");
    }

    function userAddressSpecified(address value) public {
        bidderPaymentAddress = value;
        msigWallet = value;
        sendRegRequest(generateHash(bidderPaymentAddress, bidAmount, nonce));
    }

    function sendRegRequest(uint256 value) private {
        request.hash = value;
        TvmCell payload = tvm.encodeBody(IDensRoot.regName, request);
        optional(uint256) pubkey;
        IMultisig(msigWallet).submitTransaction{
            abiVer: 2,
            extMsg: true,
            sign: true,
            pubkey: pubkey,
            time: uint64(now),
            expire: 0,
            callbackId: tvm.functionId(regNameCallback),
            onErrorId: tvm.functionId(onError)
        }(root, 1e9, true, false, payload);
    }

    function onError(uint32 sdkError, uint32 exitCode) public {
        exitCode = exitCode; sdkError = sdkError;
        Terminal.print(tvm.functionId(start), "Transaction failed.");
    }

    function regNameCallback() public {
        //ВЫЗОВ СОХРАНЕНЕНИЯ в dens bid box 
        start();
    }

    function miAuction(uint32 index) public {
        require(index >= 0);
        Menu.select ("Options", "Available debot actions", [
            MenuItem("List",        "List existing auctions",           tvm.functionId(mi_listExistingAuctions)),
            MenuItem("Participate", "Participate in auctions",          tvm.functionId(mi_participateInAuction)),
            MenuItem("Reveal",      "Reveal bid",                       tvm.functionId(mi_revealBid)),
            MenuItem("Finalize",    "Finalize auction",                 tvm.functionId(mi_finalizeAuction)),
            MenuItem("Withdraw",    "Withdraw previously revealed bid", tvm.functionId(mi_withdrawBid)),
            MenuItem("Quit", "", 0)
            ]);
    }

    function mi_listExistingAuctions() public {
        DensRoot(root).auction_code{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: getAccountsDataByHash,
                onErrorId: 0
            }();
    }

    function getAccountsDataByHash(TvmCell auction_code) public {
        uint256 h = tvm.hash(auction_code);
        Sdk.getAccountsDataByHash(tvm.functionId(onAccountsByHash),h,address(0x0));
    }

    function onAccountsByHash(ISdk.AccData[] accounts) public {
        if (accounts.length == 0) {
            Terminal.print(0,"No running auctions!");
        }
        for (uint i=0; i<accounts.length;i++)
        {
            Terminal.print(0,format("Name {} Address {}",DensAuction(accounts[i].id).name{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: 0,
                onErrorId: 0
            }(), accounts[i]));
        }
        m_count += accounts.length;
        if (accounts.length != 0) {
            Sdk.getAccountsDataByHash(
                tvm.functionId(onDataResult),
                m_codeHash,
                accounts[accounts.length - 1].id
            );
        } else {
            m_codeHash = 0;
            Terminal.print(0, format("{} contracts.", m_count));
        }
    }

    function mi_participateInAuction() public {
        Terminal.inputStr(tvm.functionId(getAucForName), "Enter name which you'd like to buy:", false);
    }

    function getAucForName(string value) public {
        IDensRoot(root).auction{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(processAuc),
                onErrorId: 0
            }(value);
    }

    function processAuc(address value0) public {
        currAucAddr = value;
        Sdk.getAccountType(tvm.functionId(checkAucOpen), value);
    }

    function checkAucOpen(int8 acc_type) public {
        if (acc_type == -1)  {
            Terminal.print(0, "Auction does not exist check whether you can register this name.");
            start();
        }
        if (acc_type == 0) {
            Terminal.print(0, "Auction exists, proceeding..");
            AddressInput.get(tvm.functionId(userAddress4BidSpecified), "Please select wallet address you want to use:");
        }
    }

    function userAddress4BidSpecified(address value) public {
        bidderPaymentAddress = value;
        AmountInput.get(tvm.functionId(amount4BidSpecified), "Please enter desired amount for the bid:", 9, 1, 1e13);
    }

    function amount4BidSpecified(uint128 value) public {
        bidAmount = value;
        nonce = rnd.next();
        sendBid(generateHash(bidderPaymentAddress, bidAmount, nonce));
    }

    function sendBid(uint256 value) public {
        IDensAuction(currAucAddr).bid{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: tvm.functionId(onSuccessBid),
                onErrorId: 0
            }(value);
    }

    function onSuccessBid(bool value) public {
        if (value) {
            IDensAuction(currAucAddr).findBid{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: computeBidLoad,
                onErrorId: 0
            }(0, address(this));
        } else {
            Terminal.print(0, "Placing a bid was unsuccessfull");
        }
    }

    function computeBidLoad(address value0) public {
        densBidAddr = value;
        Sdk.chacha20(tvm.functionId(placingSecret2Bid), bytes(bidAmount), bytes(nonce), tvm.pubkey());
    }

    function placingSecret2Bid(bytes value) public {
        IDensBid(densBidAddr).put{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: computeBidLoad,
                onErrorId: 0
            }(value);
        start();
    }

    function mi_revealBid() public {
        Terminal.inputStr(tvm.functionId(getAucName), "Enter name of auction:", false);
    }

    function getAucName(string value) public {
        currAucAddr = value;
        IDensAuction(currAucAddr).findBid{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: revealBid,
                onErrorId: 0
            }(0, address(this));
    }

    function revealBid(address value0) public {
        //IDensBid(value0).reveal
    }

    function mi_finalizeAuction() public {
        Terminal.inputStr(tvm.functionId(finalizeAuction), "Enter name of auction:", false);
    }

    function finalizeAuction(string value) public {
        currAucAddr = value;
        IDensAuction(currAucAddr).finalize{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: finalizeResult,
                onErrorId: 0
            }(0, address(this));
    }

    function finalizeResult(bool value0) public {
        if (value0) {
            Terminal.print(0, "Successfully finalized");
            getAucWithdrawName(currAucAddr);
        } else {
            Terminal.print(0, "Failed to finalize");
            start();
        }
    }

    function mi_withdrawBid() public {
        Terminal.inputStr(tvm.functionId(getAucWithdrawName), "Enter name of auction:", false);
    }

    function getAucWithdrawName(string value) public {
        currAucAddr = value;
        IDensAuction(currAucAddr).findBid{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: withdrawBid,
                onErrorId: 0
            }(0, address(this));
    }

    function withdrawBid(address value0) public {
        IDensBid(value0).withdraw{
                abiVer: 2,
                extMsg: true,
                sign: false,
                pubkey: pubkey,
                time: 0,
                expire: 0,
                callbackId: 0,
                onErrorId: 0
            }()
        start();
    }
}