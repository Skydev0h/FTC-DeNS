pragma ton-solidity >=0.45.0;

library Errors {

    uint8 constant initialOwnerMissing       =  111;
    uint8 constant onlyOwnerAccepted         =  112;
    uint8 constant onlySmvRootAccepted       =  113;
    uint8 constant onlyPendingOwnerAccepted  =  114;

    uint8 constant ownerTransferMissDeadline =  121;
    uint8 constant adminFlagDisabled         =  122;
    uint8 constant cantForgetActiveBid       =  123;

    uint8 constant remainingBalanceTooLow    =  131;
    uint8 constant messageValueTooLow        =  132;
    uint8 constant bidWasMadeTooEarly        =  133;
    uint8 constant bidWasMadeTooLate         =  134;
    uint8 constant bidProofInvalid           =  135;
    uint8 constant invalidTimePhase          =  136;
    uint8 constant alreadyInitialized        =  137;
    uint8 constant auctionsAreRestricted     =  138;
    uint8 constant contractCodeNotInstalled  =  139;

    uint8 constant directDeployForbidden     =  141;
    uint8 constant directReceiveForbidden    =  142;
    uint8 constant fallbackForbidden         =  143;
    uint8 constant contractNotFragile        =  144;
    uint8 constant contractIsFragile         =  145;
    uint8 constant contractNotReady          =  146;

    uint8 constant methodIsNotCallable       =  150;
    uint8 constant senderIsNotRoot           =  151;
    uint8 constant senderIsNotParent         =  152;
    uint8 constant interactionWrongSender    =  153;
    uint8 constant interactionOutdated       =  154;

    uint8 constant invalidArgument           =  161;
    uint8 constant internalMessageOnly       =  162;
    uint8 constant externalMessageOnly       =  163;

    uint8 constant baseCannotBeChanged       =  171;

}