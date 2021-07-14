pragma ton-solidity >=0.45.0;
pragma AbiHeader time;
pragma AbiHeader pubkey;
pragma AbiHeader expire;

import "./Imports.sol";

contract D4MFT128 {

    constructor() public {
        tvm.accept();
    }

    function sendMessage(address dest, uint128 value, uint16 flag, string message) private pure {
        TvmBuilder b;
        b.store(uint32(0));
        // TvmBuilder s;
        b.store(message);
        // b.store(s.toCell());
        dest.transfer({value: value, bounce: false, flag: flag, body: b.toCell()});
    }

    receive() external view {
        require(msg.value >= 2 ton);
        tvm.rawReserve(address(this).balance - msg.value, 0);
        sendMessage(msg.sender, 1 ton, 0, "Flag 0 + 1 ton");
        sendMessage(msg.sender, 0, 128, "Attempt remaining");
    }

}