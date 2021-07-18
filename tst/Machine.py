import tonos_ts4.ts4 as ts4, json
from Wrappers import *
from Utils import *

class Machine:

    def __init__(self, base_path: str, preload_contracts: list):
        self.base_path = base_path
        self.code = dict()
        self.time = 0
        self.root: WrapD4Root = None
        self.tests: dict[WrapD4Test] = dict()
        self.users: dict[WrapD4User] = dict()
        self.aucts: dict[WrapD4Auct] = dict()
        self.bids: dict[dict[int]] = dict()
        self.certs: dict[WrapD4Cert] = dict()
        Utils.silence(False)
        Utils.dboxed('Initializing...')
        ts4.set_verbose(True)
        ts4.set_tests_path(base_path)
        ts4.G_WARN_ON_UNEXPECTED_ANSWERS = True
        Utils.boxed('Preloading contracts...')
        for i in preload_contracts:
            self.code[i] = ts4.core.load_code_cell(base_path + i + '.tvc')
            ts4.register_abi(i)
        Utils.boxed('Resetting state...')
        self.reset()

    def reset(self, set_silence: bool = None):
        if set_silence is not None:
            Utils.silence(set_silence)
        ts4.reset_all()
        self.root = None
        self.tests = dict()
        self.users = dict()
        self.aucts = dict()
        self.bids = dict()
        self.certs = dict()
        self.set_time(1)

    def set_time(self, time: int):
        self.time = time
        ts4.core.set_now(self.time)

    def advance_time(self, time: int):
        self.time += time
        ts4.core.set_now(self.time)

    def deploy_root(self):
        Utils.boxed('Deploying root...')
        keypair = Utils.static_keypair()
        contract = ts4.BaseContract('D4Root', {}, keypair=keypair, nickname='D4Root',
                                    override_address=Utils.address('0000'))
        self.root = WrapD4Root(contract)
        print('Root deployed at address ' + str(contract.address))

    def root_install_code_images(self):
        c = self.code
        Utils.boxed('Installing code images to root...')
        self.root.setBaseCode(c['D4Base'], ts4_sign=True)
        self.root.setCertificateCode(c['D4Cert'], ts4_sign=True)
        self.root.setAuctionCode(c['D4Auct'], ts4_sign=True)
        self.root.setUserCode(c['D4User'], ts4_sign=True)

    def create_users(self, count: int = 10):
        Utils.boxed('Creating ' + str(count) + ' wallets and users...')
        for i in range(1, count+1):
            sid = str(1000 + i)
            c = WrapD4Test(ts4.BaseContract('D4Test', {'root': self.root.A_},
                                            nickname='D4Test_' + sid,
                                            override_address=Utils.address(sid)))
            self.tests[i] = c
            c.makeIntUser()
            self.users[i] = WrapD4User(ts4.BaseContract('D4User', {},
                                                        address=c.iaddr(),
                                                        nickname='D4User_' + sid))

    def start_auction(self, user_id: int, domain: str, duration: int):
        Utils.boxed('User ' + str(user_id) + 'starting auction for ' + domain + '(' + str(duration) + 'y)')
        self.tests[user_id].createAuction(Utils.hex(domain), duration)
        aa = self.users[user_id].lastCreatedAuction()
        self.aucts[domain] = WrapD4Auct(ts4.BaseContract('D4Auct', {}, address=aa,
                                                         nickname='D4Auct_' + domain))

    def make_bid(self, user_id: int, domain: str, amount: int):
        Utils.boxed('User ' + str(user_id) + ' signs bid ' + str(amount) + ' for ' + domain)
        ct = self.tests[user_id]
        iu = self.users[user_id]
        ainfo = iu.auctInfo()
        aa = self.aucts[domain].A_
        if aa not in ainfo:
            ct.queryAuct(aa)
            ainfo = iu.auctInfo()
        bhash = iu.utilBidHash(aa, ainfo[aa]['startTime'], ct.A_, amount, Utils.static_nonce())
        ct.makeBid(aa, '00', bhash)
        if aa not in self.bids:
            self.bids[aa] = dict()
        self.bids[aa][user_id] = amount

    def reveal_bid(self, user_id: int, domain: str):
        aa = self.aucts[domain].A_
        amount = self.bids[aa][user_id]
        Utils.boxed('User ' + str(user_id) + ' reveals bid ' + str(amount) + ' for ' + domain)
        self.tests[user_id].revealBid(aa, amount, Utils.static_nonce())

    def finalize_auction(self, user_id: int, domain: str):
        aa = self.aucts[domain].A_
        Utils.boxed('User ' + str(user_id) + ' finalizes auction for ' + domain)
        self.tests[user_id].finalize(aa)

    def show_balances(self):
        Utils.boxed('Current balance of accounts:')
        print('Root balance: ' + str(Utils.b(self.root)))
        for i in self.tests:
            print('Test ' + str(i) + ' balance: ' + str(Utils.b(self.tests[i])) + ', ' +
                  'user ' + str(i) + ' balance: ' + str(Utils.b(self.users[i])))
        for i in self.aucts:
            print('Auct ' + i + ' balance: ' + str(Utils.b(self.aucts[i])))

    def resolve_cert(self, domain: str):
        if domain in self.certs:
            return self.certs[domain]
        ca = self.root.resolveFull(1, Utils.hex(domain))
        wc = WrapD4Cert(ts4.BaseContract('D4Cert', {}, address=ca, nickname='D4Cert_' + domain))
        self.certs[domain] = wc
        return wc

