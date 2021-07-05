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
    codeHash: "e23ee67ae90d0acb0346e2075321d2ddcf5360fa82322941b33ff51205daed1e",
};
module.exports = { D4RootContract };