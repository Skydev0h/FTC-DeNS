pragma ton-solidity >=0.45.0;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

enum ProposalType {
    Undefined,
    SetCode,
    Reserve,
    SetOwner,
    SetRootOwner
}

enum ProposalState {
    Undefined,
    New,
    OnVoting,
    Ended,
    Passed,
    NotPassed,
    Finalized,
    Distributed,
    Reserved,
    Last
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

struct ProposalInfo {
    uint32 start;               // Start of the voting
    uint32 end;                 // Timestamp of the voting end
    string title;               // Proposal title
    ProposalType proposalType;  // Proposal type
    TvmCell specific;           // Proposal specific data
    ProposalState state;
    uint32 votesFor;
    uint32 votesAgainst;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 1 SetCode

struct SetCodeProposalSpecific {
    uint8 ContractType;
    TvmCell code;
}

//----------------------------------------------------------------------------------------------------------------//
// 2 Reserve

struct ReserveProposalSpecific {
    string name;
    uint32 ts;
}

//----------------------------------------------------------------------------------------------------------------//
// 3 SetOwner

struct SetOwnerProposalSpecific {
    string name;
    address owner;
    uint128 ts;
}

//----------------------------------------------------------------------------------------------------------------//
// 4 SetRootOwner

struct SetRootOwnerProposalSpecific {
    uint256 pubkey;
    string comment;
}

//----------------------------------------------------------------------------------------------------------------//