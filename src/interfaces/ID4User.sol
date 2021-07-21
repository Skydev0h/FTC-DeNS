pragma ton-solidity >=0.45.0;

import "./IUpgradable.sol";
import "./IPasser.sol";
import "../structures/AuctInfo.sol";
import "../structures/CertInfo.sol";

interface ID4User is IUpgradable, IPasser {

    function addLocked(uint32 until, string name, address parent) external;

    function requestUpgrade() external view;

    function sweepLocks() external;

    function withdraw(address dest, uint128 value) external;

    function withdrawable()
        external view
        returns (uint128 avail);

    function setMasterKey(bytes newMasterKey) external;

    function createAuction(string name, uint8 duration) external view;

    function makeBid(address auction, bytes data, uint256 hash) external;

    function revealBid(address auction, uint128 amount, uint128 nonce) external;

    function bidRevealComplete() external;

    function finalize(address auction) external;

    function queryCert(address target) external view;
    function queryAuct(address target) external view;
    function forgetCert(address target) external;
    function forgetAuct(address target) external;
    function forgetMe(string name, address parent) external;

    function setValue(address target, int16 index, address new_value) external view;
    function resetValue(address target, int16 index) external view;
    function clearValues(address target) external view;
    function certWithdrawExcess(address target, uint128 amount) external view;
    function certRequestUpgrade(address target) external view;
    function requestProlong(address target) external view;
    function deploySub(address target, string name) external view;
    function syncSub(address target, string name) external view;

    function queryCertCallback(CertInfo info) external;
    function queryAuctCallback(AuctInfo info) external;

    function certTransferOwner(address target, address new_owner, uint32 deadline) external view;
    function certCancelTransferOwner(address target) external view;
    function certAcceptTransfer(address target) external view;
    function certRelinquishOwner(address target) external view;

}