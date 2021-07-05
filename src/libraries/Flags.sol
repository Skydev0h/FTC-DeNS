pragma ton-solidity >=0.45.0;

library Msg {
    uint8 constant addTxFees = 1;
    uint8 constant addFees   = 1;
    uint8 constant ignoreErr = 2;
    uint8 constant destrIf0  = 32;
    uint8 constant msgBal    = 64;
    uint8 constant incBal    = 64;
    uint8 constant allBal    = 128;
    uint8 constant ctrBal    = 128;
    uint8 constant selfDestr = 128 + 32;
}