pragma ton-solidity >=0.45.0;

import "./IRegPre.sol";
import "./ISafeOwner.sol";
import "./IUpgradable.sol";
import "./IPasser.sol";

import "../structures/CertInfo.sol";

interface ID4Cert is ISafeOwner, IUpgradable, IRegPre, IPasser {

    function getValue(int16 index)
        external view responsible
        returns(address);

    function setValue(int16 index, address new_value) external;

    function resetValue(int16 index) external;

    function clearValues() external;

    function withdrawExcess(address dest, uint128 amount)
        external pure;

    function requestUpgrade() external view;

    function requestProlong()
        external view;

    function applyAuctionResult(address new_owner, uint32 new_expiry)
        external responsible
        returns (bool success);

    function ensureExpiry(uint32 expiry, bool retval) external;

    function deploySub(string name) external;

    function syncSub(string name) external;

    function subSynchronize(address new_owner, uint32 new_expiry) external;

    function getInfo()
        external responsible view
        returns (CertInfo info);

}