const DensAuctionContract = {
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
                "name": "addBalance",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "inquiryRequest",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "rhash",
                        "type": "uint128"
                    },
                    {
                        "name": "_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "uint128"
                    },
                    {
                        "name": "value1",
                        "type": "bool"
                    },
                    {
                        "name": "value2",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "participateProxy",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "components": [
                            {
                                "name": "sender",
                                "type": "address"
                            },
                            {
                                "name": "duration",
                                "type": "uint32"
                            },
                            {
                                "name": "hash",
                                "type": "uint256"
                            }
                        ],
                        "name": "rpr",
                        "type": "tuple"
                    },
                    {
                        "name": "rhash",
                        "type": "uint128"
                    },
                    {
                        "name": "_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "uint128"
                    },
                    {
                        "name": "value1",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "bid",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "reveal",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    },
                    {
                        "name": "nonce",
                        "type": "uint256"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "finalize",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "destroy",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "root",
                "inputs": [],
                "outputs": [
                    {
                        "name": "root",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "name",
                "inputs": [],
                "outputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    }
                ]
            },
            {
                "name": "start",
                "inputs": [],
                "outputs": [
                    {
                        "name": "start",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "endBid",
                "inputs": [],
                "outputs": [
                    {
                        "name": "endBid",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "endRev",
                "inputs": [],
                "outputs": [
                    {
                        "name": "endRev",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "expiry",
                "inputs": [],
                "outputs": [
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "minfinal",
                "inputs": [],
                "outputs": [
                    {
                        "name": "minfinal",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "hashes",
                "inputs": [],
                "outputs": [
                    {
                        "name": "hashes",
                        "type": "map(address,uint256)"
                    }
                ]
            },
            {
                "name": "reveals",
                "inputs": [],
                "outputs": [
                    {
                        "name": "reveals",
                        "type": "map(address,uint128)"
                    }
                ]
            },
            {
                "name": "withdrawn",
                "inputs": [],
                "outputs": [
                    {
                        "name": "withdrawn",
                        "type": "map(address,bool)"
                    }
                ]
            },
            {
                "name": "reveal_1",
                "inputs": [],
                "outputs": [
                    {
                        "name": "reveal_1",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "reveal_2",
                "inputs": [],
                "outputs": [
                    {
                        "name": "reveal_2",
                        "type": "address"
                    }
                ]
            }
        ],
        "data": [],
        "events": [
            {
                "name": "deployed",
                "inputs": [
                    {
                        "name": "root",
                        "type": "address"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "initialized",
                "inputs": [
                    {
                        "name": "start",
                        "type": "uint32"
                    },
                    {
                        "name": "endBid",
                        "type": "uint32"
                    },
                    {
                        "name": "endRev",
                        "type": "uint32"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "bid_ev",
                "inputs": [
                    {
                        "name": "sender",
                        "type": "address"
                    },
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "revealed",
                "inputs": [
                    {
                        "name": "sender",
                        "type": "address"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    },
                    {
                        "name": "nonce",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "new_first",
                "inputs": [
                    {
                        "name": "sender",
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
                "name": "new_second",
                "inputs": [
                    {
                        "name": "sender",
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
                "name": "returned",
                "inputs": [
                    {
                        "name": "dest",
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
                "name": "failed",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "finalized",
                "inputs": [
                    {
                        "name": "winner",
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
                "name": "balanceAdded",
                "inputs": [
                    {
                        "name": "donor",
                        "type": "address"
                    },
                    {
                        "name": "value",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "95da16fc71b9a54d1d79b94a2bf4327685b1acf25b1d2a8100e31f094a3bd71a",
};
module.exports = { DensAuctionContract };