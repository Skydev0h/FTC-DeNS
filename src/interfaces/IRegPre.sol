pragma ton-solidity >=0.45.0;

interface IRegPre {

    function registrationPreflight(uint128 requestId)
        external view responsible
        returns (uint128 requestId_, uint32 expiry_);

}