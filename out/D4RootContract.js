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
    tvc: "te6ccgEClgEAI2QAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAgaK2zWVBAQkiu1TIOMDIMD/4wIgwP7jAvILkQgFhAEABgT+jQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+Gkh2zzTAAGOHYECANcYIPkBAdMAAZTT/wMBkwL4QuIg+GX5EPKoldMAAfJ64tM/AfhDIbnytCD4I4ED6KiCCBt3QKC58rT4Y9MfAfgjvPK50x8B2zz4R26OgBoKCQcAAt4DbiLQ0wP6QDD4aak4APhEf29xggiYloBvcm1vc3BvdPhk3CHHANwh1w0fjoDfId0B2zz4R26OgN6PCgkBBlvbPJAEUCCCEC4rfRa74wIgghBSvfLhu+MCIIIQbjF3srvjAiCCEH5FAHe74wJlOxYLAiggghB6po4hu+MCIIIQfkUAd7vjAhAMAiggghB8FEuEuuMCIIIQfkUAd7rjAg8NBPow+EJu4wDTH/hEWG91+GT6QZXU0dD6QN/XDR+V1NHQ0x/fINdLwAEBwACwk9TR0N7U1w0HldTR0NMH39GNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARziCbbPGim/mCCESoF8gC+8uCEI/hSvvLgmiHCAI6EhQ4CzvLgoSHBZfLgofgj+Fi+8uCKIcjLB/hJAc5yJPgoI8nbPPgnbxBopv5gobV/cPsC+ERwb3Jwb3GBAIBvdPhkIGwTWVtsQSGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPk/kUAd7Ozclw+wB+VAFSMNHbPPhSIY4cjQRwAAAAAAAAAAAAAAAAPwUS4SDIzssfyXD7AN5/+GeOBFAgghB3Fp6SuuMCIIIQd3T/iLrjAiCCEHksBOS64wIgghB6po4huuMCFRMSEQLIMPhCbuMA0wfR+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+AD4WSGEB6KwIPh5IY0EcAAAAAAAAAAAAAAAAAg0i4MgyM7LB8sHyXD7ADDbPH/4Z46UArYw+EJu4wDTH9H4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4ACD4eCCNBHAAAAAAAAAAAAAAAAAYQC9RoMjOyx/JcPsAMNs8f/hnjpQC0jD4Qm7jANH4I/hVu/LgefhU+kJvEsCdjhX4RSBukjBw3vhU+kJvE9cL/7ry4HKZ+En4VMcF8uBy4vgA+FT4U4vcAAAAAAAAAAAAAAAAGMjOWcjPkWvq3yLOAcjOzc3JcPsA+FT4c3D4dY4UAVaNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT4dNs8f/hnlAFSMNHbPPhVIY4cjQRwAAAAAAAAAAAAAAAAPcWnpKDIzssfyXD7AN5/+GeOBFAgghBbe7GAu+MCIIIQXwvP3rvjAiCCEGLRKOG74wIgghBuMXeyu+MCNi8hFwRQIIIQYv0Ya7rjAiCCEGSYZY264wIgghBotV8/uuMCIIIQbjF3srrjAh8eGRgBUDDR2zz4VyGOG40EcAAAAAAAAAAAAAAAADuMXeygyM7OyXD7AN5/+GeOAoYw+EJu4wD4RvJzf/hm0fhC8uBv+EUgbpIwcN74Qrry4HD4APhCgJ3Iz4ZAygfL/8nQ+HNw+HiBAP/4eXD4Yts8f/hnGpQCFu1E0NdJwgGKjoDijhsEJHDtRND0BXD4aoj4a4j4bIj4bYSEhBwCwoj4bnD4b3D4cHD4cXD4co0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhzjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+HRw+HVw+HaEHQCAjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+Hdw+Hhw+HmAQPQO8r3XC//4YnD4Y3D4ZnH4agLMMPhCbuMA1NH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4APhP8tCrIPhr+CP4byD5AI0EsAAAAAAAAAAAAAAAAAZVpfPAIMjOy//JcPsAMNs8f/hnjpQD4DD4Qm7jANMf+ERYb3X4ZNTR2zwhjh8j0NMB+kAwMcjPhyDOcc8LYQHIz5OL9GGuzs3JcPsAjjP4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U+wDi4wB/+GeOIJQBdI0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhEcG9ycG9xgEBvdPhkciL4KNs8MTGMBFAgghBhgwlVuuMCIIIQYj7fX7rjAiCCEGLDlhy64wIgghBi0SjhuuMCLSUjIgOUMPhCbuMA0wfU+kGV1NHQ+kDf0V8y2zxTAfhJJYvcAAAAAAAAAAAAAAAAGMjOVTDIz5FaWPiCywfOzAHIzs3NyXD7AF8D2zx/+GeOhZQD3jD4Qm7jANMf+ERYb3X4ZNHbPCGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPk4sOWHLOzclw+wCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxT7AOLjAH/4Z44klABqjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+ERwb3J/b3GAQG90+GQw+FMD5DD4Qm7jANMf+ERYb3X4ZNMH1NHbPCGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPk4j7fX7Ozclw+wCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxT7AOLjAH/4Z44mlAO6jQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEUxGCEP/////5QTAxqwJw+Chwk1MDuY6A6DBUdjFfJaG1/9s8Its8MfhEcG9ycG9xgEBvdPhkIGxxJyqMAx5TQHHbPPkAiPkAuo6A3qQqKSgCIlR3QlM1obX/2zwj2zwyIKQzKowAAi8DjogjghD/////+UEhqwIyJMD/llMVobT/Nd4htP8mtP8moL7y4EZfNrX/iCKAf6kMJdAilSDVATIx5FMBpwjXITFvAMiTJsMAhIQrAZqOPVNi10mrAiLPNasCtgi2CFRxMKoCtQ/XGDYBzjJTcKE4J44YI9dJlSPVATU03yHPNcEIl18ib4wzyDLe3jDoXNs8Nl8FbDE0XwNsMSwALpYhb4jAALOaIW+NATNTAc0xMeggyWwhBPow+EJu4wD6QZXU0dD6QN/R+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+ACAEPhZIbAhuvLgeohwc9s8ATMxVHATf8jPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAIxPs38DPFszLH8mAQPsAI46EgC4BRI0EcAAAAAAAAAAAAAAAABXN+xGgyM7OyXD7AF8E4wB/+GeUBFAgghBbjQzzuuMCIIIQW7cZuLrjAiCCEF7GBJ664wIgghBfC8/euuMCNDIxMAFQMNHbPPhTIY4bjQRwAAAAAAAAAAAAAAAAN8Lz96DIzs7JcPsA3n/4Z44DejD4Qm7jANTR+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+AAg2zww2zx/+GeOXZQDlDD4Qm7jANMf0x/U0wchwgTy0EnU0wchwgny0EnTH9cNH5XU0dDTH99VcG8IAdH4SfhXxwXy4HH4ACBvFCFvE8ACjoDeW9s8f/hnjjOUAbQg0NTTH1lvAgEwcHIibxD4KNs8yM+FiM6NBU5iWgAAAAAAAAAAAAAAAAAABQsJVsDPFsoAyXD7AHAhbxCNBHAAAAAAAAAAAAAAAAAKJMvzoMjOzMoAyXD7ADCMA+Aw+EJu4wDU0x/R+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+AB4+FkhsCG68uB6IY0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABHEl+CjbPMjPhYjOjow1AqqNBJAX14QAAAAAAAAAAAAAAAAAAMDPFlnIz5AOoIY+z5AjvoGCzssfzclx+wBTEo0EcAAAAAAAAAAAAAAAAA14wl0gyM7Myx/JcPsA2zxfA+MAf/hni5QEUCCCEFPOtk264wIgghBU9d7VuuMCIIIQV+OaArrjAiCCEFt7sYC64wI6OTg3AVIw0ds8+FAhjhyNBHAAAAAAAAAAAAAAAAA23uxgIMjOyx/JcPsA3n/4Z44CwjD4Qm7jANTR+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+AAg+G34I/hxIPkAjQSwAAAAAAAAAAAAAAAABlWl88CgyM7L/8lw+wAw2zx/+GeOlALCMPhCbuMA1NH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4ACD4bvgj+HIg+QCNBLAAAAAAAAAAAAAAAAAGVaXzwODIzsv/yXD7ADDbPH/4Z46UAVIw0ds8+FkhjhyNBHAAAAAAAAAAAAAAAAA0862TYMjOywfJcPsA3n/4Z44EUCCCEDYqNbu74wIgghBAmWD7u+MCIIIQR4Z4CbvjAiCCEFK98uG74wJRS0Q8BFAgghBJky5yuuMCIIIQSafRU7rjAiCCEFDEGBm64wIgghBSvfLhuuMCQkE+PQLCMPhCbuMA1NH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4ACD4bPgj+HAg+QCNBLAAAAAAAAAAAAAAAAAGVaXzwGDIzsv/yXD7ADDbPH/4Z46UAz4w+EJu4wDTB9Mf1w3/ldTR0NP/39GOgNhfA9s8f/hnjj+UA/6IcCTbPAEzMSH5AFNBviCUMFMwut+OK/hJcMjPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAHEZbPMDPFsmAQPsAXwPgVHAU+Ekpi9wAAAAAAAAAAAAAAAAYyM5VQMjPkUYkB5LLB87LH8sfy//NyXD7AFMS+ElwyM+FgMoAc89AhIBAAETOjQSAAAAAAAAAAAAAAAAAACMT7N/AzxbMyx/JgED7AF8DAm4w0ds8IY4oI9DTAfpAMDHIz4cgzo0EAAAAAAAAAAAAAAAADJp9FTjPFst/yXD7AJEw4uMAf/hniJQD9jD4Qm7jANMf+ERYb3X4ZNMH1PpBldTR0PpA39HbPCGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPkyZMucrOzclw+wCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxT7AOLjAH/4Z45DlAFyjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+ERwb3Jwb3GAQG90+GRfM9s8MWwxjARQIIIQQhMWo7rjAiCCEEPLlZa64wIgghBGpJWLuuMCIIIQR4Z4CbrjAkpHRkUBUjDR2zz4SiGOHI0EcAAAAAAAAAAAAAAAADHhngJgyM7LD8lw+wDef/hnjgFQMNHbPPhMIY4bjQRwAAAAAAAAAAAAAAAAMaklYuDIzszJcPsA3n/4Z44D5jD4Qm7jAPpBldTR0PpA39cNH5XU0dDTH98g10vAAQHAALCT1NHQ3tT6QZXU0dD6QN/XDACV1NHQ0gDf0XJd2zwk+CjHBbOOK1RwQSWL3AAAAAAAAAAAAAAAABjIzlUwyM+RWgoKGszOWcjOygDNzclw+wCOhUgCWI4eUxKNBHAAAAAAAAAAAAAAAAAWGtgk4MjOzM7JcPsA4iCOgN5fBds8f/hnSZQBHshTRVjOyx9xXyQjyds8W34BUjDR2zz4ViGOHI0EcAAAAAAAAAAAAAAAADCExajgyM7LH8lw+wDef/hnjgRQIIIQOy9GSLrjAiCCEDuOhRO64wIgghA+h1EguuMCIIIQQJlg+7rjAlBOTUwBUDDR2zz4SyGOG40EcAAAAAAAAAAAAAAAADAmWD7gyM7MyXD7AN5/+GeOAVAw0ds8+FQhjhuNBHAAAAAAAAAAAAAAAAAvodRIIMjOzslw+wDef/hnjgT6MPhCbuMA+kGV1NHQ+kDf0fhT+kJvEsCdjhX4RSBukjBw3vhT+kJvE9cL/7ry4HCZ+En4U8cF8uBw4vgAgCD4WSGwIbry4HqIcHHbPAEzMVRwE3/Iz4WAygBzz0DOjQSAAAAAAAAAAAAAAAAAACMT7N/AzxbMyx/JgED7ACOOhIBPAUSNBHAAAAAAAAAAAAAAAAAHJy4b4MjOzslw+wBfBOMAf/hnlALSMPhCbuMA+kGV1NHQ+kDf0fhT+kJvEsCdjhX4RSBukjBw3vhT+kJvE9cL/7ry4HCZ+En4U8cF8uBw4vgAIPhXi9wAAAAAAAAAAAAAAAAYyM5ZyM+RViD/2s4ByM7Nzclw+wD4d9s8f/hnjpQEUCCCEDJQ0b664wIgghA0VYxluuMCIIIQNIEd1rrjAiCCEDYqNbu64wJjYFVSBPww+EJu4wDTH/hEWG91+GTXDf+V1NHQ0//f0Y0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhJjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAExwXy0KJopv5gghEqBfIAvvLghIhziCSAnciOhIRTAqLPhkDKB8v/ydAj2zz4J28QaKb+YKG1f3D7AvhEcG9ycG9xgQCAb3T4ZCBsE1lbMSGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPktio1u7Ozclw+wB+VAF2jjP4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AHHPC2kByPhEbxXPCx/Ozcn4RG8U+wDi2zx/+GeUA4Qw+EJu4wDTH9Mf1NMHIcIE8tBJ1NMHIcIJ8tBJ0x/XDR+V1NHQ0x/fVXBvCAHR+En4V8cF8uBx+ACOgNgw2zx/+GeOVpQEQCBvFCFvE8ABjoDgIW8TwAKOgOAhbxPAA46A4CFvE8AEW1pYVwDSjmUg0NP/1FlvAgEwIG8QgJ3Iz4ZAygfL/8nQ+HONCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT4dHD4dXD4dvhTjQRwAAAAAAAAAAAAAAAAGvgj6uDIzs7JcPsAW+AwAYgg0NT6QNN/VSBvAwEwIG8QIW8RIm8StR/bPCBvErUfIW8RIm8QjQRwAAAAAAAAAAAAAAAABqJLByDIzszOyx/JcPsAW1kBVFMBcSX4KNs8cMjPhYDKAHPPQM5xzwtuWcjPkMlDRvrOyx/NyYBA+wBfA4wBtCDQ1NMfWW8CATB/ciJvEPgo2zzIz4WIzo0FTmJaAAAAAAAAAAAAAAAAAAAFCwlWwM8WygDJcPsAfyFvEI0EcAAAAAAAAAAAAAAAAAoky/OgyM7MygDJcPsAW4wBxiDQ0wfUWW8CATAgbxEg+QAibxBcjQRwAAAAAAAAAAAAAAAACUFmTCDIzssHy//JcPsAIMABmFv4bFv4I/hw4CDAAphb+G1b+CP4ceAgwAOYW/huW/gj+HLgIIEA/7qOgOBfBVwBCiLbPF8FXQP+IPkA+EGIyM+OK2zWzM7J+QCNBHAAAAAAAAAAAAAAAAAR27XLYMjOy//L/8lw+wAg0CCLOK2zWMcFk9dN0N7XTNDtHu1TIPsEyCD4WfhY+Ff4U/hS+FH4UPhP+E74TfhM+Ev4SlUMyw/MzMzMyx/LH8sfyx/OzssfywcxIMnbPJVfXgACWwAE8AIDdjD4Qm7jANH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4AI6A2Ns8f/hnjmGUAer4I/hWvI4q+COBASygtR8g+Hb4U40EcAAAAAAAAAAAAAAAAAsj7axgyM7Oyx/JcPsA4PhTjQRwAAAAAAAAAAAAAAAAE/PXPmDIzs7JcPsAjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+HNiAFiNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT4dHD4dXD4dgL8MPhCbuMA+kGV1NHQ+kDf1w0fldTR0NMf39H4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4APgjIbny4Hkh+HQg+HVTAfhTi9wAAAAAAAAAAAAAAAAYyM5VIMjPkLs/K3bOWcjOyx/Nzclw+wBbjmQBCts8f/hnlARQIIIQCLagqrvjAiCCEA7eOp674wIgghAkgvJau+MCIIIQLit9FrvjAnx2bWYEUCCCECWpGfy64wIgghAmyKPsuuMCIIIQKWl7YrrjAiCCEC4rfRa64wJsamhnAVIw0ds8+FEhjhyNBHAAAAAAAAAAAAAAAAArit9FoMjOyx/JcPsA3n/4Z44D3jD4Qm7jANMf+ERYb3X4ZNHbPCGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPkqWl7YrOzclw+wCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxT7AOLjAH/4Z45plABqjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+ERwb3J/b3GAQG90+GQw+FQD8DD4Qm7jANMf+ERYb3X4ZPpBldTR0PpA39HbPCGOHyPQ0wH6QDAxyM+HIM5xzwthAcjPkpsij7LOzclw+wCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAcc8LaQHI+ERvFc8LH87NyfhEbxT7AOLjAH/4Z45rlAJyjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+ERwb3Jwb3GAQG90+GRziCPbPDExhIwBUDDR2zz4TSGOG40EcAAAAAAAAAAAAAAAAClqRn8gyM7MyXD7AN5/+GeOBFAgghAPohPfuuMCIIIQExMZirrjAiCCECMrNoO64wIgghAkgvJauuMCc3JwbgPoMPhCbuMA1NH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4AHL4WSGwIbry4HqBAPvIyweNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQBznIj+Cgjyds8MCKOfm8CSI0EcAAAAAAAAAAAAAAAABqVmNJgyM7MyXD7ANs8XwPjAH/4Z4uUA3Iw+EJu4wD6QZXU0dD6QN/XDQeV1NHQ0wffIcIE8tBJ1NH4SfhXxwXy4HH4ACHAAo6A3l8D2zx/+GeOcZQBwCDQ1NMfWW8CATCBAP/IyweNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQBznIibxD4KCPJ2zwwIW8QjQRwAAAAAAAAAAAAAAAAAyrnrGDIzszJcPsAW34C/DD4Qm7jANH4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4AHD4dY0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPh0+FONBHAAAAAAAAAAAAAAAAAMHGFR4MjOzslw+wDbPH/4Z46UBOYw+EJu4wDTH/hEWG91+GTRjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+EmNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATHBfLQomim/mCCESoF8gC+8uCEiHOI+EkjjoSEdAP+2zz4J28QaKb+YKG1f3D7AvhEcG9ycG9xgQCAb3T4ZCBsE1lbIY4fI9DTAfpAMDHIz4cgznHPC2EByM+SPohPfs7NyXD7AI4z+EQgbxMhbxL4SVUCbxHIcs9AygBzz0DOAfoC9ABxzwtpAcj4RG8Vzwsfzs3J+ERvFPsA4ts8f36UdQAE+GcEUCCCEAjefBO64wIgghAI76BguuMCIIIQCmCFM7rjAiCCEA7eOp664wJ7enl3A/4w+EJu4wDU+kGV1NHQ+kDf1w0fldTR0NMf39H4U/pCbxLAnY4V+EUgbpIwcN74U/pCbxPXC/+68uBwmfhJ+FPHBfLgcOL4AHH4WSGwIbry4HrIUyNYzssfcSX4KCPJ2zwwVHI0jQRwAAAAAAAAAAAAAAAAFXPc42DIzszOyx/Jjn54Ahhw+wDbPF8F4wB/+GeLlAFSMNHbPPhYIY4cjQRwAAAAAAAAAAAAAAAAIpghTODIzssfyXD7AN5/+GeOAh4w+EJu4wDSANEw2zx/+GeOlAFSMNHbPPhPIY4cjQRwAAAAAAAAAAAAAAAAIjefBODIzssfyXD7AN5/+GeOBEwgggiidra64wIgggs2LyO64wIgghAIc9F9uuMCIIIQCLagqrrjAo2Jhn0E8DD4Qm7jANT6QZXU0dD6QN8g10vAAQHAALCT1NHQ3tT6QZXU0dD6QN/XDR+V1NHQ0x/f0XFfJds8yFMSWM7LH3Ek+Ekjyds8MPhJcMjPhYDKAHPPQM6NBIAAAAAAAAAAAAAAAAAAB0RqDMDPFsmAQPsAXwbbPH/4Z46FfpQD/ohwJds8ATMxVHIBbXDIy/9wWIBA9EP4KHFYgED0FinIywdyWIBA9EMoc1iAQPQXJ3RYgED0Fsj0AMn4S8jPhID0APQAz4HJIPkAyM+KAEDL/8nQVTAkyM+FiM6NBJDuaygAAAAAAAAAAAAAAAAAAcDPFszPkMB7PyfMyx/MyXGEgH8ACvsAIGxxAiiIcCLAAZVb+Ez4UI6A4iDy4ItsEoSBARgiwAKVW/hN+FGOgOKCARgiwAOVW/hO+FKOgOKDAQiIMjBwhAAAARr4SV8z2zzHBfLgmV8DjAL8MPpBldTR0PpA39cNf5XU0dDTf9/R+FP6Qm8SwJ2OFfhFIG6SMHDe+FP6Qm8T1wv/uvLgcJn4SfhTxwXy4HDi+AAg2zy78uCDIPgnbxCNBHAAAAAAAAAAAAAAAAAT4d+F4MjOy3/Lf8lw+wBTAcjPhYjOAfoCgGvPQMlw+wBbiIcBCuMAf/hnlAAecPgnbxCCElQL5AChtX8xA/4w+EJu4wDU+kGV1NHQ+kDf0fhT+kJvEsCdjhX4RSBukjBw3vhT+kJvE9cL/7ry4HCZ+En4U8cF8uBw4vgAdPhZIbAhuvLgenAicSX4KNs8yM+FiM6NBJAX14QAAAAAAAAAAAAAAAAAAMDPFlnIz5AOoIY+z5AjvoGCzssfzclxjoyKAlL7AFMSjQRwAAAAAAAAAAAAAAAADHLQ7GDIzszOyXD7ANs8XwPjAH/4Z4uUAFT4U/pCbxLDnY4f+CdvEGim/mChtX9w+wL4ScjPhQjOgG/PQMmBAID7AN4Akm1wyMv/cFiAQPRD+ChxWIBA9BYjyMsHcliAQPRDInNYgED0FyF0WIBA9BbI9ADJ+EvIz4SA9AD0AM+ByfkAyM+KAEDL/8nQbDEBUDDR2zz4TiGOG40EcAAAAAAAAAAAAAAAACAona2gyM7MyXD7AN5/+GeOAKrtRNDT/9M/0gDTD9TU1NTR0NTTH9Mf0x/TH/pA1NHQ+kDTH9Mf1NHQ+kDTH9MH0fh5+Hj4d/h2+HX4dPhz+HL4cfhw+G/4bvht+Gz4a/hq+Gb4Y/hiAQow2zzyAJAABvLAjwIK9KQg9KGTkgAUc29sIDAuNDcuMAEYoAAAAAIw2zz4D/IAlACq+Fn4WPhX+Fb4VfhU+FP4UvhR+FD4T/hO+E34TPhL+Er4RvhD+ELIy//LP8oAyw/MzMxVsMjMyx/LH8sfyx/OVVDIzssfyx9VIMjOyx/LB83NzcntVAAMIPhh7R7Z",
    code: "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",
    codeHash: "6ec423e2815d37c453f4efd97fd265e23661417af294b31e73768d57dfce1fb5",
};
module.exports = { D4RootContract };