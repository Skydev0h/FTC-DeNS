#!/bin/bash

solc_sys=$(whereis solc | awk '{print $2}')
link_sys=$(whereis tvm_linker | awk '{print $2}')
tcli_sys=$(whereis tonos-cli | awk '{print $2}')

solc=""
link=""
tcli=""

if [[ "$solc_sys" != "" ]]; then
  echo "[<] Using system solc"
  solc="$solc_sys"
else
  echo "[>] Using local solc"
  solc="../bin/solc"
fi

if [[ "$link_sys" != "" ]]; then
  echo "[<] Using system tvm_linker"
  link="$link_sys"
else
  echo "[>] Using local tvm_linker"
  link="../bin/tvm_linker"
fi

if [[ "$tcli_sys" != "" ]]; then
  echo "[<] Using system tonos-cli"
  tcli="$tcli_sys"
else
  echo "[>] Using local tonos-cli"
  tcli="./bin/tonos-cli"
fi

if [[ ! -f "$solc" ]]; then
  echo "[*] solc not found! Please download or build solc and install it to bin"
  echo "[*] You can obtain it here: https://github.com/tonlabs/TON-Solidity-Compiler"
  echo "[*] Without it contracts will not be recompiled from source"
fi

if [[ ! -f "$link" ]]; then
  echo "[*] tvm_linker not found! Please download or build tvm_linker and install it to bin"
  echo "[*] You can obtain it here: https://github.com/tonlabs/TVM-linker"
  echo "[*] Without it contracts would not be linked from source"
fi

if [[ ! -f "$tcli" ]]; then
  echo "[!] tonos-cli not found! Please download or build tonos-cli and install it to bin"
  echo "[!] You can obtain it here: https://github.com/tonlabs/tonos-cli"
  echo "!!! It is not possible to proceed without installation of it"
  exit 1
fi

./selnet.sh get call

if [[ -f "$solc" ]]; then
  cd contracts || exit
  echo "[*] Building contracts..."
  $solc DensRoot.sol >/dev/null
  $solc DensPlatform.sol >/dev/null
  $solc DensCertificate.sol >/dev/null
  $solc DensAuction.sol >/dev/null
  mv ./*.code ../build/
  mv ./*.json ../build/
  cd .. || exit

  if [[ -f "$link" ]]; then
    cd build || exit
    echo "[*] Linking contracts..."
    $link compile DensRoot.code -a DensRoot.abi.json -o DensRoot.tvc --lib stdlib_sol.tvm >/dev/null
    $link compile DensPlatform.code -a DensPlatform.abi.json -o DensPlatform.tvc --lib stdlib_sol.tvm >/dev/null
    $link compile DensCertificate.code -a DensCertificate.abi.json -o DensCertificate.tvc --lib stdlib_sol.tvm >/dev/null
    $link compile DensAuction.code -a DensAuction.abi.json -o DensAuction.tvc --lib stdlib_sol.tvm >/dev/null

    echo "Extracting code for installation..."
    $link decode --tvc DensPlatform.tvc > dens_platform.txt
    $link decode --tvc DensCertificate.tvc > dens_certificate.txt
    $link decode --tvc DensAuction.tvc > dens_auction.txt

    cat dens_platform.txt | grep 'code:' | cut -d' ' -f3 > code_plat.txt
    cat dens_certificate.txt | grep 'code:' | cut -d' ' -f3 > code_cert.txt
    cat dens_auction.txt | grep 'code:' | cut -d' ' -f3 > code_auct.txt

    cd .. || exit
  else
    echo "[-] Linking contracts and extracting code skipped"
  fi

else
  echo "[-] Building and linking contracts skipped"
fi

c_plat=$(cat build/code_plat.txt)
c_cert=$(cat build/code_cert.txt)
c_auct=$(cat build/code_auct.txt)
c_empt='te6ccgEBAQEAAgAAAA=='

tvc='build/DensRoot.tvc'
abi=build/DensRoot.abi.json
rkf=root.keys.json

if [[ ! -f "root.keys.json" ]]; then
  echo "[!] Root keys do not exist, generating them now"
  $tcli genaddr $tvc $abi --genkey $rkf | grep "Seed phrase" > root.phrase.txt
  echo "[#] Seed phrase saved to root.phrase.txt, keys saved to root.keys.json"
else
  echo "[#] Using existing keyfile root.keys.json"
fi

addr=$($tcli genaddr $tvc $abi --setkey $rkf | grep 'Raw address' | awk '{print $3}')
echo "[!] Root account address: $addr"

acnf=$($tcli account "$addr" | grep -c 'Account not found' )

if [[ "$acnf" != "0" ]]; then
  ./tx.sh "$addr" 10
fi

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
  $tcli deploy --abi $abi --sign $rkf $tvc {}
fi

echo "[=] Verifying platform code..."
ret=$($tcli run --abi $abi "$addr" platform_code {} | grep '"platform_code"' | awk '{print $2}')
doi=false
if [[ "$ret" == '"'"$c_empt"'"' ]]; then
  echo "[!] Platform code is not initialized"
  doi=true
elif [[ "$ret" == '"'"$c_plat"'"' ]]; then
  echo "[-] Platform code is up to date"
else
  echo "[!] Platform code is unknown / outdated"
  doi=true
fi

if $doi; then
  echo "[*] Installing platform code..."
  $tcli call --abi $abi --sign $rkf "$addr" installPlatform '{"code":"'"$c_plat"'"}'
fi

echo "[=] Verifying certificate code..."
ret=$($tcli run --abi $abi "$addr" certificate_code {} | grep '"certificate_code"' | awk '{print $2}')
doi=false
if [[ "$ret" == '"'"$c_empt"'"' ]]; then
  echo "[!] Certificate code is not initialized"
  doi=true
elif [[ "$ret" == '"'"$c_cert"'"' ]]; then
  echo "[-] Certificate code is up to date"
else
  echo "[!] Certificate code is unknown / outdated"
  doi=true
fi

if $doi; then
  echo "[*] Installing certificate code..."
  $tcli call --abi $abi --sign $rkf "$addr" installCertificate '{"code":"'"$c_cert"'"}'
fi

echo "[=] Verifying auction code..."
ret=$($tcli run --abi $abi "$addr" auction_code {} | grep '"auction_code"' | awk '{print $2}')
doi=false
if [[ "$ret" == '"'"$c_empt"'"' ]]; then
  echo "[!] Auction code is not initialized"
  doi=true
elif [[ "$ret" == '"'"$c_auct"'"' ]]; then
  echo "[-] Auction code is up to date"
else
  echo "[!] Auction code is unknown / outdated"
  doi=true
fi

if $doi; then
  echo "[*] Installing auction code..."
  $tcli call --abi $abi --sign $rkf "$addr" installAuction '{"code":"'"$c_auct"'"}'
fi

echo "All done! You are advised to re-run this script again to make sure everything is deployed correctly!"
echo "You also should use deploy_debot.sh to deploy and configure the corresponding debot"