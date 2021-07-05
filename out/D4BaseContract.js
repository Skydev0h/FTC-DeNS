const D4BaseContract = {
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
        "events": []
    },
    tvc: "te6ccgECJQEABWMAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAgaK2zUkBAQkiu1TIOMDIMD/4wIgwP7jAvILIQcFEgEABgL4jQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+Gkh2zzTAAGOGoECANcYIPkBAdMAAZTT/wMBkwL4QuL5EPKoldMAAfJ64tM/AfhDIbnytCD4I4ED6KiCCBt3QKC58rT4Y9MfAfgjvPK50x8B2zz4R27yfA4IAWoi0NMD+kAw+GmpOAD4RH9vcYIImJaAb3Jtb3Nwb3T4ZNwhxwDcIdcNH/K8Id0B2zz4R27yfAgDPCCCEDZgfIG74wIgghBegB/ku+MCIIIQYD2fk7vjAhoUCQIoIIIQXySbIrrjAiCCEGA9n5O64wITCgScMPhCbuMA+Ebyc3/4ZtTTH9TR+En4SscF8uCX+AD4QYjIz44rbNbMzsn4bnD4byH4cCL7BCLQIIs4rbNYxwWT103Q3tdM0O0e7VPbPFzJDiQNCwIS2zxfBNs8f/hnDB0ABPACADrIIPhQ+E/4TvhN+Ez4S/hKVQbOywfMzszLD8sfMQIW7UTQ10nCAYqOgOIgDwP+cO1E0PQFcSGAQPQOjiSNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATf+GpyIYBA9A6T1wsHkXDi+GtzIYBA9A+OgN/4bHQhgED0Do4kjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE3/htiBESEAAy+G5w+G9w+HCAQPQO8r3XC//4YnD4Y3D4ZgECiBIAAAFSMNHbPPhQIY4cjQRwAAAAAAAAAAAAAAAAN8kmyKDIzssfyXD7AN5/+GcgBFAgghBAhzZ2uuMCIIIQQJlg+7rjAiCCEEeGeAm64wIgghBegB/kuuMCGBcWFQFQMNHbPPhMIY4bjQRwAAAAAAAAAAAAAAAAN6AH+SDIzszJcPsA3n/4ZyABUjDR2zz4TyGOHI0EcAAAAAAAAAAAAAAAADHhngJgyM7LD8lw+wDef/hnIAFQMNHbPPhOIY4bjQRwAAAAAAAAAAAAAAAAMCZYPuDIzszJcPsA3n/4ZyACtjD4Qm7jANMf+ERYb3X4ZNcNf5XU0dDTf9/RcHD4SfhKxwXy4Jf4RHBvcn9vcYBAb3T4ZCJwbDIijiEk0NMB+kAwMcjPhyDOgGLPQF4Bz5MCHNnay3/LH8lw+wAgGQF6jjX4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AIBqz0BeAfhEbxXPCx/Lf8sfyfhEbxT7AOLjAH/4Zx0ETiCCCfDjkLrjAiCCECKRbaa64wIgghAlhdkjuuMCIIIQNmB8gbrjAh8eHBsBUDDR2zz4TSGOG40EcAAAAAAAAAAAAAAAAC2YHyBgyM7OyXD7AN5/+GcgAm4w+EJu4wDR+E34TPhL+EpwyM+FgMoAc89AznHPC25VIMjPkYtEo4bLB8zOzcmBAKD7AOMAf/hnIB0AWPhQ+E/4TvhN+Ez4S/hK+Eb4Q/hCyMv/yz/KAM7LB8xVMMjOzMsPyx/Nye1UAVIw0ds8+EshjhyNBHAAAAAAAAAAAAAAAAAopFtpoMjOywfJcPsA3n/4ZyABUDDR2zz4SiGOG40EcAAAAAAAAAAAAAAAACB8OOQgyM7OyXD7AN5/+GcgAFrtRNDT/9M/0gD6QNMH1NTR0PpA1NMP0x/R+HD4b/hu+G34bPhr+Gr4Zvhj+GICCvSkIPShIyIAFHNvbCAwLjQ3LjAAEKAAAAAC8sCWAAwg+GHtHtk=",
    code: "te6ccgECIgEABTYAAgaK2zUhAQQkiu1TIOMDIMD/4wIgwP7jAvILHgQCDwEAAwL4jQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+Gkh2zzTAAGOGoECANcYIPkBAdMAAZTT/wMBkwL4QuL5EPKoldMAAfJ64tM/AfhDIbnytCD4I4ED6KiCCBt3QKC58rT4Y9MfAfgjvPK50x8B2zz4R27yfAsFAWoi0NMD+kAw+GmpOAD4RH9vcYIImJaAb3Jtb3Nwb3T4ZNwhxwDcIdcNH/K8Id0B2zz4R27yfAUDPCCCEDZgfIG74wIgghBegB/ku+MCIIIQYD2fk7vjAhcRBgIoIIIQXySbIrrjAiCCEGA9n5O64wIQBwScMPhCbuMA+Ebyc3/4ZtTTH9TR+En4SscF8uCX+AD4QYjIz44rbNbMzsn4bnD4byH4cCL7BCLQIIs4rbNYxwWT103Q3tdM0O0e7VPbPFzJCyEKCAIS2zxfBNs8f/hnCRoABPACADrIIPhQ+E/4TvhN+Ez4S/hKVQbOywfMzszLD8sfMQIW7UTQ10nCAYqOgOIdDAP+cO1E0PQFcSGAQPQOjiSNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATf+GpyIYBA9A6T1wsHkXDi+GtzIYBA9A+OgN/4bHQhgED0Do4kjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE3/htiA4PDQAy+G5w+G9w+HCAQPQO8r3XC//4YnD4Y3D4ZgECiA8AAAFSMNHbPPhQIY4cjQRwAAAAAAAAAAAAAAAAN8kmyKDIzssfyXD7AN5/+GcdBFAgghBAhzZ2uuMCIIIQQJlg+7rjAiCCEEeGeAm64wIgghBegB/kuuMCFRQTEgFQMNHbPPhMIY4bjQRwAAAAAAAAAAAAAAAAN6AH+SDIzszJcPsA3n/4Zx0BUjDR2zz4TyGOHI0EcAAAAAAAAAAAAAAAADHhngJgyM7LD8lw+wDef/hnHQFQMNHbPPhOIY4bjQRwAAAAAAAAAAAAAAAAMCZYPuDIzszJcPsA3n/4Zx0CtjD4Qm7jANMf+ERYb3X4ZNcNf5XU0dDTf9/RcHD4SfhKxwXy4Jf4RHBvcn9vcYBAb3T4ZCJwbDIijiEk0NMB+kAwMcjPhyDOgGLPQF4Bz5MCHNnay3/LH8lw+wAdFgF6jjX4RCBvEyFvEvhJVQJvEchyz0DKAHPPQM4B+gL0AIBqz0BeAfhEbxXPCx/Lf8sfyfhEbxT7AOLjAH/4ZxoETiCCCfDjkLrjAiCCECKRbaa64wIgghAlhdkjuuMCIIIQNmB8gbrjAhwbGRgBUDDR2zz4TSGOG40EcAAAAAAAAAAAAAAAAC2YHyBgyM7OyXD7AN5/+GcdAm4w+EJu4wDR+E34TPhL+EpwyM+FgMoAc89AznHPC25VIMjPkYtEo4bLB8zOzcmBAKD7AOMAf/hnHRoAWPhQ+E/4TvhN+Ez4S/hK+Eb4Q/hCyMv/yz/KAM7LB8xVMMjOzMsPyx/Nye1UAVIw0ds8+EshjhyNBHAAAAAAAAAAAAAAAAAopFtpoMjOywfJcPsA3n/4Zx0BUDDR2zz4SiGOG40EcAAAAAAAAAAAAAAAACB8OOQgyM7OyXD7AN5/+GcdAFrtRNDT/9M/0gD6QNMH1NTR0PpA1NMP0x/R+HD4b/hu+G34bPhr+Gr4Zvhj+GICCvSkIPShIB8AFHNvbCAwLjQ3LjAAEKAAAAAC8sCWAAwg+GHtHtk=",
    codeHash: "cde8289d23340530c73418be2fcd11d46b344ee52aa920f64425432d3facbf4c",
};
module.exports = { D4BaseContract };