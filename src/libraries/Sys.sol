pragma ton-solidity >=0.45.0;

library Sys {

    int8 constant ExternalMetaChain = -99;

    uint32 constant RelinquishOwnerTimeout = 300;

    uint128 constant MinimalRootBalance = 10 ton;
    uint128 constant MinimalCertBalance = 1 ton;
    uint128 constant MinimalUserBalance = 1 ton;

    uint128 constant InitialBaseBalance = 1 ton;

    uint128 constant MinimalRegNameRequest = 5 ton;
    uint128 constant MinimalUserRegister = 5 ton;

    uint128 constant CallValue = 0.1 ton;

    uint32 constant ExpiringAuctionPermit = 28 days;

    uint32 constant ReserveSafetyTimeout  = 30 days;

    uint32 constant MaxTimingYearsPeriod = 4;

    uint32 constant BidPeriodPerYear    = 7 days;
    uint32 constant RevealPeriodPerYear = 1 days;

    uint8 constant MaxDurationValue = 100;

    uint32 constant ReAuctionGrace = 2 days;
    uint32 constant ProlongGrace   = 1 days;

    uint32 constant MinimumMakeBid     = 1 ton;
    uint32 constant MinumumPossibleBid = 1 ton;
    uint32 constant AddToReveal        = 1 ton;
    uint32 constant AddToProlong       = 1 ton;

    uint128 constant ProlongMultiplier = 2;
    uint128 constant ProlongDivisor    = 1;

    uint32 constant MaxU32             = 0xFFFFFFFF;

    address constant a0 = address(0);

    uint16 constant IsContructorCall = 0;

    uint8 constant ReserveDuration    = 255;
    uint8 constant ReserveNOWDuration = 251;

}