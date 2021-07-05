pragma ton-solidity >=0.45.0;

interface IUpgradable {

    function upgrade(TvmCell code, uint32 revision) external;
    function upgradeNotNeeded() external;

}