#!/bin/bash

tcli_sys=$(whereis tonos-cli | awk '{print $2}')
tcli=""

if [[ "$tcli_sys" != "" ]]; then
  echo "[<] Using system tonos-cli"
  tcli="$tcli_sys"
else
  echo "[>] Using local tonos-cli"
  tcli="./bin/tonos-cli"
fi

if [[ ! -f "$tcli" ]]; then
  echo "[!] tonos-cli not found! Please download or build tonos-cli and install it to bin"
  echo "[!] You can obtain it here: https://github.com/tonlabs/tonos-cli"
  echo "!!! It is not possible to proceed without installation of it"
  exit 1
fi

tvc=build/DensDebot.tvc
abi=build/DensDebot.abi.json
dkf=debot.keys.json

if [[ ! -f "debot.keys.json" ]]; then
  echo "[!] Debot keys do not exist, I cannot determine address without them"
  exit 1
fi

addr=$($tcli genaddr $tvc $abi --setkey $dkf | grep 'Raw address' | awk '{print $3}')
echo "[!] Debot account address: $addr"

acnf=$($tcli account "$addr" | grep -c 'Account not found' )

if [[ "$acnf" != "0" ]]; then
  echo "!!! The debot was not initialized. Please run deploy_debot.sh"
  exit 2
fi

acty=$($tcli account "$addr" | grep 'acc_type:' | awk '{print $2}')

if [[ "$acty" == "Uninit" ]]; then
  echo "!!! The debot was not initialized. Please run deploy_debot.sh"
  exit 3
fi

echo "Starting debot..."
$tcli debot fetch "$addr"
