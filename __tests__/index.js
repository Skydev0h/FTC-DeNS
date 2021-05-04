const { Account } = require("@tonclient/appkit");
const { TonClient, signerKeys } = require("@tonclient/core");
const { libNode } = require("@tonclient/lib-node");
const { DensRootContract } = require("../contracts/DensRootContract.js");
const { DensPlatformContract } = require("../contracts/DensPlatformContract.js");
const { DensAuctionContract } = require("../contracts/DensAuctionContract.js");
const { DensCertificateContract } = require("../contracts/DensCertificateContract.js");
const { DensTestContract } = require("../contracts/DensTestContract.js");


TonClient.useBinaryLibrary(libNode);

describe('Start Auction', () => {
    let client, densRootkeys, densRootAcc, densPlatformAcc, densAuctionAcc, densCertificateAcc;

    beforeAll(async function () {
        client = new TonClient({
            network: {
                endpoints: ["http://localhost"]
            }
        });
        densRootkeys = await TonClient.default.crypto.generate_random_sign_keys();
        densRootAcc = new Account(DensRootContract, {
            signer: signerKeys(densRootkeys),
            client,
        });
        densPlatformAcc = new Account(DensPlatformContract, {
            signer: signerKeys(densRootkeys),
            client,
        });

        densAuctionAcc = new Account(DensAuctionContract, {
            signer: signerKeys(densRootkeys),
            client,
        });

        densCertificateAcc = new Account(DensCertificateContract, {
            signer: signerKeys(densRootkeys),
            client,
        });


        const address = await densRootAcc.getAddress();
        console.log(`Future address of the contract will be: ${address}`);
        await densRootAcc.deploy({ useGiver: true });
        console.log(`DensRootAcc contract was deployed at address: ${address}`);

        let response = await densRootAcc.run("installPlatform", {
            code: (await client.boc.get_code_from_tvc({ tvc: DensPlatformContract.tvc })).code
        });

        const platformCodeResult = await densRootAcc.runLocal("platform_code", {});
        expect(platformCodeResult.decoded.output.platform_code).not.toBeNull();


        response = await densRootAcc.run("installCertificate", {
            code: (await client.boc.get_code_from_tvc({ tvc: DensCertificateContract.tvc })).code
        });
        const certificateCodeResult = await densRootAcc.runLocal("certificate_code", {});
        expect(certificateCodeResult.decoded.output.certificate_code).not.toBeNull();


        response = await densRootAcc.run("installAuction", {
            code: (await client.boc.get_code_from_tvc({ tvc: DensAuctionContract.tvc })).code
        });
        const auctionCodeResult = await densRootAcc.runLocal("auction_code", {});
        expect(auctionCodeResult.decoded.output.auction_code).not.toBeNull();

    });

    afterAll(async () => {
        client.close();
    });

    test('Start Aucton. 1 particant', async () => {

    });

});