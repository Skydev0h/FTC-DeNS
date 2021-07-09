#!/bin/bash

tcli="tonos-cli"

# enforces tonos-cli, jq
./select_network.sh get call
rc="$?"

if [[ "$rc" != "0" ]]; then
  exit "$rc"
fi

tvc='../lib/sms/SafeMultisigWallet.tvc'
abi='../lib/sms/SafeMultisigWallet.abi.json'
bkf='../usr/box.keys.json'
bkp='../usr/box.phrase.txt'

if [[ ! -f "$bkf" ]]; then
  echo "[!] Box keys do not exist, generating them now"
  $tcli genaddr "$tvc" "$abi" --genkey "$bkf" | grep "Seed phrase" > "$bkp"
  echo "[#] Box phrase saved to box.phrase.txt, keys saved to box.keys.json"
else
  echo "[#] Using existing keyfile box.keys.json"
fi

addr=$($tcli genaddr "$tvc" "$abi" --setkey $bkf | grep 'Raw address' | awk '{print $3}')
if [[ "$addr" == "" ]]; then
  echo "tonos-cli failed"
  $tcli genaddr "$tvc" "$abi" --setkey $bkf
  exit 2
fi
echo "[!] Box (helper multisig) account address: $addr"

acnf=$($tcli account "$addr" | grep -c 'Account not found' )

if [[ "$acnf" != "0" ]]; then
  echo "[!] The account does not exist yet. Prior to deploying you need to send some tokens to it."
  echo "!!! Please send some tokens to the account with address above and re-run the deployment script."
  exit 2
fi

acty=$($tcli account "$addr" | grep 'acc_type:' | awk '{print $2}')

if [[ "$acty" != "Uninit" ]]; then
  echo "[-] Account state is $acty, deployment is not needed"
else
  echo "[*] Deploying the contract..."
  pub=$(jq -r ".public" "$bkf")
  par="{\"owners\":[\"0x$pub\"],\"reqConfirms\":1}"
  $tcli deploy --abi "$abi" --sign "$bkf" "$tvc" "$par"
fi

echo "Checking current account state:"
$tcli account "$addr"
