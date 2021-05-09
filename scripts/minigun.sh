#!/bin/bash

tcli=""
source ./internal_locator.sh tcli

abi=../build/DensRoot.abi.json
rkf=../keys/root.keys.json

./select_network.sh get menu

addr=$($tcli genaddr ../build/DensRoot.tvc ../build/DensRoot.abi.json --setkey $rkf | grep 'Raw address' | awk '{print $3}')
echo "[*] Root account address: $addr"

now=$(date +%s)
exp=$((now + 365*24*60*60*1))

ADDRESS="0:16727aa2069d16b632d596ea411647c32a176cb3bc970c72080d9a0647e9eebd"

for ((j=0;j<100;j++));
do
  for ((i=0;i<10;i++));
  do
    echo "DEPLOY $j $i"
    HEX=$(echo -n "mg-$j-$i" | xxd -c 1000000 -pu)
    $tcli call --abi $abi --sign $rkf "$addr" directlyDeploy '{"name":"'"$HEX"'","_owner":"'"$ADDRESS"'","expiry":'"$exp"'}' &
    sleep 0.1
  done
  sleep 5
done
