pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./abstract/D4PureBase.sol";
import "./interfaces/ID4Base.sol";
import "./interfaces/ID4Root.sol";
import "./interfaces/ISink.sol";
import "./libraries/Flags.sol";

contract D4Base is ID4Base, D4PureBase {

//  >  st_root st_type st_name st_parent
//  >  base_code m_version m_revision
//  <  onlyRoot onlyParent

    constructor(TvmCell code, uint32 revision, TvmCell param)
        public
        onlyRoot
    {
//        if (revision == 0) {
//            // Existential check
//            msg.sender.transfer({
//                value:   0,
//                bounce:  false,
//                flag:    Flags.sendAllThenDestroy
//            });
//        }
//        require(msg.sender == st_root, Errors.senderIsNotRoot);
        tvm.accept();
        base_code = tvm.code();
        m_version = 0;
        m_revision = revision;
        tvm.setcode(code);
        tvm.setCurrentCode(code);
        TvmBuilder b = packBase();
        onCodeUpgrade(param, b.toCell());
    }

    function onCodeUpgrade(TvmCell, TvmCell)
        internal pure
    {
        revert(Errors.methodIsNotCallable);
    }

    function registrationPreflight(uint128 requestId)
        external view responsible override
        onlyRoot
        returns (uint128 requestId_, uint32 expiry_)
    {
        return {
            value:   0,
            bounce:  true,
            flag:    Flags.messageValue
        } (requestId, 0);
    }

    function destroy()
        external view override
        // onlyRoot // anyone can destroy incomplete instance
    {
        ID4Root(st_root).receiveShards{
             value:  0,
            bounce:  false,
              flag:  Flags.sendAllThenDestroy
        }(st_type, st_name, st_parent);
    }

}
