#!/bin/bash

DST=$1
VAL=$2
NGR=$(( VAL*1000000000 ))

# cd box || exit

tonos-cli call 0:b5e9240fc2d2f1ff8cbb1d1dee7fb7cae155e5f6320e585fcc685698994a19a5 \
    sendTransaction "{\"dest\":\"$DST\",\"value\":$NGR,\"bounce\":false}" \
    --abi ../lib/GiverV2.abi.json --sign ../lib/GiverV2.keys.json
