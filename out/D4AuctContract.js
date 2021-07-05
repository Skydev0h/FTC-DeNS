const D4AuctContract = {
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
                        "name": "_answer_id",
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
                                "type": "bytes"
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
                        "name": "_answer_id",
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
                        "type": "bytes"
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
                "type": "bytes"
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
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "2b1086c6023b19d0fdaeb61309d6e5c7365724e7809542828341457d9a71960a",
};
module.exports = { D4AuctContract };