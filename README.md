# FreeTON Contest - Decentralized Name Service
This is an implementation of DeNS elements according to the [contest specification](https://devex.gov.freeton.org/proposal?proposalAddress=0:6f72de4f9e5e04c949d048716e43cc9b6b33f1236dc7ffd3245c676925ce2a07) that is based upon [TIP-2 proposal](https://forum.freeton.org/t/tip-2-decentralized-certificates-decert/7800).

**Table of contents**

[Summary](#summary)

[Compiling, deploying and running](#compiling-deploying-and-running)



## Summary

The implementation consists of several smart contracts that are responsible for specific area in the system.

### DensRoot

The root smart contract is responsible for keeping and installing code of other components. Also it is the communication nexus that coordinates all other parts - users, debots, certificates and auctions.

### DensPlatform

The platform is the basement for other contracts such as certificates and auctions. Platform has a very small and simple code and is used to deploy contracts at specific places that can be easily precalculated with known data even locally.

### DensCertificate

The certificate is the node and leaf of the DeNS tree. It holds information about pointing to a specific smart contract address that can be retrieved and updated by the certificate owner. Also the certificate can ask root to deploy subcertificates (subdomains) on behalf of the owner.

### DensAuction

The vickrey auction system is used to distribute domains under the root smart contract. It is deployed and destroyed on-demand when needed, holds funds of auction participants and returns them back when auction is complete.

### DensDebot

The debot is used for user interaction with the system elements. Currently it is under development.

---

## Compiling, deploying and running

There are several ways to compile, deploy and run the contracts.

You may not even need to deploy them at all and just use artifacts in the `build` directory.

#### Compiling

In order to just rebuild code from solidity you may use `sol.sh` file. However, it is mostly intended for development. Furthermore, `build.sh` recompiles solidity files and links them to `tvc` files ready for deployment.

#### Deploying

The most convenient way to deploy the root contract is to use `deploy_root.sh` script. It will verify existence of required tools for you and give hints where to get them if they do not exist and do everything required for successful deploy:

* Recompile solidity files (if solc is present)
* Relink deployment tvc files (if tvm_linker is present)
* Ensure existence of root keys and store them and their phrase in files
* Verify state of the contract and give hints what needs to be done
* Deploy the contract to the blockchain
* Verify state of template contract codes (platform, certificate, auction) and update them to the current version

Having done all those actions, the script will provide you with a configured DeNS Root SC in the blockchain.

> N.B. Pay attention to the currently selected network, it depends on your local tonos-cli configuration file.

---

As for the DeBot, you can deploy it using `deploy_debot.sh` script. It also takes care of account state, ABI configuration state and performs the required actions. Having deployed the debot script will run it to test whether it is working or not. 

#### Running

You can always run the debot using `run_debot.sh` script or just by calling `tonos-cli debot fetch <address>` directly.

---

## Interaction

As of now in order to control and interact with the system you need to use `tonos-cli` tool in shell. I have attempted to write a Debot, but due to some bug it fails the way it shouldn't fail (calling `resolveRPC` directly with same parameters on root works, while debot call crashes for some reason).

Deployment of root and configuration of platform, certificate and auction codes is done automatically by `deploy_root.sh` script. Likewise, you can deploy debot with `deploy_debot.sh` and start it later using `run_debot.sh` scripts. Initially, it was planned that contracts would be interacted using debots, however, it turned out that they crash for some reason. Therefore, as of now, interaction can be done directly using `tonos-cli` tool.