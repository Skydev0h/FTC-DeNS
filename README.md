# FreeTON Contest - Decentralized Name Service
This is an implementation of DeNS elements according to the [contest specification](https://devex.gov.freeton.org/proposal?proposalAddress=0:6f72de4f9e5e04c949d048716e43cc9b6b33f1236dc7ffd3245c676925ce2a07) that is based upon [TIP-2 proposal](https://forum.freeton.org/t/tip-2-decentralized-certificates-decert/7800).

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

## Notice

Because of some bug the contest closes at 18:59 UTC while in the contest specification it should close on 23:59 UTC. Therefore the documentation and repository may still be updated until the end of day GMT.