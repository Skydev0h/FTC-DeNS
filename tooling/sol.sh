#!/bin/bash -eE

cd ../contracts
# solc DensDebot.sol
solc DensRoot.sol
solc DensPlatform.sol
solc DensCertificate.sol
solc DensAuction.sol
solc DensBid.sol
solc DensTest.sol
solc MachineGun.sol
mv ./*.code ../build/
mv ./*.json ../build/
