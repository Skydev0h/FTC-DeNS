const D4AuctContract = {
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
                "name": "registrationPreflightCallback",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "uint128"
                    },
                    {
                        "name": "expiry_",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getInfo",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "components": [
                            {
                                "name": "id",
                                "type": "uint32"
                            },
                            {
                                "name": "sync",
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
                                "name": "durationYears",
                                "type": "uint8"
                            },
                            {
                                "name": "startTime",
                                "type": "uint32"
                            },
                            {
                                "name": "bidEnds",
                                "type": "uint32"
                            },
                            {
                                "name": "revEnds",
                                "type": "uint32"
                            },
                            {
                                "name": "finalizeAfter",
                                "type": "uint32"
                            },
                            {
                                "name": "expiryTarget",
                                "type": "uint32"
                            }
                        ],
                        "name": "info",
                        "type": "tuple"
                    }
                ]
            },
            {
                "name": "commit",
                "inputs": [
                    {
                        "name": "result",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "accountBid",
                "inputs": [
                    {
                        "name": "user",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "revealBid",
                "inputs": [
                    {
                        "name": "user",
                        "type": "address"
                    },
                    {
                        "name": "bid_time",
                        "type": "uint32"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    },
                    {
                        "name": "nonce",
                        "type": "uint128"
                    },
                    {
                        "name": "prover",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "requiredAmountForProlong",
                "inputs": [
                    {
                        "name": "answerId",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "amount",
                        "type": "uint128"
                    }
                ]
            },
            {
                "name": "prolong",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "finalize",
                "inputs": [
                    {
                        "name": "user",
                        "type": "address"
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
                "name": "sink",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "st_root",
                "inputs": [],
                "outputs": [
                    {
                        "name": "st_root",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "st_type",
                "inputs": [],
                "outputs": [
                    {
                        "name": "st_type",
                        "type": "uint8"
                    }
                ]
            },
            {
                "name": "st_name",
                "inputs": [],
                "outputs": [
                    {
                        "name": "st_name",
                        "type": "string"
                    }
                ]
            },
            {
                "name": "st_parent",
                "inputs": [],
                "outputs": [
                    {
                        "name": "st_parent",
                        "type": "address"
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
                "name": "m_revision",
                "inputs": [],
                "outputs": [
                    {
                        "name": "m_revision",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "startTime",
                "inputs": [],
                "outputs": [
                    {
                        "name": "startTime",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "bidEnds",
                "inputs": [],
                "outputs": [
                    {
                        "name": "bidEnds",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "revEnds",
                "inputs": [],
                "outputs": [
                    {
                        "name": "revEnds",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "durationYears",
                "inputs": [],
                "outputs": [
                    {
                        "name": "durationYears",
                        "type": "uint8"
                    }
                ]
            },
            {
                "name": "expiryBase",
                "inputs": [],
                "outputs": [
                    {
                        "name": "expiryBase",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "expiryTarget",
                "inputs": [],
                "outputs": [
                    {
                        "name": "expiryTarget",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "finalizeAfter",
                "inputs": [],
                "outputs": [
                    {
                        "name": "finalizeAfter",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "instigator",
                "inputs": [],
                "outputs": [
                    {
                        "name": "instigator",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "bids",
                "inputs": [],
                "outputs": [
                    {
                        "name": "bids",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "revs",
                "inputs": [],
                "outputs": [
                    {
                        "name": "revs",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "top1",
                "inputs": [],
                "outputs": [
                    {
                        "name": "top1",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "amt1",
                "inputs": [],
                "outputs": [
                    {
                        "name": "amt1",
                        "type": "uint128"
                    }
                ]
            },
            {
                "name": "top2",
                "inputs": [],
                "outputs": [
                    {
                        "name": "top2",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "amt2",
                "inputs": [],
                "outputs": [
                    {
                        "name": "amt2",
                        "type": "uint128"
                    }
                ]
            }
        ],
        "data": [
            {
                "key": 1,
                "name": "st_root",
                "type": "address"
            },
            {
                "key": 2,
                "name": "st_type",
                "type": "uint8"
            },
            {
                "key": 3,
                "name": "st_name",
                "type": "string"
            },
            {
                "key": 4,
                "name": "st_parent",
                "type": "address"
            }
        ],
        "events": [
            {
                "name": "topUpdated",
                "inputs": [
                    {
                        "name": "num",
                        "type": "uint8"
                    },
                    {
                        "name": "user",
                        "type": "address"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "bidPlaced",
                "inputs": [
                    {
                        "name": "user",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "bidRevealed",
                "inputs": [
                    {
                        "name": "user",
                        "type": "address"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certProlonged",
                "inputs": [
                    {
                        "name": "price",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionFailed",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "auctionSucceded",
                "inputs": [
                    {
                        "name": "winner",
                        "type": "address"
                    },
                    {
                        "name": "paid",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionRejected",
                "inputs": [
                    {
                        "name": "winner",
                        "type": "address"
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
                "name": "st_root",
                "type": "address"
            },
            {
                "name": "st_type",
                "type": "uint8"
            },
            {
                "name": "st_name",
                "type": "string"
            },
            {
                "name": "st_parent",
                "type": "address"
            },
            {
                "name": "base_code",
                "type": "cell"
            },
            {
                "name": "m_version",
                "type": "uint16"
            },
            {
                "name": "m_revision",
                "type": "uint32"
            },
            {
                "name": "startTime",
                "type": "uint32"
            },
            {
                "name": "bidEnds",
                "type": "uint32"
            },
            {
                "name": "revEnds",
                "type": "uint32"
            },
            {
                "name": "durationYears",
                "type": "uint8"
            },
            {
                "name": "expiryBase",
                "type": "uint32"
            },
            {
                "name": "expiryTarget",
                "type": "uint32"
            },
            {
                "name": "finalizeAfter",
                "type": "uint32"
            },
            {
                "name": "instigator",
                "type": "address"
            },
            {
                "name": "bids",
                "type": "uint32"
            },
            {
                "name": "revs",
                "type": "uint32"
            },
            {
                "name": "top1",
                "type": "address"
            },
            {
                "name": "amt1",
                "type": "uint128"
            },
            {
                "name": "top2",
                "type": "address"
            },
            {
                "name": "amt2",
                "type": "uint128"
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "f6902412e330aa167211acf7f18b8f2a7a14f8d43611e9a5c857388df4902c7f",
};
module.exports = { D4AuctContract };