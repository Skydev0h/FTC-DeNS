const D4TestContract = {
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
                "inputs": [
                    {
                        "name": "root",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "makeIntUser",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "makeExtUser",
                "inputs": [
                    {
                        "name": "pk",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "addressCallbackInt",
                "inputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "addressCallbackExt",
                "inputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "addLocked",
                "inputs": [
                    {
                        "name": "until",
                        "type": "uint32"
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
                "name": "requestUpgrade",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "sweepLocks",
                "inputs": [],
                "outputs": []
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
                "name": "pull",
                "inputs": [
                    {
                        "name": "value",
                        "type": "uint128"
                    }
                ],
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
                "name": "setMasterKey",
                "inputs": [
                    {
                        "name": "newMasterKey",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "createAuction",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "duration",
                        "type": "uint8"
                    }
                ],
                "outputs": []
            },
            {
                "name": "makeBid",
                "inputs": [
                    {
                        "name": "auction",
                        "type": "address"
                    },
                    {
                        "name": "data",
                        "type": "bytes"
                    },
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "revealBid",
                "inputs": [
                    {
                        "name": "auction",
                        "type": "address"
                    },
                    {
                        "name": "amount",
                        "type": "uint128"
                    },
                    {
                        "name": "nonce",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "bidRevealComplete",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "finalize",
                "inputs": [
                    {
                        "name": "auction",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "queryCert",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "queryAuct",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "forgetCert",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "forgetAuct",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "forgetMe",
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
                "name": "setValue",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    },
                    {
                        "name": "index",
                        "type": "int16"
                    },
                    {
                        "name": "new_value",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "resetValue",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    },
                    {
                        "name": "index",
                        "type": "int16"
                    }
                ],
                "outputs": []
            },
            {
                "name": "clearValues",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certWithdrawExcess",
                "inputs": [
                    {
                        "name": "target",
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
                "name": "certRequestUpgrade",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "requestProlong",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "deploySub",
                "inputs": [
                    {
                        "name": "target",
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
                "name": "syncSub",
                "inputs": [
                    {
                        "name": "target",
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
                "name": "queryCertCallback",
                "inputs": [
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
                                "name": "registered",
                                "type": "uint32"
                            },
                            {
                                "name": "auctioned",
                                "type": "uint32"
                            },
                            {
                                "name": "expires",
                                "type": "uint32"
                            },
                            {
                                "name": "owner",
                                "type": "address"
                            }
                        ],
                        "name": "info",
                        "type": "tuple"
                    }
                ],
                "outputs": []
            },
            {
                "name": "queryAuctCallback",
                "inputs": [
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
                ],
                "outputs": []
            },
            {
                "name": "certTransferOwner",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    },
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
                "name": "certCancelTransferOwner",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certAcceptTransfer",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certRelinquishOwner",
                "inputs": [
                    {
                        "name": "target",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "passToOwner",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "upgrade",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    },
                    {
                        "name": "revision",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "upgradeNotNeeded",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "hasBid",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ],
                "outputs": [
                    {
                        "name": "res",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "getBid",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ],
                "outputs": [
                    {
                        "components": [
                            {
                                "name": "time",
                                "type": "uint32"
                            },
                            {
                                "name": "data",
                                "type": "bytes"
                            },
                            {
                                "name": "hash",
                                "type": "uint256"
                            }
                        ],
                        "name": "res",
                        "type": "tuple"
                    }
                ]
            },
            {
                "name": "_root",
                "inputs": [],
                "outputs": [
                    {
                        "name": "_root",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "iaddr",
                "inputs": [],
                "outputs": [
                    {
                        "name": "iaddr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "eaddr",
                "inputs": [],
                "outputs": [
                    {
                        "name": "eaddr",
                        "type": "address"
                    }
                ]
            }
        ],
        "data": [],
        "events": []
    },
    tvc: "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",
    code: "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",
    codeHash: "bd2af8de29d01a6ab7013c75762aa8455f8c50a2f07faa90a9b130daf92b0690",
};
module.exports = { D4TestContract };