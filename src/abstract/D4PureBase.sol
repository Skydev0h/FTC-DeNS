pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "../libraries/Errors.sol";

abstract contract D4PureBase {

    address public static st_root;
    uint8   public static st_type;
    string  public static st_name;
    address public static st_parent;

    TvmCell public base_code;

    uint16  public m_version;
    uint32  public m_revision;

    modifier onlyRoot {
        require(msg.sender == st_root, Errors.senderIsNotRoot);
        _;
    }

    modifier onlyParent {
        require(msg.sender == st_parent, Errors.senderIsNotParent);
        _;
    }

    function packBase()
        internal view
        returns (TvmBuilder)
    {
        TvmBuilder b;
        b.store(st_root, st_type, st_name, st_parent, base_code, m_version, m_revision);
        return b;
    }

    function unpackBase(TvmSlice s)
        internal
    {
        (st_root, st_type, st_name, st_parent, base_code, m_version, m_revision) =
            s.decode(address, uint8, string, address, TvmCell, uint16, uint32);
    }

}