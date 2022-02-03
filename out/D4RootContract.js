const D4RootContract = {
    abi: {
        "ABI version": 2,
        "version": "2.2",
        "header": [
            "pubkey",
            "time",
            "expire"
        ],
        "functions": [
            {
                "name": "constructor",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "dropAdminFlag",
                "inputs": [
                    {
                        "name": "flags",
                        "type": "uint8"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminDeploy",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_owner",
                        "type": "address"
                    },
                    {
                        "name": "set_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminReserve",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChown",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_owner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChexp",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminUpgradeUser",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminUpgradeCert",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "onProposalPassed",
                "inputs": [
                    {
                        "components": [
                            {
                                "name": "start",
                                "type": "uint32"
                            },
                            {
                                "name": "end",
                                "type": "uint32"
                            },
                            {
                                "name": "title",
                                "type": "string"
                            },
                            {
                                "name": "proposalType",
                                "type": "uint8"
                            },
                            {
                                "name": "specific",
                                "type": "cell"
                            },
                            {
                                "name": "state",
                                "type": "uint8"
                            },
                            {
                                "name": "votesFor",
                                "type": "uint32"
                            },
                            {
                                "name": "votesAgainst",
                                "type": "uint32"
                            }
                        ],
                        "name": "proposalInfo",
                        "type": "tuple"
                    }
                ],
                "outputs": []
            },
            {
                "name": "onProposalRejected",
                "inputs": [
                    {
                        "components": [
                            {
                                "name": "start",
                                "type": "uint32"
                            },
                            {
                                "name": "end",
                                "type": "uint32"
                            },
                            {
                                "name": "title",
                                "type": "string"
                            },
                            {
                                "name": "proposalType",
                                "type": "uint8"
                            },
                            {
                                "name": "specific",
                                "type": "cell"
                            },
                            {
                                "name": "state",
                                "type": "uint8"
                            },
                            {
                                "name": "votesFor",
                                "type": "uint32"
                            },
                            {
                                "name": "votesAgainst",
                                "type": "uint32"
                            }
                        ],
                        "name": "proposalInfo",
                        "type": "tuple"
                    }
                ],
                "outputs": []
            },
            {
                "name": "onProposalDeploy",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    },
                    {
                        "name": "proposalType",
                        "type": "uint8"
                    },
                    {
                        "name": "specific",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "deployUserForMe",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "deployUserForPubKey",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "pubkey",
                        "type": "uint256"
                    }
                ],
                "outputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolveUser",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "user",
                        "type": "address"
                    }
                ],
                "outputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolve",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ],
                "outputs": [
                    {
                        "name": "res",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolveFull",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "fullname",
                        "type": "string"
                    }
                ],
                "outputs": [
                    {
                        "name": "res",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "createAuction",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "origin",
                        "type": "address"
                    },
                    {
                        "name": "revision",
                        "type": "uint32"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "duration",
                        "type": "uint8"
                    }
                ],
                "outputs": [
                    {
                        "name": "auction",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolveAuction",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    }
                ],
                "outputs": [
                    {
                        "name": "auct_addr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "onAuctionResult",
                "inputs": [
                    {
                        "name": "winner",
                        "type": "address"
                    },
                    {
                        "name": "exp",
                        "type": "uint32"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    },
                    {
                        "name": "deploy",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "applyAuctionCallback",
                "inputs": [
                    {
                        "name": "success",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subCertDepl",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    },
                    {
                        "name": "subname",
                        "type": "string"
                    },
                    {
                        "name": "new_owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "receiveShards",
                "inputs": [
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setBaseCode",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setCertificateCode",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setAuctionCode",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setUserCode",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setRootCode",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "upgradeMeRequest",
                "inputs": [
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "my_revision",
                        "type": "uint32"
                    },
                    {
                        "name": "my_hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "assignSmvContract",
                "inputs": [
                    {
                        "name": "smv_addr",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "restrictAuctions",
                "inputs": [
                    {
                        "name": "until",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getOwner",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "owner_",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "getPendingOwner",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "pending_owner_",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "transferOwner",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    },
                    {
                        "name": "deadline",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "cancelTransferOwner",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "acceptTransfer",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "relinquishOwner",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "withdrawable",
                "inputs": [],
                "outputs": [
                    {
                        "name": "avail",
                        "type": "uint128"
                    }
                ]
            },
            {
                "name": "withdraw",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
                    {
                        "name": "value",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "m_version",
                "inputs": [],
                "outputs": [
                    {
                        "name": "m_version",
                        "type": "uint16"
                    }
                ]
            },
            {
                "name": "base_code",
                "inputs": [],
                "outputs": [
                    {
                        "name": "base_code",
                        "type": "cell"
                    }
                ]
            },
            {
                "name": "certificate_code",
                "inputs": [],
                "outputs": [
                    {
                        "name": "certificate_code",
                        "type": "cell"
                    }
                ]
            },
            {
                "name": "auction_code",
                "inputs": [],
                "outputs": [
                    {
                        "name": "auction_code",
                        "type": "cell"
                    }
                ]
            },
            {
                "name": "user_code",
                "inputs": [],
                "outputs": [
                    {
                        "name": "user_code",
                        "type": "cell"
                    }
                ]
            },
            {
                "name": "base_revision",
                "inputs": [],
                "outputs": [
                    {
                        "name": "base_revision",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "certificate_revision",
                "inputs": [],
                "outputs": [
                    {
                        "name": "certificate_revision",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "auction_revision",
                "inputs": [],
                "outputs": [
                    {
                        "name": "auction_revision",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "user_revision",
                "inputs": [],
                "outputs": [
                    {
                        "name": "user_revision",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "owner",
                "inputs": [],
                "outputs": [
                    {
                        "name": "owner",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "pending_owner",
                "inputs": [],
                "outputs": [
                    {
                        "name": "pending_owner",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "owner_transfer_deadline",
                "inputs": [],
                "outputs": [
                    {
                        "name": "owner_transfer_deadline",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "relinquish_owner_deadline",
                "inputs": [],
                "outputs": [
                    {
                        "name": "relinquish_owner_deadline",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "smv_root",
                "inputs": [],
                "outputs": [
                    {
                        "name": "smv_root",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "no_auctions_until",
                "inputs": [],
                "outputs": [
                    {
                        "name": "no_auctions_until",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "admin_enabled",
                "inputs": [],
                "outputs": [
                    {
                        "name": "admin_enabled",
                        "type": "uint8"
                    }
                ]
            }
        ],
        "data": [],
        "events": [
            {
                "name": "codeUpdated",
                "inputs": [
                    {
                        "name": "codeType",
                        "type": "uint8"
                    },
                    {
                        "name": "codeHash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subUpgraded",
                "inputs": [
                    {
                        "name": "codeType",
                        "type": "uint8"
                    },
                    {
                        "name": "subContract",
                        "type": "address"
                    },
                    {
                        "name": "from",
                        "type": "uint32"
                    },
                    {
                        "name": "to",
                        "type": "uint32"
                    },
                    {
                        "name": "newhash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerTransferStart",
                "inputs": [
                    {
                        "name": "currentOwner",
                        "type": "address"
                    },
                    {
                        "name": "nextOwner",
                        "type": "address"
                    },
                    {
                        "name": "deadline",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerTransferCancelled",
                "inputs": [
                    {
                        "name": "currentOwner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerTransferComplete",
                "inputs": [
                    {
                        "name": "fromOwner",
                        "type": "address"
                    },
                    {
                        "name": "toOwner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerRelinquishStart",
                "inputs": [
                    {
                        "name": "curOwner",
                        "type": "address"
                    },
                    {
                        "name": "deadline",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerRelinquishComplete",
                "inputs": [
                    {
                        "name": "oldOwner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvContractConfigured",
                "inputs": [
                    {
                        "name": "curSMV",
                        "type": "address"
                    },
                    {
                        "name": "newSMV",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "withdrawn",
                "inputs": [
                    {
                        "name": "oldBalance",
                        "type": "uint128"
                    },
                    {
                        "name": "withdrawn",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionsRestricted",
                "inputs": [
                    {
                        "name": "until",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "rootCodeUpgraded",
                "inputs": [
                    {
                        "name": "from",
                        "type": "uint256"
                    },
                    {
                        "name": "to",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "contractShattered",
                "inputs": [
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "ct_addr",
                        "type": "address"
                    },
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionResult",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    },
                    {
                        "name": "winner",
                        "type": "address"
                    },
                    {
                        "name": "deploy",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certReserved",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminFlagDropped",
                "inputs": [
                    {
                        "name": "which",
                        "type": "uint8"
                    },
                    {
                        "name": "remain",
                        "type": "uint8"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminDeployed",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_owner",
                        "type": "address"
                    },
                    {
                        "name": "set_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminReserved",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChowned",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_owner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChexped",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminUpgradedUser",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminUpgradedCert",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvCodeUpgrade",
                "inputs": [
                    {
                        "name": "ct",
                        "type": "uint8"
                    },
                    {
                        "name": "chash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvReserveStart",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvReserveCommit",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "result",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvSetOwner",
                "inputs": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "set_owner",
                        "type": "address"
                    },
                    {
                        "name": "set_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvSetRootOwner",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvSetSmvAddress",
                "inputs": [
                    {
                        "name": "new_smv",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvSetAuctRestrict",
                "inputs": [
                    {
                        "name": "new_until",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvDropAdminFlags",
                "inputs": [
                    {
                        "name": "flags_dropped",
                        "type": "uint8"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvWithdrawn",
                "inputs": [
                    {
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "name": "oldBalance",
                        "type": "uint128"
                    },
                    {
                        "name": "withdrawn",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            }
        ],
        "fields": [
            {
                "name": "_pubkey",
                "type": "uint256"
            },
            {
                "name": "_timestamp",
                "type": "uint64"
            },
            {
                "name": "_constructorFlag",
                "type": "bool"
            },
            {
                "name": "m_version",
                "type": "uint16"
            },
            {
                "name": "base_code",
                "type": "cell"
            },
            {
                "name": "certificate_code",
                "type": "cell"
            },
            {
                "name": "auction_code",
                "type": "cell"
            },
            {
                "name": "user_code",
                "type": "cell"
            },
            {
                "name": "base_revision",
                "type": "uint32"
            },
            {
                "name": "certificate_revision",
                "type": "uint32"
            },
            {
                "name": "auction_revision",
                "type": "uint32"
            },
            {
                "name": "user_revision",
                "type": "uint32"
            },
            {
                "name": "owner",
                "type": "address"
            },
            {
                "name": "pending_owner",
                "type": "address"
            },
            {
                "name": "owner_transfer_deadline",
                "type": "uint32"
            },
            {
                "name": "relinquish_owner_deadline",
                "type": "uint32"
            },
            {
                "name": "smv_root",
                "type": "address"
            },
            {
                "name": "no_auctions_until",
                "type": "uint32"
            },
            {
                "name": "admin_enabled",
                "type": "uint8"
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "6f09c5890056f379111b71395733d2d6e4a5ed531c083e756a3c24c58214c99f",
};
module.exports = { D4RootContract };