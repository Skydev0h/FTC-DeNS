from Wrappers import *
from Utils import Utils as U
import tonos_ts4.ts4 as ts4, json

class AbstLayer:

    def __init__(self, base_path: str, preload_contracts: list, silent: bool = False):
        self.base_path = base_path
        self.code = dict()
        self.time = 0
        self.root: WrapD4Root = None
        self.tests: dict[WrapD4Test] = dict()
        self.users: dict[WrapD4User] = dict()
        self.aucts: dict[WrapD4Auct] = dict()
        self.bids:  dict[dict[int]]  = dict()
        self.certs: dict[WrapD4Cert] = dict()
        U.silence(silent)
        U.dboxed('Initializing...')
        ts4.set_verbose(not silent)
        ts4.set_tests_path(base_path)
        ts4.G_WARN_ON_UNEXPECTED_ANSWERS = True
        U.boxed('Preloading contracts...')
        for i in preload_contracts:
            self.code[i] = ts4.load_code_cell(base_path + i)
            ts4.register_abi(i)
        U.boxed('Resetting state...')
        self.reset()

    def reset(self, set_silence: bool = None):
        if set_silence is not None:
            U.silence(set_silence)
        ts4.reset_all()
        self.root = None
        self.tests = dict()
        self.users = dict()
        self.aucts = dict()
        self.bids  = dict()
        self.certs = dict()
        self.set_time(1)

    def set_time(self, time: int):
        self.time = time
        ts4.core.set_now(self.time)

    def advance_time(self, time: int):
        self.time += time
        ts4.core.set_now(self.time)

    def deploy_root(self):
        U.boxed('Deploying root...')
        keypair = U.static_keypair()
        contract = ts4.BaseContract('D4Root', {}, keypair=keypair, nickname='D4Root',
                                    override_address=U.address('0000'))
        self.root = WrapD4Root(contract)
        if not U.shush:
            print('Root deployed at address ' + str(contract.address))

    def root_install_code_images(self):
        c = self.code
        U.boxed('Installing code images to root...')
        self.root.setBaseCode(c['D4Base'], ts4_sign=True)
        self.root.setCertificateCode(c['D4Cert'], ts4_sign=True)
        self.root.setAuctionCode(c['D4Auct'], ts4_sign=True)
        self.root.setUserCode(c['D4User'], ts4_sign=True)

    def create_users(self, count: int = 10):
        U.boxed('Creating ' + str(count) + ' wallets and users...')
        for i in range(1, count+1):
            sid = str(1000 + i)
            c = WrapD4Test(ts4.BaseContract('D4Test', {'root': self.root.A_},
                                            nickname='D4Test_' + sid,
                                            override_address=U.address(sid)))
            self.tests[i] = c
            c.makeIntUser()
            self.users[i] = WrapD4User(ts4.BaseContract('D4User', {},
                                                        address=c.iaddr(),
                                                        nickname='D4User_' + sid))

    def start_auction(self, user_id: int, domain: str, duration: int, msg_ec: int = 0):
        U.boxed('User ' + str(user_id) + 'starting auction for ' + domain + '(' + str(duration) + 'y)')
        if msg_ec != 0:
            WrapperGlobal.auto_dispatch_messages = False
        self.tests[user_id].createAuction(domain, duration)
        if msg_ec != 0:
            WrapperGlobal.auto_dispatch_messages = True
            ts4.dispatch_one_message(msg_ec)
            ts4.dispatch_messages()
        else:
            aa = self.users[user_id].lastCreatedAuction()
            self.aucts[domain] = WrapD4Auct(ts4.BaseContract('D4Auct', {}, address=aa,
                                                             nickname='D4Auct_' + domain))

    def make_bid(self, user_id: int, domain: str, amount: int):
        U.boxed('User ' + str(user_id) + ' signs bid ' + str(amount) + ' for ' + domain)
        ct = self.tests[user_id]
        iu = self.users[user_id]
        ainfo = iu.auctInfo()
        aa = self.aucts[domain].A_
        if aa not in ainfo:
            ct.queryAuct(aa)
            ainfo = iu.auctInfo()
        bhash = iu.utilBidHash(aa, ainfo[aa]['startTime'], ct.A_, amount, U.static_nonce())
        ct.makeBid(aa, '00', bhash)
        if aa not in self.bids:
            self.bids[aa] = dict()
        self.bids[aa][user_id] = amount

    def reveal_bid(self, user_id: int, domain: str):
        aa = self.aucts[domain].A_
        amount = self.bids[aa][user_id]
        U.boxed('User ' + str(user_id) + ' reveals bid ' + str(amount) + ' for ' + domain)
        self.tests[user_id].revealBid(aa, amount, U.static_nonce())

    def finalize_auction(self, user_id: int, domain: str):
        aa = self.aucts[domain].A_
        U.boxed('User ' + str(user_id) + ' finalizes auction for ' + domain)
        self.tests[user_id].finalize(aa)

    def show_balances(self):
        U.boxed('Current balance of accounts:')
        print('Root balance: ' + str(U.b(self.root)))
        for i in self.tests:
            print('Test ' + str(i) + ' balance: ' + str(U.b(self.tests[i])) + ', ' +
                  'user ' + str(i) + ' balance: ' + str(U.b(self.users[i])))
        for i in self.aucts:
            print('Auct ' + i + ' balance: ' + str(U.b(self.aucts[i])))

    def resolve_cert(self, domain: str):
        if domain in self.certs:
            return self.certs[domain]
        ca = self.root.resolveFull(1, domain)
        wc = WrapD4Cert(ts4.BaseContract('D4Cert', {}, address=ca, nickname='D4Cert_' + domain))
        self.certs[domain] = wc
        return wc

    def get_auction(self, domain: str):
        return self.aucts[domain]
