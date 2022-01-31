const D4BaseContract = {
    abi: {
        "ABI version": 2,
        "version": "2.2",
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
                        "name": "code",
                        "type": "cell"
                    },
                    {
                        "name": "revision",
                        "type": "uint32"
                    },
                    {
                        "name": "param",
                        "type": "cell"
                    }
                ],
                "outputs": []
            },
            {
                "name": "registrationPreflight",
                "inputs": [
                    {
                        "name": "answerId",
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
                "name": "destroy",
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
                        "type": "string"
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
                "type": "string"
            },
            {
                "key": 4,
                "name": "st_parent",
                "type": "address"
            }
        ],
        "events": [],
        "fields": [
            {
                "name": "_pubkey",
                "type": "uint256"
            },
            {
                "name": "_timestamp",
                "type": "uint64"
            },
            {
                "name": "_constructorFlag",
                "type": "bool"
            },
            {
                "name": "st_root",
                "type": "address"
            },
            {
                "name": "st_type",
                "type": "uint8"
            },
            {
                "name": "st_name",
                "type": "string"
            },
            {
                "name": "st_parent",
                "type": "address"
            },
            {
                "name": "base_code",
                "type": "cell"
            },
            {
                "name": "m_version",
                "type": "uint16"
            },
            {
                "name": "m_revision",
                "type": "uint32"
            }
        ]
    },
    tvc: "te6ccgECKAEABTkAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAgaK2zUnBAQkiu1TIOMDIMD/4wIgwP7jAvILJAYFEQO+7UTQ10nDAfhmifhpIds80wABjhqBAgDXGCD5AQHTAAGU0/8DAZMC+ELi+RDyqJXTAAHyeuLTPwH4QyG58rQg+COBA+iogggbd0CgufK0+GPTHwH4I7zyudMfAds88jwTDgcDeu1E0NdJwwH4ZiLQ0wP6QDD4aak4APhEf29xggiYloBvcm1vc3BvdPhk3CHHAOMCIdcNH/K8IeMDAds88jwjIwcDPCCCEDVqFTe74wIgghBHhngJu+MCIIIQYD2fk7vjAhsVCAIoIIIQXySbIrrjAiCCEGA9n5O64wIUCQSUMPhCbuMA+Ebyc9TTH9TR+En4SscF8uCX+AD4QYjIz44rbNbMzsn4bnD4bwH4cCH7BAHQIIs4rbNYxwWT103Q3tdM0O0e7VPbPMkOJw0KAgzbPNs88gAMCwBU+FD4T/hO+E34TPhL+Er4Q/hCyMv/yz/Pg87LB8xVMMjOzMsPyx/Nye1UAATwAgAy+FD4T/hO+E34TPhL+ErIzssHzM7Myw/LHwIW7UTQ10nCAY6A4w0PIgSacO1E0PQFcSGAQPQOjoDfciKAQPQOk9cLB5Fw4nMjgED0D46A33QkgED0Do6A34hwIPhw+G/4bvht+Gz4a/hqgED0DvK91wv/+GJw+GMSEBIRAQKIEQAAAQKJEwBDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAFQMNHbPPhQIY4cjQRwAAAAAAAAAAAAAAAAN8kmyKDIzssfyXD7AN7yACIEUCCCEDZgfIG64wIgghBAhzZ2uuMCIIIQQJlg+7rjAiCCEEeGeAm64wIaGBcWAVAw0ds8+E8hjhyNBHAAAAAAAAAAAAAAAAAx4Z4CYMjOyw/JcPsA3vIAIgFOMNHbPPhOIY4bjQRwAAAAAAAAAAAAAAAAMCZYPuDIzszJcPsA3vIAIgP6MPhG8uBM+EJu4wDTH/hEWG91+GQhk9TR0N7Tf9HbPCKOHyTQ0wH6QDAxyM+HIM6AYs9AXgHPkwIc2drLf8sfyXCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAgGrPQF4B+ERvFc8LH8t/yx/J+ERvFOL7AOMA8gAiGR4AMPhJ+ErHBfLgl/hEcG9yf29xgEBvdPhkcAFOMNHbPPhNIY4bjQRwAAAAAAAAAAAAAAAALZgfIGDIzs7JcPsA3vIAIgROIIIJ8OOQuuMCIIIQIpFtprrjAiCCECWF2SO64wIgghA1ahU3uuMCISAdHAFOMNHbPPhMIY4bjQRwAAAAAAAAAAAAAAAALVqFTeDIzszJcPsA3vIAIgMkMPhG8uBM+EJu4wDR2zzjAPIAIh8eACjtRNDT/9M/MfhDWMjL/8s/zsntVABW+E34TPhL+EpwyM+FgMoAc89AznHPC25VIMjPkTQExz7LB8zOzcmBAKD7AAFQMNHbPPhLIY4cjQRwAAAAAAAAAAAAAAAAKKRbaaDIzssHyXD7AN7yACIBTjDR2zz4SiGOG40EcAAAAAAAAAAAAAAAACB8OOQgyM7OyXD7AN7yACIAWO1E0NP/0z/TADH6QNMH1NTR0PpA1NMP0x/R+HD4b/hu+G34bPhr+Gr4Y/hiAAr4RvLgTAIK9KQg9KEmJQAUc29sIDAuNTYuMAASoAAAAAJb8sCWAAwg+GHtHtk=",
    code: "te6ccgECJQEABQwAAgaK2zUkAQQkiu1TIOMDIMD/4wIgwP7jAvILIQMCDgO+7UTQ10nDAfhmifhpIds80wABjhqBAgDXGCD5AQHTAAGU0/8DAZMC+ELi+RDyqJXTAAHyeuLTPwH4QyG58rQg+COBA+iogggbd0CgufK0+GPTHwH4I7zyudMfAds88jwQCwQDeu1E0NdJwwH4ZiLQ0wP6QDD4aak4APhEf29xggiYloBvcm1vc3BvdPhk3CHHAOMCIdcNH/K8IeMDAds88jwgIAQDPCCCEDVqFTe74wIgghBHhngJu+MCIIIQYD2fk7vjAhgSBQIoIIIQXySbIrrjAiCCEGA9n5O64wIRBgSUMPhCbuMA+Ebyc9TTH9TR+En4SscF8uCX+AD4QYjIz44rbNbMzsn4bnD4bwH4cCH7BAHQIIs4rbNYxwWT103Q3tdM0O0e7VPbPMkLJAoHAgzbPNs88gAJCABU+FD4T/hO+E34TPhL+Er4Q/hCyMv/yz/Pg87LB8xVMMjOzMsPyx/Nye1UAATwAgAy+FD4T/hO+E34TPhL+ErIzssHzM7Myw/LHwIW7UTQ10nCAY6A4w0MHwSacO1E0PQFcSGAQPQOjoDfciKAQPQOk9cLB5Fw4nMjgED0D46A33QkgED0Do6A34hwIPhw+G/4bvht+Gz4a/hqgED0DvK91wv/+GJw+GMPDQ8OAQKIDgAAAQKJEABDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAFQMNHbPPhQIY4cjQRwAAAAAAAAAAAAAAAAN8kmyKDIzssfyXD7AN7yAB8EUCCCEDZgfIG64wIgghBAhzZ2uuMCIIIQQJlg+7rjAiCCEEeGeAm64wIXFRQTAVAw0ds8+E8hjhyNBHAAAAAAAAAAAAAAAAAx4Z4CYMjOyw/JcPsA3vIAHwFOMNHbPPhOIY4bjQRwAAAAAAAAAAAAAAAAMCZYPuDIzszJcPsA3vIAHwP6MPhG8uBM+EJu4wDTH/hEWG91+GQhk9TR0N7Tf9HbPCKOHyTQ0wH6QDAxyM+HIM6AYs9AXgHPkwIc2drLf8sfyXCOM/hEIG8TIW8S+ElVAm8RyHLPQMoAc89AzgH6AvQAgGrPQF4B+ERvFc8LH8t/yx/J+ERvFOL7AOMA8gAfFhsAMPhJ+ErHBfLgl/hEcG9yf29xgEBvdPhkcAFOMNHbPPhNIY4bjQRwAAAAAAAAAAAAAAAALZgfIGDIzs7JcPsA3vIAHwROIIIJ8OOQuuMCIIIQIpFtprrjAiCCECWF2SO64wIgghA1ahU3uuMCHh0aGQFOMNHbPPhMIY4bjQRwAAAAAAAAAAAAAAAALVqFTeDIzszJcPsA3vIAHwMkMPhG8uBM+EJu4wDR2zzjAPIAHxwbACjtRNDT/9M/MfhDWMjL/8s/zsntVABW+E34TPhL+EpwyM+FgMoAc89AznHPC25VIMjPkTQExz7LB8zOzcmBAKD7AAFQMNHbPPhLIY4cjQRwAAAAAAAAAAAAAAAAKKRbaaDIzssHyXD7AN7yAB8BTjDR2zz4SiGOG40EcAAAAAAAAAAAAAAAACB8OOQgyM7OyXD7AN7yAB8AWO1E0NP/0z/TADH6QNMH1NTR0PpA1NMP0x/R+HD4b/hu+G34bPhr+Gr4Y/hiAAr4RvLgTAIK9KQg9KEjIgAUc29sIDAuNTYuMAASoAAAAAJb8sCWAAwg+GHtHtk=",
    codeHash: "39950d05fa9fff4aff9df9890e5940b3e99a6d52b55cff18cf956590593fbc1a",
};
module.exports = { D4BaseContract };