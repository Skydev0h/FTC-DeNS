pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4Test is ID4User {

    address public _root;
    address public iaddr;
    address public eaddr;
    ID4User usr;

    modifier a() {
        tvm.accept();
        _;
    }

    constructor(address root) public {
        tvm.accept();
        _root = root;
    }

    function makeIntUser() public view a {
        require(iaddr == address(0));
        ID4Root(_root).deployUserForMe{value: Sys.MinimalUserRegister,
            flag: Flags.addFees, callback: D4Test.addressCallbackInt}();
    }

    function makeExtUser(uint256 pk) public view a {
        require(eaddr == address(0));
        ID4Root(_root).deployUserForPubKey{value: Sys.MinimalUserRegister,
            flag: Flags.addFees, callback: D4Test.addressCallbackExt}(pk);
    }

    function addressCallbackInt(address user_addr) public a {
        iaddr = user_addr;
        usr = ID4User(iaddr);
    }

    function addressCallbackExt(address user_addr) public a {
        eaddr = user_addr;
    }

    function addLocked(uint32 until, string name, address parent) external a override {}

    function requestUpgrade() external view a override { usr.requestUpgrade(); }

    function sweepLocks() external a override { usr.sweepLocks(); }

    function withdraw(address dest, uint128 value) external a override { usr.withdraw(dest, value); }

    function pull(uint128 value) external view a {
        usr.withdraw(address(this), value);
    }

    function withdrawable() external view override returns (uint128 avail) { return 0; }

    function setMasterKey(bytes newMasterKey) external a override { usr.setMasterKey(newMasterKey); }

    function createAuction(string name, uint8 duration) external view a override {
        usr.createAuction{value: Sys.MinimalRegNameRequest, flag: 1}(name, duration);
    }

    function makeBid(address auction, bytes data, uint256 hash) external a override {
        usr.makeBid{value: Sys.MinimumMakeBid, flag: 1}(auction, data, hash);
    }

    function revealBid(address auction, uint128 amount, uint128 nonce) external a override {
        usr.revealBid{value: amount + Sys.AddToReveal, flag: 1}(auction, amount, nonce);
    }

    function bidRevealComplete() external a override { }

    function finalize(address auction) external a override {
        usr.finalize(auction);
    }

    function queryCert(address target) external view a override { usr.queryCert(target); }
    function queryAuct(address target) external view a override { usr.queryAuct(target); }
    function forgetCert(address target) external a override { usr.forgetCert(target); }
    function forgetAuct(address target) external a override { usr.forgetAuct(target); }
    function forgetMe(string name, address parent) external a override {}

    function setValue(address target, int16 index, address new_value) external view a override { usr.setValue(target, index, new_value); }
    function resetValue(address target, int16 index) external view a override { usr.resetValue(target, index); }
    function clearValues(address target) external view a override { usr.clearValues(target); }
    function certWithdrawExcess(address target, uint128 amount) external view a override { usr.certWithdrawExcess(target, amount); }
    function certRequestUpgrade(address target) external view a override { usr.certRequestUpgrade(target); }
    function requestProlong(address target) external view a override { usr.requestProlong(target); }
    function deploySub(address target, string name) external view a override { usr.deploySub(target, name); }
    function syncSub(address target, string name) external view a override { usr.syncSub(target, name); }

    function queryCertCallback(CertInfo info) external a override { }
    function queryAuctCallback(AuctInfo info) external a override { }

    function certTransferOwner(address target, address new_owner, uint32 deadline) external view a override { usr.certTransferOwner(target, new_owner, deadline); }
    function certCancelTransferOwner(address target) external view a override { usr.certCancelTransferOwner(target); }
    function certAcceptTransfer(address target) external view a override { usr.certAcceptTransfer(target); }
    function certRelinquishOwner(address target) external view a override { usr.certRelinquishOwner(target); }

    function passToOwner() external a override { }

    function upgrade(TvmCell code, uint32 revision) external a override { }

    function upgradeNotNeeded() external a override { }

    function hasBid(address) external a override returns (bool res) { return false; }

    function getBid(address) external a override returns (AuctBid res) { return AuctBid(0,'',0); }

}