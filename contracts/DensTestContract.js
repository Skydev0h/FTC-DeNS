const DensTestContract = {
    abi: {
        "ABI version": 2,
        "header": [
            "time"
        ],
        "functions": [
            {
                "name": "constructor",
                "inputs": [
                    {
                        "name": "_root",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "setValue",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
                    {
                        "name": "value",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "transferOwner",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
                    {
                        "name": "new_owner",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "acceptOwner",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "regName",
                "inputs": [
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
                        "name": "req",
                        "type": "tuple"
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
                "name": "regNameCallback",
                "inputs": [
                    {
                        "name": "b",
                        "type": "bool"
                    },
                    {
                        "name": "u",
                        "type": "uint8"
                    },
                    {
                        "name": "a",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "bid",
                "inputs": [
                    {
                        "name": "dest",
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
                "name": "bidCallback",
                "inputs": [
                    {
                        "name": "res",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "reveal",
                "inputs": [
                    {
                        "name": "dest",
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
                "name": "revealCallback",
                "inputs": [
                    {
                        "name": "res",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "finalize",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "finalizeCallback",
                "inputs": [
                    {
                        "name": "res",
                        "type": "bool"
                    }
                ],
                "outputs": []
            },
            {
                "name": "requestSubCertificate",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
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
                "name": "syncSubCertificate",
                "inputs": [
                    {
                        "name": "dest",
                        "type": "address"
                    },
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
            }
        ],
        "data": [],
        "events": []
    },
    tvc: "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",
    code: "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",
    codeHash: "0534288832ad86c10736163a0e533fb82e085a0fd2abd48be868d073f3f7387a",
};
module.exports = { DensTestContract };