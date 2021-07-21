const D4CertContract = {
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
                "name": "requestUpgrade",
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
                ]
            },
            {
                "name": "getValue",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "index",
                        "type": "int16"
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
                "name": "setValue",
                "inputs": [
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
                        "name": "index",
                        "type": "int16"
                    }
                ],
                "outputs": []
            },
            {
                "name": "clearValues",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "registrationPreflight",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "requestId",
                        "type": "uint128"
                    }
                ],
                "outputs": [
                    {
                        "name": "requestId_",
                        "type": "uint128"
                    },
                    {
                        "name": "expiry_",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "applyAuctionResult",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "new_owner",
                        "type": "address"
                    },
                    {
                        "name": "new_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "success",
                        "type": "bool"
                    }
                ]
            },
            {
                "name": "ensureExpiry",
                "inputs": [
                    {
                        "name": "expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "retval",
                        "type": "bool"
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
                "name": "requestProlong",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "deploySub",
                "inputs": [
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
                        "name": "name",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subSynchronize",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    },
                    {
                        "name": "new_expiry",
                        "type": "uint32"
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
                "name": "withdrawExcess",
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
                "name": "value",
                "inputs": [],
                "outputs": [
                    {
                        "name": "value",
                        "type": "map(int16,address)"
                    }
                ]
            },
            {
                "name": "registered",
                "inputs": [],
                "outputs": [
                    {
                        "name": "registered",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "auctioned",
                "inputs": [],
                "outputs": [
                    {
                        "name": "auctioned",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "expires",
                "inputs": [],
                "outputs": [
                    {
                        "name": "expires",
                        "type": "uint32"
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
                "name": "excessBalanceWithdrawn",
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
                "name": "valueSet",
                "inputs": [
                    {
                        "name": "index",
                        "type": "int16"
                    },
                    {
                        "name": "value",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "valueReset",
                "inputs": [
                    {
                        "name": "index",
                        "type": "int16"
                    }
                ],
                "outputs": []
            },
            {
                "name": "valueCleared",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "upgradeRequested",
                "inputs": [
                    {
                        "name": "my_rev",
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
                "name": "upgradeReceived",
                "inputs": [
                    {
                        "name": "new_rev",
                        "type": "uint32"
                    },
                    {
                        "name": "new_hash",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "alreadyUpToDate",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "auctionResultApplied",
                "inputs": [
                    {
                        "name": "curOwner",
                        "type": "address"
                    },
                    {
                        "name": "newOwner",
                        "type": "address"
                    },
                    {
                        "name": "curExpiry",
                        "type": "uint32"
                    },
                    {
                        "name": "newExpiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "prolongRequested",
                "inputs": [
                    {
                        "name": "value",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "initialized",
                "inputs": [
                    {
                        "name": "initOwner",
                        "type": "address"
                    },
                    {
                        "name": "initExpiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "synchronized",
                "inputs": [
                    {
                        "name": "syncOwner",
                        "type": "address"
                    },
                    {
                        "name": "syncExpiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "reservedOwnerSet",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    },
                    {
                        "name": "new_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            }
        ]
    },
    tvc: "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",
    code: "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",
    codeHash: "6982b4b30370f8d2844e2b1c43e05c70f3e3512ab507dbeb9fcaf589033c8641",
};
module.exports = { D4CertContract };