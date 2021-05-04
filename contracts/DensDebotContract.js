const DensDebotContract = {
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
                        "name": "_root",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "start",
                "inputs": [],
                "outputs": []
            },
            {
                "name": "mi_Resolve",
                "inputs": [
                    {
                        "name": "index",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "mi_Resolve_1",
                "inputs": [
                    {
                        "name": "value",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            },
            {
                "name": "onResolve",
                "inputs": [
                    {
                        "name": "res",
                        "type": "address"
                    }
                ],
                "outputs": []
            },
            {
                "name": "onResolveWhois",
                "inputs": [
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
                        "name": "res",
                        "type": "tuple"
                    }
                ],
                "outputs": []
            },
            {
                "name": "mi_Root",
                "inputs": [
                    {
                        "name": "index",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "mi_Certificate",
                "inputs": [
                    {
                        "name": "index",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "mi_Auction",
                "inputs": [
                    {
                        "name": "index",
                        "type": "uint32"
                    }
                ],
                "outputs": []
            },
            {
                "name": "getVersion",
                "inputs": [],
                "outputs": [
                    {
                        "name": "name",
                        "type": "bytes"
                    },
                    {
                        "name": "semver",
                        "type": "uint24"
                    }
                ]
            },
            {
                "name": "getDebotOptions",
                "inputs": [],
                "outputs": [
                    {
                        "name": "options",
                        "type": "uint8"
                    },
                    {
                        "name": "debotAbi",
                        "type": "bytes"
                    },
                    {
                        "name": "targetAbi",
                        "type": "bytes"
                    },
                    {
                        "name": "targetAddr",
                        "type": "address"
                    }
                ]
            },
            {
                "name": "setABI",
                "inputs": [
                    {
                        "name": "dabi",
                        "type": "bytes"
                    }
                ],
                "outputs": []
            }
        ],
        "data": [],
        "events": []
    },
    tvc: "te6ccgECbQEADzoAAgE0AwEBAcACAEPQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgBCj/AIrtUyDjAyDA/+MCIMD+4wLyC2sFBGwCxCHbPNMAAY4dgQIA1xgg+QEB0wABlNP/AwGTAvhC4iD4ZfkQ8qiV0wAB8nri0z8Bjh34QyG5IJ8wIPgjgQPoqIIIG3dAoLnekyD4Y+DyNNgw0x8B+CO88rnTHwHbPPhHbvJ8SQYBOiLQ1wsDqTgA3CHHANwh1w0f8rwh3QHbPPhHbvJ8BgRYIIIQOY98FLuOgOAgghBUYqbXu46A4CCCEF+6FZG7joDgIIIQfezQ27uOgOBLQhEHAzwgghBnqTztuuMCIIIQcsN2jrrjAiCCEH3s0Nu64wJMCwgDkjD4QW7jANHbPCTA/44zJtDTAfpAMDHIz4cgzo0EAAAAAAAAAAAAAAAAD97NDbjPFiTPCwcjzxQizxQhzxbJcPsA3l8E4wB/+GdqCVIE9nCIiI0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhLbrOW+EsgbvJ/joDiM/hMbrOW+EwgbvJ/joDiMvhNbrOW+E0gbvJ/jiSNCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATiMfhKNGxsCgoBAohsBCQw+EFu4wD6QYrf0ds82zx/+GdqSAxSAQiOgNgwDQQ2cMhtbwLIi8R290IGFkZHJlc3MgjbPNs8I9s8Pz40DgQs2zzbPPhRpPhPbxC6joDg+FGk+HHbPDNoDxcCWHCI2zwgyM+FiM6NBk5iWgAAAAAAAAAAAAAAAAAAAUvJSir9BwzAzxbJcPsAEGgAJlJlcXVlc3RpbmcgdmFsdWUuLi4DPCCCEFX6Dhm64wIgghBdd4w5uuMCIIIQX7oVkbrjAiIgEgMeMPhBbuMA1NHbPNs8f/hnahNSBDYgcMhtbwLIi6UmVzb2x2aW5nII2zzbPCPQ2zw/Pj8UBBbbPIsy4uLo2zzbPD4/PhUEVNs82zwgghD/////+UEwMasCcHBtbwL4b3CTUwK5joDoMPhPUzFfJKG1/zNoGxYCfNs8AW8iIaQDWYAg9BdvAvhvcPhxjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+HDbPF8EHhcETPhR+E9vEYAg9A/ysnDIbW8CyIt0xvb2t1cCCNs82zz4UNs8ixL4Pz40GAQQ2zzbPCPQ2zw/Pj8ZBBbbPIsy4uLo2zzbPD4/PhoCcts82zz4TsjPhYjOjQZOYloAAAAAAAAAAAAAAAAAADAdvxI5YbtHQM8WIc8U+FDPFnHPCwfJcPsAMDNoAx5TMHHbPPkAiPkAuo6A3qQeHRwBOPhPJF0lobX/2zwBbyIhpANZgCD0F28C+G8gpDIeAAIvAoiII4IQ//////lBIasCMiG0/ya0/yagvvLgRiTA/5ZTFaG0/zXeJYB/qQwo0CKVINUBMjHkUwGnCNchMchtbwLIkynDAGwfAYqOPVOS10mrAiLPNasCtgi2CFRxMKoCtQ/XGDbPFjJToKE7Ko4YI9dJlSPVATU03yHPNcEIl1MSbwIzyDLe3jDoXNs8bMEzAx4w+EFu4wDU0ds82zx/+GdqIVIAMPhC+EUgbpIwcN668uBk+AD4SnGx+Gr4awQiMPhBbuMA1PpBit/6QYrf+kFqSEgjBCSK39cNH4rf1w0fit9VUG8GAdFIQUEkAg7bPNs8f/hnJVIEKnCI2zxwyG1vAsiLdPd25lcjogjbPEBoPyYEEts8I28R2zzbPD40MycESts8cMhtbwLIi8UmVnaXN0ZXJlZDogjbPNs8+CMkbxShtR9wcHBoPz4oBBrbPNs8i1cyBhZ2+Ns8MD4/KQQ02zzbPNs8cMhtbwLIi8RXhwaXJlczogaW4gg+M2gqBDjbPNs8I28V+COhtP+2C3BwJm8V+COhtP/BANs8Pz4wKwQS2zyLFzjbPNs8Pj8+LAQY2zzbPHDIbW8CyIjQM2gvLQQS2zzbPCNvE9s8Pz40LgMO2zzbPNs8MDNoUwBAQWRkcmVzcyB2YWx1ZSAocmVxdWVzdCByZXN1bHQpOgoCdCTPNasCyMhwI5kwfygzITmAfzTfJZKAMJKAIOIllymALc8LBzreJKU1JJl/Mik0IjqAfzXfKHrbPCk8MQHkjlNTkbkglDApwn/f8tBCU5GhUwe7jhkgllPDzwsHPeRTcKE4J5l/NSw3JT2AfzjfjiEnllPDzwsHPeR/NSw3JT1TB6GWU8PPCwc95IB/IaEooDjiMN5TFruOFyGOEyuAMCJvEKDPCwc8IG8RIG7yfzHkMgCMjjYmjhMrgDAibxCgzwsHPCBvESBu8n8x5H80KzYkPFMWoY4TK4AwIm8QoM8LBzwgbxEgbvJ/MeTiI7OSKzaSKzXiXzVswwBEIJUibxFus44VUyJvECLNb1AzMCFvECJvESBu8n8z6MlsIQRIINs8yMhwU2TbPAI1MzEnXzPbPAE5NybPNSDCCJcngDrPCwc4PTc+NQMujoDiU3SAQH9/cNs8AjY0MihfNNs8bJI2OD4BJMgggDrPCwcxXykif9s8ATs5MD4BHly2C7X/cHB/JcEA2zxsIzgCdiXPNasCyMhwI5kwfykzITqAfzTfJpKAMJKAIOIllyqALc8LBzveJKU1JJl/Mio0IjuAfzXfKYAQ2zwqPDkBso5TU6G5IJQwKsJ/3/LQRVOhoVMHu44ZIJZT088LBz7kU3ChOCeZfzUtNyU+gH84344hJ5ZT088LBz7kfzUtNyU+UwehllPTzwsHPuSAfyGhKKA44jDeUxa7OgFgji4hjiogbxAgwQqZLYAwIqDPCwc+n1PZkoBXkoA34iKgzwsHPuIhbxEgbvJ/MjDkOwDojmQmjiogbxAgwQqZLYAwIqDPCwc+n1PZkoBXkoA34iKgzwsHPuIhbxEgbvJ/MjDkfzQsNiQ9UxahjiogbxAgwQqZLYAwIqDPCwc+n1PZkoBXkoA34iKgzwsHPuIhbxEgbvJ/MjDk4iOzkiw2kiw14l81bNMAdnBwbW8CjjEgb1Ejl3FwIm8CbCLhkyPDAI4VIaQycG1vAl8kqQwBNiIBb1AyAW9R6CBvESBu8n8x2GwiACog+kIgbxDDAvJ1IG8SIW8T1wv/bCIANshtbwLIjhEilF8lbCLhU0VvAlMEbCNYMNhsQgBqIc81pvkh10sgliNwItcxNN7IUyO7IJVfJs8WN44QXyXXGDdTcM8WOFMmzxYzMOImXyKzbHMAKlJlY2VpdmVkIGluZm9ybWF0aW9uOgAK1NHQ0x8DPCCCEEAC67W64wIgghBHVlTcuuMCIIIQVGKm17rjAkxHQwMgMPhBbuMA0x/R2zzbPH/4Z2pEUgIiIHC+8uBkghBfuhWRiHDbPDBGRQCqjQhnDDyymxs3cQwpbatuZbBeKyLMWwxkMv4oZFjVugXdCUccIMjPhYjOjQVOYloAAAAAAAAAAAAAAAAAAASBYzJAzxYkzwsfI88UIs8KAMlw+wBfBAAYRG9tYWluIG5hbWU6A1ww+EFu4wD4RvJzcfhm+kGK39H4QvLgZPhFIG6SMHDe+EK68uBk+AD4bts8f/hnSUhSAArU0dD6QAGu7UTQINdJwgGOTdP/0z/TANXTH/QEWW8C+G/XC//4cdMH9AQBIG6T0NdM3/hr9AQBIG6T0NdM3/hs9AQBIG6U0PpAMN/4bfpA+HD4bvhqf/hh+Gb4Y/hiSgD4jnn0BXD4am34a234bG34bY0IYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPhucG1vAvhvjQhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE+HBw+HFwAYBA9A7yvdcL//hicPhjcPhmf/hh4gM8IIIQBZwNb7rjAiCCEDVBV2+64wIgghA5j3wUuuMCUU5MAyAw+EFu4wDTH9HbPNs8f/hnak1SAAIwA4Qw+EFu4wDR2zwiwP+OLSTQ0wH6QDAxyM+HIM6NBAAAAAAAAAAAAAAAAAtUFXb4zxYizxQhzwsXyXD7AN5b2zx/+GdqT1ICMIhwiHBxcCKqD7UXIqoHtRexIbFsMQEzMWxQABREZU5TIERlYm90Axww+EFu4wDR2zzbPH/4Z2pTUgDQ+ELIy//4Q88LP/hGzwsAyPhPbyL4UV4gyx/0AMv/+Er4S/hM+E34TvhQXmDPEcsHASBus5fIzAHPg88RkzDPgeIBIG6zl8jMAc+DzxGTMM+B4gEgbrOXyM4Bz4PPEZMwz4Hizs7J7VQEDHCI2zxwiGloZ1QEDNs8iIh1bWhmZVUEJIiIghBUYqbXbwPbPHBYgCD0Q2RjYlYEJIiIghBAAuu1bwPbPHFYgCD0Q2FgYlcEJIiIghBnqTztbwPbPHJYgCD0Q19eYlgEJIiIghA5j3wUbwPbPHNYgCD0Q11cYlkEIoiIcG8D2zx0WIAg9ENvAts8W2xiWgCwjQhnDWDSafZ1EZckvB76UR1AwR5uUZAu4sZpBibZLOErAtpEIMjPhYjOjQVOYloAAAAAAAAAAAAAAAAAADTAoxzAzxYkzxQjzxQibyICyx/0AMlw+wBfBAAIUXVpdAAySW50ZXJhY3Rpb24gd2l0aCBhdWN0aW9ucwAOQXVjdGlvbgAyV29ya2luZyB3aXRoIGNlcnRpZmljYXRlcwAWQ2VydGlmaWNhdGUALk9wZXJhdGluZyB0aGUgRGVOUyByb290AAhSb290ABBvIwLIzMzLHwAkUmVzb2x2ZSBhbiBhZGRyZXNzAA5SZXNvbHZlAC5BdmFpbGFibGUgZGVib3QgYWN0aW9ucwAOT3B0aW9ucwA0UGxlYXNlIHNlbGVjdCB5b3VyIG9wdGlvbjoAoo0IZww8spsbN3EMKW2rbmWwXisizFsMZDL+KGRY1boF3QlHHCDIz4WIzo0FTmJaAAAAAAAAAAAAAAAAAAAGcyThQM8WI88LHyLPFMlw+wBfAwA0V2VsY29tZSB0byB0aGUgRGVOUyBkZWJvdCEAoO1E0NP/0z/TANXTH/QEWW8C+G/XC//4cdMH9AQBIG6T0NdM3/hr9AQBIG6T0NdM3/hs9AQBIG6U0PpAMN/4bfpA+HD4bvhqf/hh+Gb4Y/hiAQr0pCD0oWwAAA==",
    code: "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",
    codeHash: "4059b532dc23a01de536e0c260e7d63c8184d596c31d69df594efff91b9b49ab",
};
module.exports = { DensDebotContract };