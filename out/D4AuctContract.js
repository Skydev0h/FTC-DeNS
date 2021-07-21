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
    codeHash: "74db1f5a5482d22063dd4046ad6913e87926f76ef524a11f5dd9c07942ecb451",
};
module.exports = { D4AuctContract };