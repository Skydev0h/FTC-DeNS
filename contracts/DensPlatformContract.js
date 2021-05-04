const DensPlatformContract = {
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
                "name": "initialize",
                "inputs": [
                    {
                        "name": "code",
                        "type": "cell"
                    },
                    {
                        "name": "owner",
                        "type": "address"
                    }
                ],
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
                "name": "type_id",
                "inputs": [],
                "outputs": [
                    {
                        "name": "type_id",
                        "type": "uint8"
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
                "name": "parent",
                "inputs": [],
                "outputs": [
                    {
                        "name": "parent",
                        "type": "address"
                    }
                ]
            }
        ],
        "data": [
            {
                "key": 1,
                "name": "root",
                "type": "address"
            },
            {
                "key": 2,
                "name": "type_id",
                "type": "uint8"
            },
            {
                "key": 3,
                "name": "name",
                "type": "bytes"
            },
            {
                "key": 4,
                "name": "parent",
                "type": "address"
            }
        ],
        "events": []
    },
    tvc: "te6ccgECHQEAA5sAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgBCj/AIrtUyDjAyDA/+MCIMD+4wLyCxoHBBABAAUC/I0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhpIds80wABjhqBAgDXGCD5AQHTAAGU0/8DAZMC+ELi+RDyqJXTAAHyeuLTPwGOHfhDIbkgnzAg+COBA+iogggbd0Cgud6TIPhj4PI02DDTHwH4I7zyudMfAQwGAQ7bPPhHbvJ8CAFCItDTA/pAMPhpqTgA3CHHANwh1w0f8rwh3QHbPPhHbvJ8CANCIIIQFsOAMLuOgOAgghBJy000u46A4CCCEHmFs/S7joDgFhEJAiggghBotV8/uuMCIIIQeYWz9LrjAgsKAUjbPPhMjQRwAAAAAAAAAAAAAAAAPmFs/SDIziHPFMlw+wB/+GcZAjww+EFu4wD4RvJzcfhm0fhJ+ErHBfLgY/gA2zx/+GcMHAFS7UTQINdJwgGOHNP/0z/TAPpA0wfU+G34bPhr+Gp/+GH4Zvhj+GKOgOINAvz0BXEhgED0Do4kjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE3/hqciGAQPQOk9cLB5Fw4vhrcyGAQPQPjoDf+Gx0IYBA9A6OJI0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABN/4bXABgEAPDgAk9A7yvdcL//hicPhjcPhmf/hhAQKIEAAAAiggghA3KV4guuMCIIIQSctNNLrjAhUSBIAw+EFu4wDU+kGK39H4SfhKxwXy4GP4ACH7BCHQ10zQ7R7tU8gg+ErPFvhMzxQizxb4Tc8WMSDJ2zxfA9s8f/hnGRQTHAAE8AIACtTR0PpAAUjbPPhKjQRwAAAAAAAAAAAAAAAALcpXiCDIziHPFslw+wB/+GcZAiggghANjyyguuMCIIIQFsOAMLrjAhgXAUrbPPhLjQRwAAAAAAAAAAAAAAAAJbDgDCDIziHPCwfJcPsAf/hnGQFI2zz4TY0EcAAAAAAAAAAAAAAAACNjyyggyM4hzxbJcPsAf/hnGQA+7UTQ0//TP9MA+kDTB9T4bfhs+Gv4an/4Yfhm+GP4YgEK9KQg9KEbARigAAAAAjDbPPgP8gAcAEL4QsjL//hDzws/+EbPCwD4SvhL+Ez4TV4wzssHzM7J7VQ=",
    code: "te6ccgECGgEAA24ABCj/AIrtUyDjAyDA/+MCIMD+4wLyCxcEAQ0BAAIC/I0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhpIds80wABjhqBAgDXGCD5AQHTAAGU0/8DAZMC+ELi+RDyqJXTAAHyeuLTPwGOHfhDIbkgnzAg+COBA+iogggbd0Cgud6TIPhj4PI02DDTHwH4I7zyudMfAQkDAQ7bPPhHbvJ8BQFCItDTA/pAMPhpqTgA3CHHANwh1w0f8rwh3QHbPPhHbvJ8BQNCIIIQFsOAMLuOgOAgghBJy000u46A4CCCEHmFs/S7joDgEw4GAiggghBotV8/uuMCIIIQeYWz9LrjAggHAUjbPPhMjQRwAAAAAAAAAAAAAAAAPmFs/SDIziHPFMlw+wB/+GcWAjww+EFu4wD4RvJzcfhm0fhJ+ErHBfLgY/gA2zx/+GcJGQFS7UTQINdJwgGOHNP/0z/TAPpA0wfU+G34bPhr+Gp/+GH4Zvhj+GKOgOIKAvz0BXEhgED0Do4kjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE3/hqciGAQPQOk9cLB5Fw4vhrcyGAQPQPjoDf+Gx0IYBA9A6OJI0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABN/4bXABgEAMCwAk9A7yvdcL//hicPhjcPhmf/hhAQKIDQAAAiggghA3KV4guuMCIIIQSctNNLrjAhIPBIAw+EFu4wDU+kGK39H4SfhKxwXy4GP4ACH7BCHQ10zQ7R7tU8gg+ErPFvhMzxQizxb4Tc8WMSDJ2zxfA9s8f/hnFhEQGQAE8AIACtTR0PpAAUjbPPhKjQRwAAAAAAAAAAAAAAAALcpXiCDIziHPFslw+wB/+GcWAiggghANjyyguuMCIIIQFsOAMLrjAhUUAUrbPPhLjQRwAAAAAAAAAAAAAAAAJbDgDCDIziHPCwfJcPsAf/hnFgFI2zz4TY0EcAAAAAAAAAAAAAAAACNjyyggyM4hzxbJcPsAf/hnFgA+7UTQ0//TP9MA+kDTB9T4bfhs+Gv4an/4Yfhm+GP4YgEK9KQg9KEYARigAAAAAjDbPPgP8gAZAEL4QsjL//hDzws/+EbPCwD4SvhL+Ez4TV4wzssHzM7J7VQ=",
    codeHash: "7954a31c2935df1315d4aeb37dc5fd71d6826ad9e1b33608418001d65cf5db41",
};
module.exports = { DensPlatformContract };