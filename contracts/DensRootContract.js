const DensRootContract = {
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
                "name": "installPlatform",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "installCertificate",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "installAuction",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "upgrade",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "requestCertificateUpgrade",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "reserveName",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "until",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "resolve",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolveRPC",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "cert",
                        "type": "address"
                    },
                    {
                        "name": "ptype",
                        "type": "uint8"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "resolveSub",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "cert",
                        "type": "address"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "auction",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "gc",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "regName",
                "inputs": [
                    {
                        "name": "callbackFunctionId",
                        "type": "uint32"
                    },
                    {
                        "components": [
                            {
                                "name": "name",
                                "type": "bytes"
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
                        "name": "request",
                        "type": "tuple"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionProcessCallback",
                "inputs": [
                    {
                        "name": "rhash",
                        "type": "uint128"
                    },
                    {
                        "name": "res",
                        "type": "bool"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certificateProcessCallback",
                "inputs": [
                    {
                        "name": "rhash",
                        "type": "uint128"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionParticipationCallback",
                "inputs": [
                    {
                        "name": "rhash",
                        "type": "uint128"
                    },
                    {
                        "name": "res",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ensureExpiry",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionFailed",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionSucceeded",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
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
                "name": "auctionSink",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "certAuctProcessCallback",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certAuctProcessCallbackDummy",
                "inputs": [
                    {
                        "name": "value0",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "directlyDeploy",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "directlyReconfigure",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "generateHash",
                "inputs": [
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
                        "type": "uint256"
                    }
                ]
            },
            {
                "name": "subCertRequest",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "_par",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subCertSync",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "_par",
                        "type": "address"
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
                        "name": "value0",
                        "type": "uint256"
                    }
                ]
            },
            {
                "name": "transferOwner",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "acceptOwner",
                "inputs": [],
                "outputs": []
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
                        "name": "value0",
                        "type": "uint256"
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
                "name": "platform_code",
                "inputs": [],
                "outputs": [
                    {
                        "name": "platform_code",
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
                "name": "owner",
                "inputs": [],
                "outputs": [
                    {
                        "name": "owner",
                        "type": "uint256"
                    }
                ]
            },
            {
                "name": "pending_owner",
                "inputs": [],
                "outputs": [
                    {
                        "name": "pending_owner",
                        "type": "uint256"
                    }
                ]
            }
        ],
        "data": [],
        "events": [
            {
                "name": "platformCodeUpdated",
                "inputs": [
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certificateCodeUpdated",
                "inputs": [
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionCodeUpdated",
                "inputs": [
                    {
                        "name": "hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "rootCodeUpdated",
                "inputs": [
                    {
                        "name": "hash",
                        "type": "uint256"
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
            },
            {
                "name": "certCodeUpgraded",
                "inputs": [
                    {
                        "name": "cert",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "prepareOwnerTransfer",
                "inputs": [
                    {
                        "name": "to",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerTransferred",
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
                "name": "withdrawn",
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
                "name": "receivedAuction",
                "inputs": [
                    {
                        "name": "amount",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certificateDeployed",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "parent",
                        "type": "address"
                    },
                    {
                        "name": "cert",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionDeployed",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "duration",
                        "type": "uint32"
                    },
                    {
                        "name": "sender",
                        "type": "address"
                    },
                    {
                        "name": "auct",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "certificateReconfigured",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "owner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "cert",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionSuccess",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "winner",
                        "type": "address"
                    },
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "auct",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "auctionFail",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "auct",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "garbage_collected",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "regNameRequest",
                "inputs": [
                    {
                        "name": "sender",
                        "type": "address"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "duration",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "regNameRejected",
                "inputs": [
                    {
                        "name": "sender",
                        "type": "address"
                    },
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "duration",
                        "type": "uint32"
                    },
                    {
                        "name": "reason",
                        "type": "uint8"
                    }
                ],
                "outputs": []
            },
            {
                "name": "nameReserved",
                "inputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "until",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "98681618b2719c4d2d97f88fe8971d8061599c949c68194b61c53a2cac9850c3",
};
module.exports = { DensRootContract };