pragma ton-solidity >=0.45.0;

import "../structures/SmvStructures.sol";

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// SMV Specific

interface IClient {
    function onProposalPassed(ProposalInfo proposalInfo) external;
    function onProposalRejected(ProposalInfo proposalInfo) external;
    function onProposalDeploy(address addr, ProposalType proposalType, TvmCell specific) external;
}
