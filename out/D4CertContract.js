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
    codeHash: "b0b378bbad6d518f6af2a4f5bfbc13305186c2e37c093ddf6229d7330903f6e1",
};
module.exports = { D4CertContract };