pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4Test {

    address public addr;

    constructor() public {
        tvm.accept();
    }

    function makeIntUser(address root) public pure {
        tvm.accept();
        ID4Root(root).deployUserForMe{value: Sys.MinimalUserRegister,
            flag: Flags.addFees, callback: D4Test.addressCallback}();
    }

    function addressCallback(address user_addr) public {
        tvm.accept();
        addr = user_addr;
    }

    function makeExtUser(address root, uint256 pk) public pure {
        tvm.accept();
        ID4Root(root).deployUserForPubKey{value: Sys.MinimalUserRegister,
            flag: Flags.addFees, callback: D4Test.addressCallback}(pk);
    }

}