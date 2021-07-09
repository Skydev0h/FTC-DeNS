#!/bin/bash

tcli="tonos-cli"

# enforces tonos-cli, jq
./select_network.sh get call
rc="$?"

if [[ "$rc" != "0" ]]; then
  exit "$rc"
fi

# codeRoot=$(grep 'code: "' ../out/D4RootContract.js | cut -d'"' -f2)
codeBase=$(grep 'code: "' ../out/D4BaseContract.js | cut -d'"' -f2)
codeCert=$(grep 'code: "' ../out/D4CertContract.js | cut -d'"' -f2)
codeAuct=$(grep 'code: "' ../out/D4AuctContract.js | cut -d'"' -f2)
codeUser=$(grep 'code: "' ../out/D4UserContract.js | cut -d'"' -f2)
codeEmpty='te6ccgEBAQEAAgAAAA=='

tvc='../out/D4Root.tvc'
abi='../out/D4Root.abi.json'
rkf='../usr/root.keys.json'
rkp='../usr/root.phrase.txt'

if [[ ! -f "$rkf" ]]; then
  echo "[!] Root keys do not exist, generating them now"
  $tcli genaddr $tvc $abi --genkey "$rkf" | grep "Seed phrase" > "$rkp"
  echo "[#] Seed phrase saved to root.phrase.txt, keys saved to root.keys.json"
else
  echo "[#] Using existing keyfile root.keys.json"
fi

addr=$($tcli genaddr $tvc $abi --setkey $rkf | grep 'Raw address' | awk '{print $3}')
echo "[!] Root account address: $addr"

acnf=$($tcli account "$addr" | grep -c 'Account not found' )

if [[ "$acnf" != "0" ]]; then
  echo "Attempting automated transaction..."
  ./internal_tx.sh "$addr" 10
  echo "Waiting for arrival..."
  for i in {1..15}
  do
    acnf=$($tcli account "$addr" | grep -c 'Account not found' )
    if [[ "$acnf" == "0" ]]; then
      break
    fi
    sleep 2
  done
fi

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
  $tcli deploy --abi $abi --sign $rkf $tvc {}
fi

function processCode()
{
  cname="$1"
  cnameup="$(tr '[:lower:]' '[:upper:]' <<< "${cname:0:1}")${cname:1}"
  ccode="$2"

  doi=false

  echo "[=] Verifying $cname code..."
  ret=$($tcli run --abi $abi "$addr" "${cname}_code" {} | grep "\"${cname}_code\"" | awk '{print $2}')
  doi=false
  if [[ "$ret" == '"'"$codeEmpty"'"' ]]; then
    echo "[!] $cnameup code is not initialized"
    doi=true
  elif [[ "$ret" == '"'"$ccode"'"' ]]; then
    echo "[-] $cnameup code is up to date"
  else
    echo "[!] $cnameup code is unknown / outdated"
    doi=true
  fi

  if $doi; then
    echo "[*] Installing $cname code..."
    $tcli call --abi $abi --sign $rkf "$addr" "set${cnameup}Code" '{"code":"'"$ccode"'"}'
  fi
}

processCode base "$codeBase"
processCode certificate "$codeCert"
processCode auction "$codeAuct"
processCode user "$codeUser"
