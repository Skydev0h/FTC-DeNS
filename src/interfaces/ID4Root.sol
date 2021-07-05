pragma ton-solidity >=0.45.0;

import "./ISafeOwner.sol";
import "./IClient.sol";

interface ID4Root is ISafeOwner, IClient {

    function deployUserForMe()
        external responsible
        returns (address user_addr);

    function deployUserForPubKey(uint256 pubkey)
        external responsible
        returns (address user_addr);

    function resolveUser(address user)
        external responsible view
        returns (address user_addr);

    function createAuction(address origin, uint32 revision, string name, uint8 duration)
        external responsible
        returns (address auction);

    function resolveAuction(string name)
        external view responsible
        returns (address auct_addr);

    function resolve(uint8 ct_type, string name, address parent)
        external responsible view
        returns (address res);

    function resolveFull(uint8 ct_type, string fullname)
        external responsible view
        returns (address res);

    function setBaseCode(TvmCell code) external;

    function setCertificateCode(TvmCell code) external;

    function setAuctionCode(TvmCell code) external;

    function setUserCode(TvmCell code) external;

    function setRootCode(TvmCell code) external;

    function assignSmvContract(address smv_addr) external;

    function restrictAuctions(uint32 until) external;

    function withdraw(address dest, uint128 value)
        external pure;

    function withdrawable()
        external pure
        returns (uint128 avail);

    function upgradeMeRequest(uint8 ct_type, uint32 my_revision, uint256 my_hash) external;

    function receiveShards(uint8 ct_type, string name, address parent) external;

    function onAuctionResult(address winner, uint32 exp, string name, address parent, bool deploy) external;

    function subCertDepl(string name, address parent, string subname, address new_owner, uint32 expiry) external;

    function dropAdminFlag(uint8 flags) external;
    function adminDeploy(string name, address set_owner, uint32 set_expiry) external view;
    function adminReserve(string name) external view;
    function adminChown(string name, address set_owner) external view;
    function adminChexp(string name, uint32 set_expiry) external view;
    function adminUpgradeUser(address target) external view;
    function adminUpgradeCert(address target) external view;

}