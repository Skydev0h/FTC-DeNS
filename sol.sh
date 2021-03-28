#!/bin/bash -eE

cd contracts
solc DensDebot.sol
solc DensRoot.sol
solc DensPlatform.sol
solc DensCertificate.sol
solc DensAuction.sol
solc DensTest.sol
mv ./*.code ../build/
mv ./*.json ../build/

cd ../build
tvm_linker compile DensDebot.code -a DensDebot.abi.json -o DensDebot.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensRoot.code -a DensRoot.abi.json -o DensRoot.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensPlatform.code -a DensPlatform.abi.json -o DensPlatform.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensCertificate.code -a DensCertificate.abi.json -o DensCertificate.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensAuction.code -a DensAuction.abi.json -o DensAuction.tvc --lib stdlib_sol.tvm &
tvm_linker compile DensTest.code -a DensTest.abi.json -o DensTest.tvc --lib stdlib_sol.tvm &
