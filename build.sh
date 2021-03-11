#!/bin/bash -eE

cd build

tvm_linker compile DensRoot.code -a DensRoot.abi.json -o DensRoot.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensPlatform.code -a DensPlatform.abi.json -o DensPlatform.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensCertificate.code -a DensCertificate.abi.json -o DensCertificate.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensAuction.code -a DensAuction.abi.json -o DensAuction.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensTest.code -a DensTest.abi.json -o DensTest.tvc --lib stdlib_sol.tvm &

tvm_linker decode --tvc DensPlatform.tvc > dens_platform.txt
tvm_linker decode --tvc DensCertificate.tvc > dens_certificate.txt
tvm_linker decode --tvc DensAuction.tvc > dens_auction.txt

cat dens_platform.txt | grep 'code:' | cut -d' ' -f3 > code_plat.txt
cat dens_certificate.txt | grep 'code:' | cut -d' ' -f3 > code_cert.txt
cat dens_auction.txt | grep 'code:' | cut -d' ' -f3 > code_auct.txt

tonos-cli genaddr DensRoot.tvc DensRoot.abi.json --setkey ../keys/root.keys.json
