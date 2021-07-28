pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "Imports.sol";
import "../Imports.sol";

interface IDeNSDebotHelper {
    function isD4Userdeployed() external view returns (bool result);
    function createD4User() external;
    function getD4User() external view returns (address result);
    function createAuction(string name, uint8 duration) external pure;
    function resolveAuction(string name) external view;
    function getAucAddress() external view returns (address result);
    function setPubkey(uint256 value) external;
    function resolveCert(string name) external view;
    function getCertAddress() external view returns (address result);
    function makeBid(address b_auction, bytes b_data, uint256 b_hash) external pure;
    function revealBid(address auction, uint128 amount, uint128 nonce) external view;
}

contract DeNSDebotHelper {
    address userMsigWallet;
    bool d4UserDeployed;
    address d4User;
    address root;
    address auction;
    address certificate;
    uint256 pubkey;

    constructor(address _wallet, address _root) public {
        d4UserDeployed = false;
        userMsigWallet = _wallet;
        root = _root;
        ID4Root(root).resolveUser{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(resolveUserCallback),
            onErrorId: 0
        }(address(this));
    }

    function setPubkey(uint256 value) external {
        pubkey = value;
    }

    function resolveUserCallback(address user_addr) public {
        d4User = user_addr;
        Sdk.getAccountType(tvm.functionId(checkStatus), user_addr);
    }

    function checkStatus(int8 acc_type) public {
        if (acc_type == -1 || acc_type == 0 || acc_type == 2)  {
            d4UserDeployed = false;
        } else {
            d4UserDeployed = true;
        }
    }

    function createD4User() external pure {
        tvm.accept();
        TvmCell payload = tvm.encodeBody(ID4Root.deployUserForMe, deployUserCallback);
        root.transfer(Sys.MinimalUserRegister, true, 1, payload);
    }

    function deployUserCallback(address user_addr) public {
        d4User = user_addr;
        d4UserDeployed = true;
    }

    function isD4Userdeployed() external view returns (bool) {
        return d4UserDeployed;
    }

    function getD4User() external view returns (address result) {
        return d4User;
    }

    function createAuction(string name, uint8 duration) external pure {
        tvm.accept();
        TvmCell payload = tvm.encodeBody(ID4User.createAuction, name, duration);
        d4User.transfer(Sys.MinimalRegNameRequest, true, 1, payload);
    }

    function resolveAuction(string name) external view {
        ID4Root(root).resolveAuction{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(resolveAuctionCallback),
            onErrorId: 0
        }(name);
    }

    function resolveAuctionCallback(address auct_addr) public view {
        auction == auct_addr;
    }

    function getAucAddress() external view returns (address result) {
        return auction;
    }

    function resolveCert(string name) external view {
        ID4Root(root).resolve{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: pubkey,
            time: 0,
            expire: 0,
            callbackId: tvm.functionId(resolveCertificateCallback),
            onErrorId: 0
        }(1, name, root);
    }

    function resolveCertificateCallback(address res) public view {
        certificate == res;
    }

    function getCertAddress() external view returns (address result) {
        return certificate;
    }

    function makeBid(address b_auction, bytes b_data, uint256 b_hash) external pure {
        tvm.accept();
        TvmCell payload = tvm.encodeBody(ID4User.makeBid, b_auction, b_data, b_hash);
        d4User.transfer(msg.value, true, 1, payload);
    }

    function revealBid(address b_auction, uint128 b_amount, uint128 b_nonce) external view {
        ID4User(d4User).revealBid{
            abiVer: 2,
            extMsg: true,
            sign: false,
            pubkey: pubkey,
            time: 0,
            expire: 0,
            callbackId: 0,
            onErrorId: 0
            }( b_auction, b_amount, b_nonce);
    }

}