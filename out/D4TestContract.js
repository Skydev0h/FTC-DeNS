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
                "inputs": [],
                "outputs": []
            },
            {
                "name": "makeIntUser",
                "inputs": [
                    {
                        "name": "root",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "addressCallback",
                "inputs": [
                    {
                        "name": "user_addr",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "makeExtUser",
                "inputs": [
                    {
                        "name": "root",
                        "type": "address"
                    },
                    {
                        "name": "pk",
                        "type": "uint256"
                    }
                ],
                "outputs": []
            },
            {
                "name": "addr",
                "inputs": [],
                "outputs": [
                    {
                        "name": "addr",
                        "type": "address"
                    }
                ]
            }
        ],
        "data": [],
        "events": []
    },
    tvc: "te6ccgECFgEAApUAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgBCSK7VMg4wMgwP/jAiDA/uMC8gsTBQQVAqwh2zzTAAGOGoECANcYIPkBAdMAAZTT/wMBkwL4QuL5EPKoldMAAfJ64tM/AfhDIbnytCD4I4ED6KiCCBt3QKC58rT4Y9MfAfgjvPK50x8B2zz4R27yfAgGAToi0NcLA6k4ANwhxwDcIdcNH/K8Id0B2zz4R27yfAYCKCCCEFtLvsu74wIgghBotV8/uuMCCQcCKjD4Qm7jAPhG8nN/+GbR+ADbPH/4ZwgRAZDtRNDXScIBio49cO1E0PQFjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+GqAQPQO8r3XC//4YnD4Y3D4ZuIPBE4gggmE2vK64wIgghAKT41huuMCIIIQPiSfDrrjAiCCEFtLvsu64wIQDQwKAjgw+kGV1NHQ+kDf1w3/ldTR0NP/39HbPOMAf/hnCxEAbvgAUwHIz4WIzo0E1ASoF8gAAAAAAAAAAAAAAAAAAMDPFgHIz5DYqNbuz5ApPjWGy//NyXH7AFsBUDDR2zz4SiGOG40EcAAAAAAAAAAAAAAAAC+JJ8OgyM7OyXD7AN5/+GcPAy4w+EJu4wD6QZXU0dD6QN/R2zzbPH/4Zw8OEQAI+AD4agAo7UTQ0//TP9IA+kDR+Gr4Zvhj+GICJDD6QZXU0dD6QN/R2zzjAH/4ZxIRACb4SvhG+EP4QsjL/8s/ygDOye1UAFr4ACDIz4WIzo0G1ASoF8gAAAAAAAAAAAAAAAAAAAfRCe+FJ8awwM8WyXH7ADACCvSkIPShFRQAFHNvbCAwLjQ3LjAAAA==",
    code: "te6ccgECEwEAAmgABCSK7VMg4wMgwP/jAiDA/uMC8gsQAgESAqwh2zzTAAGOGoECANcYIPkBAdMAAZTT/wMBkwL4QuL5EPKoldMAAfJ64tM/AfhDIbnytCD4I4ED6KiCCBt3QKC58rT4Y9MfAfgjvPK50x8B2zz4R27yfAUDAToi0NcLA6k4ANwhxwDcIdcNH/K8Id0B2zz4R27yfAMCKCCCEFtLvsu74wIgghBotV8/uuMCBgQCKjD4Qm7jAPhG8nN/+GbR+ADbPH/4ZwUOAZDtRNDXScIBio49cO1E0PQFjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+GqAQPQO8r3XC//4YnD4Y3D4ZuIMBE4gggmE2vK64wIgghAKT41huuMCIIIQPiSfDrrjAiCCEFtLvsu64wINCgkHAjgw+kGV1NHQ+kDf1w3/ldTR0NP/39HbPOMAf/hnCA4AbvgAUwHIz4WIzo0E1ASoF8gAAAAAAAAAAAAAAAAAAMDPFgHIz5DYqNbuz5ApPjWGy//NyXH7AFsBUDDR2zz4SiGOG40EcAAAAAAAAAAAAAAAAC+JJ8OgyM7OyXD7AN5/+GcMAy4w+EJu4wD6QZXU0dD6QN/R2zzbPH/4ZwwLDgAI+AD4agAo7UTQ0//TP9IA+kDR+Gr4Zvhj+GICJDD6QZXU0dD6QN/R2zzjAH/4Zw8OACb4SvhG+EP4QsjL/8s/ygDOye1UAFr4ACDIz4WIzo0G1ASoF8gAAAAAAAAAAAAAAAAAAAfRCe+FJ8awwM8WyXH7ADACCvSkIPShEhEAFHNvbCAwLjQ3LjAAAA==",
    codeHash: "5b8a55af41fa61b28d0d57e75261f861b46e06d58f174568545d8038f28e4501",
};
module.exports = { D4TestContract };