const DensCertificateContract = {
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
                "name": "requestUpgrade",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "subCertRequest",
                "inputs": [
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "subexpiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subCertSynchronize",
                "inputs": [
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "subexpiry",
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
                        "name": "value0",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "setOwner",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    }
                ],
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
                "name": "withdraw",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint128"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getValue",
                "inputs": [
                    {
                        "name": "_answer_id",
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
                "name": "setValue",
                "inputs": [
                    {
                        "name": "new_value",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getExpiry",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "setExpiry",
                "inputs": [
                    {
                        "name": "_expiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "prolong",
                "inputs": [
                    {
                        "name": "length",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getRegistered",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "inquiryExpiry",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    },
                    {
                        "name": "rhash",
                        "type": "uint128"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "uint128"
                    },
                    {
                        "name": "value1",
                        "type": "uint32"
                    }
                ]
            },
            {
                "name": "getParent",
                "inputs": [
                    {
                        "name": "_answer_id",
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
                "name": "getRoot",
                "inputs": [
                    {
                        "name": "_answer_id",
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
                "name": "getName",
                "inputs": [
                    {
                        "name": "_answer_id",
                        "type": "uint32"
                    }
                ],
                "outputs": [
                    {
                        "name": "value0",
                        "type": "bytes"
                    }
                ]
            },
            {
                "name": "whois",
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
                                "name": "name",
                                "type": "bytes"
                            },
                            {
                                "name": "owner",
                                "type": "address"
                            },
                            {
                                "name": "parent",
                                "type": "address"
                            },
                            {
                                "name": "value",
                                "type": "address"
                            },
                            {
                                "name": "registered",
                                "type": "uint32"
                            },
                            {
                                "name": "expiry",
                                "type": "uint32"
                            }
                        ],
                        "name": "value0",
                        "type": "tuple"
                    }
                ]
            },
            {
                "name": "auctionProcess",
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
                        "name": "value0",
                        "type": "bool"
                    }
                ]
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
                "name": "parent",
                "inputs": [],
                "outputs": [
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "value",
                "inputs": [],
                "outputs": [
                    {
                        "name": "value",
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
                "name": "expiry",
                "inputs": [],
                "outputs": [
                    {
                        "name": "expiry",
                        "type": "uint32"
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
                        "name": "upgraded",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "upgradeRequested",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "modified",
                "inputs": [
                    {
                        "name": "value",
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
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerTransferred",
                "inputs": [
                    {
                        "name": "from",
                        "type": "address"
                    },
                    {
                        "name": "to",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "ownerForceChanged",
                "inputs": [
                    {
                        "name": "new_owner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "expiryChanged",
                "inputs": [
                    {
                        "name": "new_expiry",
                        "type": "uint32"
                    },
                    {
                        "name": "prolong",
                        "type": "bool"
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
                "name": "auctionSet",
                "inputs": [
                    {
                        "name": "owner",
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
                "name": "subCertRequested",
                "inputs": [
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "subexpiry",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "subCertSynchronized",
                "inputs": [
                    {
                        "name": "subname",
                        "type": "bytes"
                    },
                    {
                        "name": "subexpiry",
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
    codeHash: "9c20ac169ef51c3b51638f3d36897145f0c1d2872bc7795a5fa19be34cba2ab4",
};
module.exports = { DensCertificateContract };