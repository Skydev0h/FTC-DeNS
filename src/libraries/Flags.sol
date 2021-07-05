pragma ton-solidity >=0.45.0;

library Flags {

    // Short
    uint8 constant addTxFees = 1;
    uint8 constant addFees   = 1;
    uint8 constant ignoreErr = 2;
    uint8 constant destrIf0  = 32;
    uint8 constant msgVal    = 64;
    uint8 constant incVal    = 64;
    uint8 constant allBal    = 128;
    uint8 constant ctrBal    = 128;
    uint8 constant selfDestr = 128 + 32;

    // Long
    uint8 constant addTransactionFees   = 1;
    uint8 constant ignoreErrors         = 2;
    uint8 constant destroyIfZeroBalance = 32;
    uint8 constant messageValue         = 64;
    uint8 constant addMessageValue      = 64;
    uint8 constant addIncomingValue     = 64;
    uint8 constant allBalance           = 128;
    uint8 constant contractBalance      = 128;
    uint8 constant addAllBalance        = 128;
    uint8 constant addContractBalance   = 128;
    uint8 constant selfDestruct         = 128 + 32;
    uint8 constant sendAllThenDestroy   = 128 + 32;

}