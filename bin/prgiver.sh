#!/bin/bash

DST=$1
VAL=$2
NGR=$(( VAL*1000000000 ))

# cd box || exit

tonos-cli call 0:2bb4a0e8391e7ea8877f4825064924bd41ce110fce97e939d3323999e1efbb13 \
    sendTransaction "{\"dest\":\"$DST\",\"value\":$NGR,\"bounce\":false}" \
    --abi ../lib/GiverV2.abi.json --sign ../usr/prgiver.keys.json
