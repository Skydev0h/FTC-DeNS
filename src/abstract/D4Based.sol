pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "../interfaces/ISink.sol";
import "../libraries/Errors.sol";
import "../libraries/Flags.sol";
import "./D4PureBase.sol";
import "../D4Base.sol";

abstract contract D4Based is D4PureBase, ISink {

    constructor()
        virtual public
    {
        revert(Errors.directDeployForbidden);
    }

    fallback()
        virtual external pure
    {
        revert(Errors.fallbackForbidden);
    }

    function sink()
        external override pure
    {

    }

    function _resolveContract(uint8 ct_type, string name, address parent)
        internal view
        returns (address)
    {
        TvmCell stateInit = tvm.buildStateInit({
            contr: D4Base,
            code: base_code,
            varInit: {
                st_root: st_root,
                st_type: ct_type,
                st_name: name,
                st_parent: parent
            }
        });
        return address(tvm.hash(stateInit));
    }

    function verifyInteraction(uint8 ct_type, string name, address parent)
        internal view
    {
        require(msg.sender == _resolveContract(ct_type, name, parent),
            Errors.interactionWrongSender);
    }

    modifier returnRemainder()
    {
        _;
        msg.sender.transfer({value: 0, bounce: false, flag: Flags.messageValue});
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Now() for integration testing

    function Now()
        pure virtual internal inline
        returns (uint32)
    {
        return now;
    }

}