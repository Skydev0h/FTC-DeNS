pragma ton-solidity >=0.45.0;

struct AuctInfo {

    uint32 id;
    uint32 sync;

    string name;
    address parent;

    uint8 durationYears;
    uint32 startTime;
    uint32 bidEnds;
    uint32 revEnds;
    uint32 finalizeAfter;
    uint32 expiryTarget;

}