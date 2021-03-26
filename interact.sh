#!/bin/bash

if ! command -v jq &> /dev/null
then
    echo "Error: jq not found. Please install jq first."
    exit 1
fi

if ! command -v xxd &> /dev/null
then
    echo "Error: xxd not found. Please install xxd first."
    exit 1
fi


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

abi=build/DensRoot.abi.json
cabi=build/DensCertificate.abi.json
aabi=build/DensAuction.abi.json
rkf=root.keys.json
aid0='"_answer_id":0'
zero='0x0000000000000000000000000000000000000000000000000000000000000000'

addr=$($tcli genaddr build/DensRoot.tvc build/DensRoot.abi.json --setkey $rkf | grep 'Raw address' | awk '{print $3}')
echo "[*] Root account address: $addr"
root=$addr

echo "[>] You can use enter when in any menu to display option keys again! [<]"

function InputAddress() {
  WCID=""
  ADDR=""
  ADDRESS=""
  export WCID ADDR ADDRESS
  IFS=":" read -r -p "$1" -a entered
  elems=${#entered[@]}
  if (( elems != 2 )); then
    echo 'Incorrect address format, please use format workchainId(0/-1):hexAddress(64 hex chars)'
    return 0
  fi
  WCID=${entered[0]}
  if [[ "$WCID" != "0" && "$WCID" != "-1" ]]; then
    echo 'Incorrect workchain ID, please use 0 or -1 before :'
    return 0
  fi
  ADDR=${entered[1]}
  ALEN=${#ADDR}
  if [[ "$ALEN" != 64 ]]; then
    echo 'Incorrect address length, please use 64 hex characters'
    return 0
  fi
  if ! [[ "$ADDR" =~ ^[0-9A-Fa-f]{64}$ ]] ; then
    echo "Incorrect address format, please use 64 hex characters"
    return 0
  fi
  ADDRESS="$WCID:$ADDR"
  export WCID ADDR ADDRESS
  return 1
}

function InputPubKey() {
  PUBKEY=""
  export PUBKEY
  read -r -p "$1" entered
  if ! [[ "$entered" =~ ^[0-9A-Fa-f]{64}$ ]] ; then
    echo "Incorrect pubkey format, please use 64 hex characters"
    return 0
  fi
  PUBKEY="$entered"
  export PUBKEY
  return 1
}

function InputText() {
  TEXT=""
  export TEXT
  read -r -p "$1" entered
  TEXT="$entered"
  export TEXT
  return 1
}

function InputNumber() {
  NUMBER=""
  export NUMBER
  read -r -p "$1" entered
  if [[ ! "$entered" =~ ^[0-9]+$ ]] ; then
    echo "[!] Invalid entered number format"
    return 0
  fi
  NUMBER="$entered"
  export NUMBER
  return 1
}

function ToHex() {
  HEX=$(echo -n "$1" | xxd -c 1000000 -pu)
  export HEX
}

function GetResult() {
  res="$(echo "$1" | tr '\n' ' ' | tr '\r' ' ' | cut -d'{' -f3-)"
  RES=$(echo "{ $res")
  if [ "$#" -ge 2 ]; then
    RES=$(echo "$RES" | jq -r "$2")
  fi
  export RES
  return 0
}

function Resolve() {
  RES=$(echo "$1" | jq -r "$2")
  export RES
  return 0
}

# ======================================================================================================================

function MainMenu() {
  # echo "Root address: $addr"
  PS3='[/] Please select an option: '
  options=("Resolve an address" "Root actions" "Certificate actions" "Auction actions" "Set root address" "Quit")
  select opt in "${options[@]}"
  do
      case $opt in
          "Resolve an address")
              echo "[>] Entering address resolution mode"
              MResolve; break; ;;
          "Root actions")
              echo "[>] Entering root contract operation mode"
              MRoot; break; ;;
          "Certificate actions")
              echo "[>] Entering certificate operation mode"
              MCertificate; break; ;;
          "Auction actions")
              echo "[>] Entering auction operation mode"
              MAuction; break; ;;
          "Set root address")
              echo "[>] Configuring root address"
              MRootAddress; break; ;;
          "Quit")
              echo "[!] Bye bye!"
              exit; ;;
          *) echo "[!] Invalid option $REPLY";;
      esac
  done
}

# ======================================================================================================================

function MResolve() {
  if [[ "$root" == "" ]]; then
    echo "[!] Root address not set! Please configure root address first!"
    return
  fi
  IFS='/' read -r -p '[/resolve/] Please enter domain name: ' -a dom
  parent="$root"
  crumb=""
  for piece in "${dom[@]}"; do
    crumb="$crumb/$piece"
    echo "[.] Resolving $crumb certificate address..."
    ToHex "$piece"
    GetResult "$($tcli run --abi $abi "$root" resolveRPC "{$aid0,\"name\":\"$HEX\",\"cert\":\"$parent\",\"ptype\":1}")" '.value0'
    if [[ "$RES" == "" ]]; then
      echo "[!] Failed when resolving $piece element"
      return
    fi
    echo "[-] Obtained certificate address: $RES"
    parent="$RES"
  done
  echo "[*] Final certificate address: $parent"
  GetResult "$($tcli run --abi $cabi "$parent" whois "{$aid0}")" '.value0'
  if [[ "$RES" == "" ]]; then
    echo "[!] Failed to inquiry information about the certificate!"
    return
  fi
  info="$RES"
  Resolve "$info" ".owner"
  echo "[.] Certificate owned by $RES"
  Resolve "$info" ".expiry"
  expires="$RES"
  Resolve "$info" ".registered"
  registr="$RES"
  echo "[.] Registered at $(date -d "@$registr"), expires at $(date -d "@$expires")"
  Resolve "$info" ".value"
  echo "[*] Certificate value is: $RES"
}

# ======================================================================================================================

function MRoot() {
  if [[ "$root" == "" ]]; then
    echo "Root address not set! Please configure root address first!"
    return
  fi
  if [[ ! -f "$rkf" ]]; then
    echo "[!] Root keyfile does not exist, please configure root.keys.json first!"
    return
  fi
  PS3='[/root/] Please select an option: '
  options=("Change ownership" "Reserve a domain" "Directly deploy certificate" "Directly reconfigure certificate" \
           "Withdraw excess funds" "Return")
  select opt in "${options[@]}"
  do
      case $opt in
          "Change ownership")
              echo "[>] Entering root ownership change mode"
              MRootChOwn; ;;
          "Reserve a domain")
              echo "[>] Entering domain reservation mode"
              MRootReserve; ;;
          "Directly deploy certificate")
              echo "[>] Entering certificate deployment mode"
              MRootDeploy; ;;
          "Directly reconfigure certificate")
              echo "[>] Entering certificate reconfiguration mode"
              MRootReconfigure; ;;
          "Withdraw excess funds")
              echo "[>] Entering withdrawal mode"
              MRootWithdraw; ;;
          "Return")
              echo "[<] Returning to main menu"
              return; ;;
          *) echo "[!] Invalid option $REPLY";;
      esac
  done
}

function MRootChOwn() {
  echo '[/root/chown/] Verifying pending ownership change...'
  GetResult "$($tcli run --abi $abi "$root" pending_owner "{}")" '.pending_owner'
  if [[ "$RES" == "" ]]; then
    echo "[!] Failed to retrieve pending ownership change!"
    return
  fi
  if [[ "$RES" == "$zero" ]]; then
    echo "[-] There is no pending ownership change"
  else
    echo "[>] There is a pending ownership change to $RES"
  fi
  PS3='[/root/chown/] Please select an option: '
  options=("Cancel pending ownership change" "Initiate ownership change" "Accept ownership" "Return")
  select opt in "${options[@]}"
  do
      case $opt in
          "Cancel pending ownership change")
              echo "[>] Configuring ownership change to zero pubkey..."
              $tcli call --abi $abi --sign $rkf "$addr" transferOwner '{"new_owner":"'"$zero"'"}'
              ;;
          "Initiate ownership change")
              InputPubKey "[?] Please enter new owner's public key (without 0x): "
              if [[ "$PUBKEY" != "" ]]; then
                echo "[>] Configuring ownership change to 0x$PUBKEY..."
                $tcli call --abi $abi --sign $rkf "$addr" transferOwner '{"new_owner":"'"0x$PUBKEY"'"}'
              fi
              ;;
          "Accept ownership")
              echo "[>] Attempting to accept ownership change..."
              $tcli call --abi $abi --sign $rkf "$addr" acceptOwner '{}'
              ;;
          "Return")
              echo "[<] Returning to root actions menu"
              return; ;;
          *) echo "[!] Invalid option $REPLY";;
      esac
  done
}

function MRootReserve() {
  InputText "[?] Please enter a domain name to reserve: "
  if [[ "$TEXT" == "" ]]; then
    echo "[!] No domain name entered"
    return
  fi
  echo '[*] Enter 0 to unreserve, 1 for permanent or unix time to reserve until'
  InputNumber '[?] Enter reservation expiration unix time: '
  if [[ "$NUMBER" == "" ]]; then
    echo "[!] No correct reservation expiration entered"
    return
  fi
  ToHex "$TEXT"
  $tcli call --abi $abi --sign $rkf "$addr" reserveName '{"name":"'"$HEX"'","until":'"$NUMBER"'}'
}

function MRootDeploy() {
  InputText "[?] Please enter a domain name to deploy: "
  if [[ "$TEXT" == "" ]]; then
    echo "[!] No domain name entered"
    return
  fi
  echo '[*] Enter 0 for permanent domain or lifetime in years'
  InputNumber '[?] Enter domain lifetime in years: '
  if [[ "$NUMBER" == "" ]]; then
    echo "[!] No correct lifetime entered"
    return
  fi
  InputAddress "[?] Enter initial domain owner address: "
  if [[ "$ADDRESS" == "" ]]; then
    echo "[!] No correct owner address entered"
    return
  fi
  ToHex "$TEXT"
  now=$(date +%s)
  exp=4294967295
  if [[ "$NUMBER" != "0" ]]; then
    exp=$((now + 365*24*60*60*NUMBER))
  fi
  echo "[>] Deploying $TEXT domain with expiration $exp and owner $ADDRESS"
  $tcli call --abi $abi --sign $rkf "$addr" directlyDeploy '{"name":"'"$HEX"'","_owner":"'"$ADDRESS"'","expiry":'"$exp"'}'
}

function MRootReconfigure() {
  InputText "[?] Please enter a domain name to reconfigure: "
  if [[ "$TEXT" == "" ]]; then
    echo "[!] No domain name entered"
    return
  fi
  echo '[*] Enter 0 for permanent domain or lifetime in years'
  InputNumber '[?] Enter domain lifetime in years: '
  if [[ "$NUMBER" == "" ]]; then
    echo "[!] No correct lifetime entered"
    return
  fi
  InputAddress "[?] Enter new domain owner address: "
  if [[ "$ADDRESS" == "" ]]; then
    echo "[!] No correct owner address entered"
    return
  fi
  ToHex "$TEXT"
  now=$(date +%s)
  exp=4294967295
  if [[ "$NUMBER" != "0" ]]; then
    exp=$((now + 365*24*60*60*NUMBER))
  fi
  echo "[>] Reconfiguring $TEXT domain with expiration $exp and owner $ADDRESS"
  $tcli call --abi $abi --sign $rkf "$addr" directlyReconfigure '{"name":"'"$HEX"'","_owner":"'"$ADDRESS"'","expiry":'"$exp"'}'
}

function MRootWithdraw() {
  echo "[!] Not implemented yet"
}

# ======================================================================================================================

function MCertificate() {
  PS3='[/certificate/] Please select an option: '
  echo "[!] Not implemented yet"
}

# ======================================================================================================================

function MAuction() {
  PS3='[/auction/] Please select an option: '
  echo "[!] Not implemented yet"
}

# ======================================================================================================================

function MRootAddress() {
  echo "Current root address: [$root]"
  InputAddress 'Please enter new root address: '
  if [[ "$ADDRESS" != "" ]]; then
    export root="$ADDRESS"
    echo "Root address changed to [$root]"
  fi
}

# ======================================================================================================================

while true
do
  MainMenu
done
