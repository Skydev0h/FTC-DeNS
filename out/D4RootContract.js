const D4RootContract = {
    abi: {
        "ABI version": 2,
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
                        "type": "bytes"
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
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChown",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
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
                        "type": "bytes"
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
                                "type": "bytes"
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
                                "type": "bytes"
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
                        "name": "_answer_id",
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
                        "name": "_answer_id",
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
                        "name": "_answer_id",
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
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
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
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "ct_type",
                        "type": "uint8"
                    },
                    {
                        "name": "fullname",
                        "type": "bytes"
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
                        "name": "_answer_id",
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
                        "type": "bytes"
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
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "type": "bytes"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    },
                    {
                        "name": "subname",
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "name": "_answer_id",
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
                        "name": "_answer_id",
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
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "adminChowned",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
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
                        "type": "bytes"
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
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "smvReserveCommit",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
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
                        "type": "bytes"
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
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "6fe3c8e009dbcc54d6a71fd8501fa64fc64c436118114f6d43d87acbbd285602",
};
module.exports = { D4RootContract };