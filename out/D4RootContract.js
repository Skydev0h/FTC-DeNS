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
    tvc: "te6ccgECtQEAIzMAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAgaK2zW0BAQkiu1TIOMDIMD/4wIgwP7jAvILsAYFmwTG7UTQ10nDAfhmifhpIds80wABjh2BAgDXGCD5AQHTAAGU0/8DAZMC+ELiIPhl+RDyqJXTAAHyeuLTPwH4QyG58rQg+COBA+iogggbd0CgufK0+GPTHwH4I7zyudMfAds8W9s8ni8IrgR07UTQ10nDAfhmItDTA/pAMPhpqTgA+ER/b3GCCJiWgG9ybW9zcG90+GTcIccA4wIh1w0fjoDfIeMDAa+trwcCCts8W9s8CK4EUCCCEC4rfRa74wIgghBR/SZku+MCIIIQc96bgbvjAiCCEHwUS4S74wJ7SRcJAiggghB5LATku+MCIIIQfBRLhLvjAg4KAiggghB6po4huuMCIIIQfBRLhLrjAgwLAVAw0ds8+FIhjhyNBHAAAAAAAAAAAAAAAAA/BRLhIMjOyx/JcPsA3vIArAMqMPhG8uBM+EJu4wDTB9HbPDDbPPIArA2zAL74U/pCbxLAnY4Y+EUgbpIwcN74U/pCbxPXC/+6aKb7YMD/nPhJ+FPHBWim+2DAAOKw8uBw+AD4WSGEB6KwIPh5AY0EcAAAAAAAAAAAAAAAAAg0i4MgyM7LB8sHyXD7AARQIIIQduu2gLrjAiCCEHcWnpK64wIgghB3dP+IuuMCIIIQeSwE5LrjAhQTEQ8DKjD4RvLgTPhCbuMA0x/R2zww2zzyAKwQswCq+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAIPh4jQRwAAAAAAAAAAAAAAAAGEAvUaDIzssfyXD7AAMmMPhG8uBM+EJu4wDR2zww2zzyAKwSswLC+CP4Vbvy4Hn4VPpCbxLAnY4Y+EUgbpIwcN74VPpCbxPXC/+6aKb7YMD/nPhJ+FTHBWim+2DAAOKw8uBy+AD4VPhTicjOWcjPkWvq3yLOAcjOzc3JcPsA+FT4c3D4dYn4dGieAVAw0ds8+FUhjhyNBHAAAAAAAAAAAAAAAAA9xaekoMjOyx/JcPsA3vIArAOmMPhG8uBM+EJu4wAhjhvTH9Mf1NMHIcIJ8tBJ1NMHIcIJ8tBJ0x/U0dCOGNMf0x/U0wchwgny0EnU0wchwgny0EnTH+LTH1VwbwgB0ds8MNs88gCsFbMBPPhJ+FfHBWim+2DAALDy4HH4ACBvFAFvE8ACjoDeMBYBriDQ1NMfMG8CcHIibxD4KNs8yM+FiM6NBU5iWgAAAAAAAAAAAAAAAAAABQsJVsDPFsoAyXD7AHABbxCNBHAAAAAAAAAAAAAAAAAYGTaiIMjOzMoAyXD7AKEEUCCCEFT13tW74wIgghBfC8/eu+MCIIIQaLVfP7vjAiCCEHPem4G74wI/OC0YBFAgghBqLUBHuuMCIIIQbjF3srrjAiCCEHHJ0zG64wIgghBz3puBuuMCKyocGQT8MPhG8uBM+EJu4wDTH/hEWG91+GQhltMH1NTR0JPTB9Ti+kDR2zwhjh0j0NMB+kAwMcjPhyDOcc8LYQHIz5PPem4Gzs3JcI4x+EQgbxMhbxL4SVUCbxHIcs9AygBzz0DOAfoC9ABxzwtpAcj4RG8Vzwsfzs3J+ERvFOL7AOMArBuoGgAE8gABIPhEcG9ycG9xgEBvdPhk2zyhA+gw+Eby4Ez4Qm7jANMf+ERYb3X4ZNMH1NHbPCGOHSPQ0wH6QDAxyM+HIM5xzwthAcjPk8cnTMbOzclwjjH4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U4vsA4wDyAKwdqANoIIIQ//////lBMDGrAnD4KHCTUwO5joDoMFUSI1UTobX/2zxY2zz4RHBvcnBvcYBAb3T4ZB4hoQMeU0Bx2zz5AIj5ALqOgN6kISAfAiJfJVR0JKG1/9s8I9s8MiCkMyGhAAIvAU4ighD/////+UEwMasCIcD/llMCobT/Mt60/yK0/yKgvvLgRrX/2zwiAkABgH+pDFUC0FiS1THkAacI1yFvAMiTI8MAjoDo2zxsISYjARiWIW+IwACzjoDoyTEkAQwh2zwzzxElABxvjW+NWSBviJJvjJEw4gFEXddJqwIizzWrArYItghUcTCqArUP1xg2Ac4yJKI0I46A3icBIiLXSZQi1TEz3yDPNcEIjoDeKAEG2zzIKQA6ASBviJ9vjSBviIEA/6GUb4xvAN+SbwDiWG+Mb4wBTjDR2zz4VyGOG40EcAAAAAAAAAAAAAAAADuMXeygyM7OyXD7AN7yAKwDTDD4RvLgTPhCbuMAIZTU1NHQkdTi+kDU1NHQ+kDTH9HbPDDbPPIArCyzAnpxVRPbPAHIzssfcVj4SVUCyds8MPhJcMjPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAB0RqDMDPFsmAQPsAUpQEUCCCEGGDCVW64wIgghBiw5YcuuMCIIIQZJhljbrjAiCCEGi1Xz+64wI1MzEuAn4w+EJu4wD4RvJz0fhC8uBv+EUgbpIwcN74Qrry4HD4APhCgJ3Iz4ZAygfL/8nQ+HNw+HiBAP/4eXD4Yts88gAvswIW7UTQ10nCAY6A4w0wrAOAcO1E0PQFcPhA+EH4QvhD+ET4RfhG+Ef4SPhJcIhfMHBfMIkgcCCJcCCAGm+A7VeAQPQO8r3XC//4YnD4Y3H4apuengMoMPhG8uBM+EJu4wDU0ds8MNs88gCsMrMAwvhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4APhP8tCrIPhr+CP4b/kAjQSwAAAAAAAAAAAAAAAABlWl88AgyM7L/8lw+wAD4jD4RvLgTPhCbuMA0x/4RFhvdfhk0ds8IY4dI9DTAfpAMDHIz4cgznHPC2EByM+Tiw5Ycs7NyXCOMfhEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxTi+wDjAPIArDSoACD4RHBvcn9vcYBAb3T4ZPhTAzQw+Eby4Ez4Qm7jACGT1NHQ3vpA0ds84wDyAKw2qALe+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAgBD4WSGwuvLgenPbPAEif8jPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAIxPs38DPFszLH8mAQPsAlzcANo0EcAAAAAAAAAAAAAAAABXN+xGgyM7OyXD7AARQIIIQV+OaArrjAiCCEFt7sYC64wIgghBexgSeuuMCIIIQXwvP3rrjAj08OjkBTjDR2zz4UyGOG40EcAAAAAAAAAAAAAAAADfC8/egyM7OyXD7AN7yAKwDKDD4RvLgTPhCbuMA1NHbPDDbPPIArDuzAXD4U/pCbxLAnY4Y+EUgbpIwcN74U/pCbxPXC/+6aKb7YMD/nPhJ+FPHBWim+2DAAOKw8uBw+ADbPHkBUDDR2zz4UCGOHI0EcAAAAAAAAAAAAAAAADbe7GAgyM7LH8lw+wDe8gCsAygw+Eby4Ez4Qm7jANTR2zww2zzyAKw+swC4+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAIPht+CP4cfkAjQSwAAAAAAAAAAAAAAAABlWl88CgyM7L/8lw+wAEUCCCEFK98uG64wIgghBTRRMYuuMCIIIQU862TbrjAiCCEFT13tW64wJHQ0JAAygw+Eby4Ez4Qm7jANTR2zww2zzyAKxBswC4+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAIPhu+CP4cvkAjQSwAAAAAAAAAAAAAAAABlWl88DgyM7L/8lw+wABUDDR2zz4WSGOHI0EcAAAAAAAAAAAAAAAADTzrZNgyM7LB8lw+wDe8gCsA0ow+Eby4Ez4Qm7jACGT1NHQ3vpA0x/U1NHQ+kDSANHbPDDbPPIArESzA2JyXds8JPgoxwWOGlMSjQRwAAAAAAAAAAAAAAAAA0zsZyDIzszOjoDiyXD7AI6A3l8EUkZFARxTI8jOyx9xXVUCyds8MJQBMlRwQSWJyM5VMMjPkGvHXn7MzlnIzsoAzc1oAygw+Eby4Ez4Qm7jANTR2zww2zzyAKxIswC4+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAIPhs+CP4cPkAjQSwAAAAAAAAAAAAAAAABlWl88BgyM7L/8lw+wAEUCCCEDRVjGW74wIgghA+h1Egu+MCIIIQR4Z4CbvjAiCCEFH9JmS74wJiWVRKBFAgghBJp9FTuuMCIIIQTQExz7rjAiCCEFDEGBm64wIgghBR/SZkuuMCU1BNSwP+MPhG8uBM+EJu4wDTH/hEWG91+GQhk9TR0N76QNMf1NMH0ds8IY4dI9DTAfpAMDHIz4cgznHPC2EByM+TR/SZks7NyXCOMfhEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxTi+wAw2zzyAKxMswO4c4hVBNs8aKb+YIIRKgXyAL7y4IRY+FK+8uCaIMIA8uChIMFl8uCh+CP4WL7y4IrIywf4SQHOclj4KFUCyds8+CdvEGim/mChtX9w+wL4RHBvcnBvcYEAgG90+GSbUpQDSDD4RvLgTPhCbuMAIZfTB9Mf1NHQlNMH0x/i0//R2zww2zzyAKxOswPyIts8IfkAU0G+VQMiurGOK/hJcMjPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAHEZbPMDPFsmAQPsAXwXgIVUD+ElVBYnIzlVAyM+RRiQHkssHzssfyx/L/83JcPsA+CdvEGim/mChtX9w+wIB+ElwyM+FgMoAc89AzpdoTwBAjQSAAAAAAAAAAAAAAAAAACMT7N/AzxbMyx/JgQCA+wADRDD4RvLgTPhCbuMAIZbTB9TU0dCT0wfU4vpA0ds8MNs88gCsUbMCRF8y2zwB+ElVAonIzlUwyM+QZBY1+ssHzswByM7Nzclw+wBSaAEW+ElVINs8xwXy4JmhAnYw+Eby4EzR2zwhjigj0NMB+kAwMcjPhyDOjQQAAAAAAAAAAAAAAAAMmn0VOM8Wy3/JcPsAkTDi4wDyAKqoBFAgghBAmWD7uuMCIIIQQhMWo7rjAiCCEEaklYu64wIgghBHhngJuuMCWFdWVQFQMNHbPPhKIY4cjQRwAAAAAAAAAAAAAAAAMeGeAmDIzssPyXD7AN7yAKwBTjDR2zz4TCGOG40EcAAAAAAAAAAAAAAAADGpJWLgyM7MyXD7AN7yAKwBUDDR2zz4ViGOHI0EcAAAAAAAAAAAAAAAADCExajgyM7LH8lw+wDe8gCsAU4w0ds8+EshjhuNBHAAAAAAAAAAAAAAAAAwJlg+4MjOzMlw+wDe8gCsBFAgghA2KjW7uuMCIIIQOy9GSLrjAiCCEDuOhRO64wIgghA+h1EguuMCYF5bWgFOMNHbPPhUIY4bjQRwAAAAAAAAAAAAAAAAL6HUSCDIzs7JcPsA3vIArAM0MPhG8uBM+EJu4wAhk9TR0N76QNHbPOMA8gCsXKgC3vhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4AIAg+FkhsLry4Hpx2zwBIn/Iz4WAygBzz0DOjQSAAAAAAAAAAAAAAAAAACMT7N/AzxbMyx/JgED7AJddADaNBHAAAAAAAAAAAAAAAAAHJy4b4MjOzslw+wADNjD4RvLgTPhCbuMAIZPU0dDe+kDR2zww2zzyAKxfswGg+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAIPhXicjOWcjPkVYg/9rOAcjOzc3JcPsA+HdoA/Qw+Eby4Ez4Qm7jANMf+ERYb3X4ZCGT1NHQ3tP/0ds8IY4dI9DTAfpAMDHIz4cgznHPC2EByM+S2KjW7s7NyXCOMfhEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxTi+wAw2zzyAKxhswSK+EmJxwXy0KJopv5gghEqBfIAvvLghHOIWICdyM+GQMoHy//J0IjbPPgnbxBopv5gobV/cPsC+ERwb3Jwb3GBAIBvdPhknpublARQIIIQMHBTG7rjAiCCEDDFAAa64wIgghAyUNG+uuMCIIIQNFWMZbrjAmxpZmMDJjD4RvLgTPhCbuMA0ds8MNs88gCsZLMBcvhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4AI6A2GUCtvgj+Fa8jir4I4EBLKC1HyD4dvhTjQRwAAAAAAAAAAAAAAAACyPtrGDIzs7LH8lw+wDg+FONBHAAAAAAAAAAAAAAAAAT89c+YMjOzslw+wCJ+HOJ+HRw+HVw+HaengM6MPhG8uBM+EJu4wAhk9TR0N76QNMf0ds8MNs88gCsZ7MBvPhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4APgjIbny4Hkh+HQg+HUB+FOJyM5VIMjPkLs/K3bOWcjOyx/Nzclw+wBoABrAAAAAAAAAAAAAAAABAyow+Eby4Ez4Qm7jANTTH9HbPOMA8gCsaqgD8vhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4AHj4WSGwuvLgeiCJcST4KNs8yM+FiM6NBJAX14QAAAAAAAAAAAAAAAAAAMDPFlmLgDqCGPCO+gYIyM7Oyx/NyXH7AAGeoWsBPo0EcAAAAAAAAAAAAAAAAB45Qv3gyM7Myx/JcPsA2zyTA6Yw+Eby4Ez4Qm7jACGOG9Mf0x/U0wchwgny0EnU0wchwgny0EnTH9TR0I4Y0x/TH9TTByHCCfLQSdTTByHCCfLQSdMf4tMfVXBvCAHR2zww2zzyAKxtswEq+En4V8cFaKb7YMAAsPLgcfgAjoDYbgRAIG8UIW8TwAGOgOAhbxPAAo6A4CFvE8ADjoDgIW8TwAR3dnRvA+COgOAhbxPABY6A4CFvE8AGjijQ+kDUMG8CbxAg+HeNBHAAAAAAAAAAAAAAAAAYZSiQoMjOzslw+wAw4CFvE8AHjijQ0x8wbwFvEPh4+FeNBHAAAAAAAAAAAAAAAAAYZSiQoMjOzslw+wAw4CFvE8AIc3JwAXiOMNDTBzBvAfhZIW8QhAeisPh5bxCNBHAAAAAAAAAAAAAAAAAWx4xTYMjOywfJcPsAMOABbxPACY6A4DBxAaDQ+kDTfzBvAiBvEds8u/LggyBvEfgnbxAibxCNBHAAAAAAAAAAAAAAAAAS8hCQoMjOzst/y3/JcPsAIG8RAW8QyM+FiM4B+gKAa89AyXD7AKoBZND6QNQwbwJvEPhzifh0cPh1cPh2+FONBHAAAAAAAAAAAAAAAAAa+CPq4MjOzslw+wAwngF80NP/1DBvAm8QgJ3Iz4ZAygfL/8nQ+HOJ+HRw+HVw+Hb4U40EcAAAAAAAAAAAAAAAABr4I+rgyM7OyXD7ADCeAYDQ1PpA038wbwMgbxAhbxEibxK1H9s8IG8StR8hbxFYbxCNBHAAAAAAAAAAAAAAAAAZa5164MjOzM7LH8lw+wAwdQFQAXFVAvgo2zxwyM+FgMoAc89AznHPC25ZyM+QyUNG+s7LH83JgED7AKEBrtDU0x8wbwJ/ciJvEPgo2zzIz4WIzo0FTmJaAAAAAAAAAAAAAAAAAAAFCwlWwM8WygDJcPsAfwFvEI0EcAAAAAAAAAAAAAAAABgZNqIgyM7MygDJcPsAMKEBvNDTB9QwbwIgbxEg+QBYbxBmjQRwAAAAAAAAAAAAAAAACUFmTCDIzssHy//JcPsAIMABmDD4bPgj+HAw4CDAApgw+G34I/hxMOAgwAOYMPhu+CP4cjDggQD/uo6A4Ft4AQbbPDB5AvIg+QD4QYjIz44rbNbMzsn5AI0EcAAAAAAAAAAAAAAAABHbtctgyM7L/8v/yXD7ACDQIIs4rbNYxwWT103Q3tdM0O0e7VP7BPhZ+Fj4V/hT+FL4UfhQ+E/4TvhN+Ez4S/hKyMsPzMzMzMsfyx/LH8sfzs7LH8sHyds8tHoABPACBFAgghAI76Bgu+MCIIIQD6IT37vjAiCCECN/Nhq74wIgghAuK30Wu+MCo46DfARQIIIQJakZ/LrjAiCCECbIo+y64wIgghApaXtiuuMCIIIQLit9FrrjAoKAfn0BUDDR2zz4USGOHI0EcAAAAAAAAAAAAAAAACuK30WgyM7LH8lw+wDe8gCsA+Iw+Eby4Ez4Qm7jANMf+ERYb3X4ZNHbPCGOHSPQ0wH6QDAxyM+HIM5xzwthAcjPkqWl7YrOzclwjjH4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U4vsA4wDyAKx/qAAg+ERwb3J/b3GAQG90+GT4VAPyMPhG8uBM+EJu4wDTH/hEWG91+GQhk9TR0N76QNHbPCGOHSPQ0wH6QDAxyM+HIM5xzwthAcjPkpsij7LOzclwjjH4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U4vsA4wDyAKyBqAIm+ERwb3Jwb3GAQG90+GRziFjbPJuhAU4w0ds8+E0hjhuNBHAAAAAAAAAAAAAAAAApakZ/IMjOzMlw+wDe8gCsBFAgghAQnoH9uuMCIIIQExMZirrjAiCCECMrNoO64wIgghAjfzYauuMCjIqHhAM6MPhG8uBM+EJu4wAhlNTU0dCR1OL6QNHbPOMA8gCshagC8vhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4AHT4WSGwuvLgenAhcST4KNs8yM+FiM6NBJAX14QAAAAAAAAAAAAAAAAAAMDPFlmLgDqCGPCO+gYIyM7Oyx/NyXH7AAGhhgE8jQRwAAAAAAAAAAAAAAAAHa8os+DIzszOyXD7ANs8kwNIMPhG8uBM+EJu4wAhk9TR0N76QNMHIcIJ8tBJ1NHbPDDbPPIArIizATL4SfhXxwVopvtgwACw8uBx+AABwAKOgN5biQJwINDU0x8wbwLIz4f+iQHOciJvEPgoVQLJ2zwwbxCNBHAAAAAAAAAAAAAAAAAa3tLCYMjOzMlw+wCelAMmMPhG8uBM+EJu4wDR2zww2zzyAKyLswGy+FP6Qm8SwJ2OGPhFIG6SMHDe+FP6Qm8T1wv/umim+2DA/5z4SfhTxwVopvtgwADisPLgcPgAcPh1ifh0+FONBHAAAAAAAAAAAAAAAAAMHGFR4MjOzslw+wCeAz4w+Eby4Ez4Qm7jACGU1NTR0JHU4vpA0x/R2zzjAPIArI2oAuD4U/pCbxLAnY4Y+EUgbpIwcN74U/pCbxPXC/+6aKb7YMD/nPhJ+FPHBWim+2DAAOKw8uBw+ABx+FkhsLry4HpTAcjOyx9xJPgoVQLJ2zwwAo0EcAAAAAAAAAAAAAAAAB+97regyM7MzssfyXD7ANs8lJMEUCCCEApghTO64wIgghAKjfSeuuMCIIIQDK/3WLrjAiCCEA+iE9+64wKin5GPA+Qw+Eby4Ez4Qm7jANMf+ERYb3X4ZNHbPCGOHSPQ0wH6QDAxyM+HIM5xzwthAcjPkj6IT37OzclwjjH4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U4vsAMNs88gCskLMEdPhJiccF8tCiaKb+YIIRKgXyAL7y4IRziPhJiNs8+CdvEGim/mChtX9w+wL4RHBvcnBvcYEAgG90+GSem5uUAyYw+Eby4Ez4Qm7jANTR2zzjAPIArJKoA9r4U/pCbxLAnY4Y+EUgbpIwcN74U/pCbxPXC/+6aKb7YMD/nPhJ+FPHBWim+2DAAOKw8uBw+ABy+FkhsLry4HrIz4fuiQHOciL4KFUCyds8MI0EcAAAAAAAAAAAAAAAAAR/82jgyM7MyXD7ANs8npSTAFT4U/pCbxLDnY4f+CdvEGim/mChtX9w+wL4ScjPhQjOgG/PQMmBAID7AN4E/CPDA46A3iPbPAFwyMv/cG2AQPRD+ChxWIBA9BZVBcjLB3JYgED0Q1UEc1iAQPQXVQN0WIBA9BbI9ADJ+EvIz4SA9AD0AM+BySD5AMjPigBAy//J0FUwJMjPhYjOjQSQ7msoAAAAAAAAAAAAAAAAAAHAzxYh2zzMz5DAez8nzJyXlpUADssfzMlx+wAANNDSAAGT0gQx3tIAAZPSATHe9AT0BPQE0V8DAiiIcCLAAZVb+Ez4UI6A4iDy4ItsEpuYARgiwAKVW/hN+FGOgOKZARgiwAOVW/hO+FKOgOKaAQZbiHCbAAABGCLbPCCVcrYJ8vDeMJ0AtMjMydDVMSDXSak4ApQwgQC44CDXSZQwgQC14XBwlSLXScIAjjAi0wc0MiHALphfA4EAt3TbMeAhwC+YXwOBALZ02zHgIcEgIsJ/sZhfA4EAuXTbMeDjGNxbcABDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAPkMPhG8uBM+EJu4wDTH/hEWG91+GTU0ds8IY4dI9DTAfpAMDHIz4cgznHPC2EByM+SKjfSes7NyXCOMfhEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxTi+wDjAPIArKCoASj4RHBvcnBvcYBAb3T4ZHIB+CjbPKEAjnDIy/9wbYBA9EP4KHFYgED0FlUCyMsHcliAQPRDWHNYgED0FwF0WIBA9BbI9ADJ+EvIz4SA9AD0AM+ByfkAyM+KAEDL/8nQAVAw0ds8+FghjhyNBHAAAAAAAAAAAAAAAAAimCFM4MjOyx/JcPsA3vIArAROIIIIona2uuMCIIIQCHPRfbrjAiCCEAjefBO64wIgghAI76BguuMCq6empAMqMPhG8uBM+EJu4wDSANHbPDDbPPIArKWzAAIwAVAw0ds8+E8hjhyNBHAAAAAAAAAAAAAAAAAiN58E4MjOyx/JcPsA3vIArAIuMPhG8uBMIZPU0dDe+kDTf9HbPOMA8gCpqAAo7UTQ0//TPzH4Q1jIy//LP87J7VQB4vhT+kJvEsCdjhj4RSBukjBw3vhT+kJvE9cL/7popvtgwP+c+En4U8cFaKb7YMAA4rDy4HD4ACDbPLvy4IMg+CdvEI0EcAAAAAAAAAAAAAAAABPh34XgyM7Lf8t/yXD7AAHIz4WIzgH6AoBrz0DJcPsAqgAa+CdvEIISVAvkAKG1fwFOMNHbPPhOIY4bjQRwAAAAAAAAAAAAAAAAICidraDIzszJcPsA3vIArACi7UTQ0//TP9MAMdMP1NTU1NHQ1NMf0x/TH9Mf+kDU0dD6QNMf0x/U0dD6QNMf0wfRcPhA+EH4QvhD+ET4RfhG+Ef4SPhJVfmAGm+A7Vf4Y/hiAQow2zzyAK4AEPhG8uBM8sCPAAr4RvLgTAIK9KQg9KGysQAUc29sIDAuNTYuMAEYoAAAAAIw2zz4D/IAswCK7UdwgBpvh4Abb4IwgBpwZF8K+EP4QsjL/8s/z4PLD8zMzFWwyMzLH8sfyx/LH85VUMjOyx/LH1UgyM7LH8sHzc3Nye1UAAwg+GHtHtk=",
    code: "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",
    codeHash: "6f6b7dd4499efbc7e066013ac4898974a15232a6dfb2f119ebd4ba4c1731d5c1",
};
module.exports = { D4RootContract };