pragma ton-solidity >=0.45.0;

interface ISafeOwner {

    function getOwner()
        external view responsible
        returns (address owner_);

    function getPendingOwner()
        external view responsible
        returns (address pending_owner_);

    function transferOwner(address new_owner, uint32 deadline) external;

    function cancelTransferOwner() external;

    function acceptTransfer() external;

    function relinquishOwner() external;

}