#!/bin/bash

if ! command -v jq &> /dev/null
then
    echo "Error: jq not found. Please install jq first."
    exit 1
fi

if ! command -v tonos-cli &> /dev/null
then
    echo "Error: tonos-cli not found. Please install tonos-cli first."
    exit 1
fi

tcli="tonos-cli"

function GetResultTC() {
  res="$(echo "$1" | tr '\n' ' ' | tr '\r' ' ' | cut -d'{' -f2-)"
  RES=$(echo "{ $res")
  if [ "$#" -ge 2 ]; then
    RES=$(echo "$RES" | jq -r "$2")
  fi
  export RES
  return 0
}

GetResultTC "$($tcli config)" '.url'
if [[ "$1" != "get" ]]; then
  echo "[>] Select a network for TonOS CLI execution"
fi
echo "[@] Current selected network URL: $RES"

if [[ "$1" == "get" ]]; then
  if [[ "$2" == "menu" ]]; then
    echo "[@] You can use menu entry to change the network"
  fi
  if [[ "$2" == "call" ]]; then
    echo "[@] You can use ./selnet.sh script to change the network"
  fi
  exit
fi

function SelectNetwork() {
  PS3='Please select an option: '
  options=("FreeTON DevNet (https://net.ton.dev)" "FreeTON MainNet (https://main.ton.dev)" \
           "FloodNet (https://gql.custler.net)" "LocalNode (http://localhost)" "VM LocalNode (http://localnode)"
           "Custom URL" "Exit")
  select opt in "${options[@]}"
  do
      case $opt in
          "FreeTON DevNet (https://net.ton.dev)")
            SetNet "https://net.ton.dev"; exit; ;;
          "FreeTON MainNet (https://main.ton.dev)")
            SetNet "https://main.ton.dev"; exit; ;;
          "FloodNet (https://gql.custler.net)")
            SetNet "https://gql.custler.net"; exit; ;;
          "LocalNode (http://localhost)")
            SetNet "http://localhost"; exit; ;;
          "VM LocalNode (http://localnode)")
            SetNet "http://localnode"; exit; ;;
          "Custom URL")
            read -r -p "[?] Please enter new endpoint URL: " url
            if [[ "$url" != "" ]]; then
              SetNet "$url"
            else
              echo "[!] No URL entered, aborting"
            fi
            exit; ;;
          "Exit")
              echo "[-] Exiting without any changes"; exit; ;;
          *) echo "[!] Invalid option $REPLY";;
      esac
  done
}

function SetNet() {
  echo "[*] Changing TonOS CLI network URL to $1..."
  $tcli config --url "$1" | head -n 4
  echo "}"
}

SelectNetwork

exit 0
