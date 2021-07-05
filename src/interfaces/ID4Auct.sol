pragma ton-solidity >=0.45.0;

import "../structures/AuctInfo.sol";

interface ID4Auct {

    function registrationPreflightCallback(uint128 requestId_, uint32 expiry_) external;

    function accountBid(address user) external;

    function revealBid(address user, uint32 bid_time, uint128 amount, uint128 nonce, uint256 prover) external;

    // function configure(address user, uint8 duration) external;

    function requiredAmountForProlong()
        external view responsible
        returns (uint128 amount);

    function prolong() external;

    function commit(bool result) external view;

    function finalize(address user) external view;

    function getInfo()
        external responsible view
        returns (AuctInfo info);

}