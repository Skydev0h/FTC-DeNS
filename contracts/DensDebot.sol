pragma ton-solidity ^0.38.0;
pragma AbiHeader expire;
pragma AbiHeader time;
pragma AbiHeader pubkey;

import "ui/Debot.sol";
import "ui/Terminal.sol";

contract DensDebot is Debot {

    /// @notice Entry point function for DeBot.
    function start() public override {
        // print string to user.
        Terminal.print(0, "Hello, World!");
        // input string from user and define callback that receives entered string.
        Terminal.input(tvm.functionId(setUserInput), "How is it going?", false);
    }

    function setUserInput(string value) public {
        // TODO: continue DeBot logic here...
        Terminal.print(0, format("You entered \"{}\"", value));
    }

    function getVersion() public override returns (string name, uint24 semver) {
        (name, semver) = ("DeNS Debot", _version(0,1,0));
    }

    function _version(uint24 major, uint24 minor, uint24 fix) private pure inline returns (uint24) {
        return (major << 16) | (minor << 8) | (fix);
    }

}