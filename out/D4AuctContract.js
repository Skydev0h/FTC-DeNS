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
    codeHash: "2b7e278a07f4c0247a6cc053856fbda6ec77f4ad81adceaa9a7287c522a73077",
};
module.exports = { D4AuctContract };