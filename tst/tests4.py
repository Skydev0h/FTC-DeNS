import tonos_ts4.ts4 as ts4, json
from Wrappers import *

eq = ts4.eq
baseTime = 1000000
basePath = '../out/'
codeFormat = basePath + 'D4{0}.tvc'

ts4.set_verbose(True)
ts4.set_tests_path(basePath)
ts4.G_WARN_ON_UNEXPECTED_ANSWERS = True

code = dict()
for i in 'Auct, Base, Cert, Root, User'.split(', '):
    code[i] = ts4.core.load_code_cell(codeFormat.format(i))
    ts4.register_abi('D4' + i)

static_key_pair = ('1b5d84f798478416f9e3c3914d85ffb4659bf28772115240e2b8c98c2caa1154b3982dc3a7ae6132b'
                   '87e974284c3ca6de353a09a1ec63d52d0aba5e6be9ea8b5', '0xb3982dc3a7ae6132b87e974284c3ca6'
                                                                      'de353a09a1ec63d52d0aba5e6be9ea8b5')

def lad(l, n=64, p='', s=''): return ts4.Address('0:' + p + (n * l) + s)

class Root(ts4.BaseContract):
    def __init__(self):
        kp = static_key_pair  # ts4.make_keypair()
        super(Root, self).__init__('D4Root', {}, keypair=kp, nickname='Root',
                                   override_address=lad('a'))

def h(s: str): return s.encode('ASCII').hex()
def seg(s: str): print('\n# ******************************\n# {}\n# ******************************\n'.format(s))
def dm(): ts4.dispatch_messages()
def gr(g: int = 1): return g * ts4.GRAM
def b(acct): return acct.balance / gr() if acct.balance is not None else '-'
def cg(acct, meth): return acct.call_getter(meth)

ts4.core.set_now(baseTime)
nonce = '0x123456789'

seg('Root initialization')
root = Root()
wroot = WrapD4Root(root)

seg('Code installation')
cinst = {
    'Base': 'Base',
    'Cert': 'Certificate',
    'Auct': 'Auction',
    'User': 'User'
}
for i in cinst:
    root.call_method_signed('set' + cinst[i] + 'Code', {'code': code[i]})

seg('Upgrade (setCode)')
wroot.setRootCode(code['Root'], ts4_sign=True)  # root.call_method_signed('setRootCode', {'code': code['Root']})

class Test(ts4.BaseContract):
    def __init__(self, iden='', kp=None):
        sid = str(iden)
        super(Test, self).__init__('D4Test', {'root': root.address}, nickname='Test' + sid.rstrip('0'),
                                   override_address=lad('e', 64 - len(sid), sid))
        self.w = WrapD4Test(self)
        self.w.makeIntUser()
        # noinspection PyTypeChecker
        self.i = ts4.BaseContract('D4User', {}, address=self.call_getter('iaddr'),
                                  nickname='IntUser' + sid.rstrip('0'))
        self.wi = WrapD4User(self.i)
        if kp is not None:
            self.w.makeExtUser(kp[1])
            # noinspection PyTypeChecker
            self.e = ts4.BaseContract('D4User', {}, address=self.call_getter('eaddr'),
                                      nickname='ExtUser' + sid.rstrip('0'), keypair=kp)
            self.we = WrapD4User(self.e)
        self.la = None

    def start_auction(self, name, duration):
        self.w.createAuction(h(name), duration)
        self.la = self.wi.lastCreatedAuction()

    def bid(self, amount, _auct=None):
        la = _auct if _auct is not None else self.la
        ainfo = self.wi.auctInfo()
        if la not in ainfo:
            self.w.queryAuct(la)
            ainfo = self.wi.auctInfo()
        bhash = self.wi.utilBidHash(la, ainfo[la]['startTime'], self.address, amount, nonce)
        self.w.makeBid(la, '00', bhash)

    def rev(self, amount, _auct=None):
        la = _auct if _auct is not None else self.la
        self.w.revealBid(la, amount, nonce)


seg('Create user contracts')
uc, wc = dict(), dict()
for i in range(0, 10):
    uc[i] = Test(str(i) + '000', static_key_pair if i == 0 else None)
    wc[i] = WrapD4Test(uc[i])

test, intUser, wtest, wintUser = uc[0], uc[0].i, wc[0], uc[0].wi

seg('Create auction')
test.start_auction('test', 2)
auct = ts4.BaseContract('D4Auct', {}, address=test.la, nickname='testAuct')
wauct = WrapD4Auct(auct)

seg('Perform bid')
test.bid(gr(10))

seg('And some other bids')
bids = {1:5, 2:8, 3:2, 4:6, 5: 15, 6:13}
for k in bids:
    uc[k].bid(gr(bids[k]), test.la)

ainfo = wintUser.auctInfo()[test.la]

ts4.core.set_now(ainfo['bidEnds'] + 1)

seg('Reveals (time warp)')

def rev(idx):
    seg('Reveal #{}: amount is {}'.format(idx, bids[idx]))
    uc[idx].rev(gr(bids[idx]), test.la)

rev(1)
rev(2)
rev(3)
rev(4)

seg('Finalize')
ts4.core.set_now(ainfo['revEnds'] + 1)
wtest.finalize(test.la)
# test.call_method('finalize', {'auction': test.la})
dm()

certAddr = wroot.resolveFull(1, h('test'))
cert = ts4.BaseContract('D4Cert', {}, address=certAddr, nickname='testCert')
wcert = WrapD4Cert(cert)

wcert.getOwner(0)

seg('Set value')
wc[2].setValue(certAddr, 0, root.address)
wcert.getValue(0)

wc[2].resetValue(certAddr, 0)
wcert.getValue(0, ts4_expect_ec=50)


#
# seg('Find auction')
# auctAddr = root.call_getter('resolveFull', {'_answer_id': 0, 'ct_type': 2, 'fullname': h('test')})
#
# # noinspection PyTypeChecker
# auct = ts4.BaseContract('D4Auct', {}, address=auctAddr, nickname='testAuct')
#
# seg('Query again')
# test.call_method('queryAuct', {'target': auctAddr})
# dm()
#
# seg('Read information')
# auctInfo = intUser.call_getter('auctInfo')
#
# user = intUser.call_getter('st_parent')
# bhash = intUser.call_getter('utilBidHash', {'auction': auctAddr, 'startTime': baseTime,
#                                             'user': user, 'amount': gr(10), 'nonce': nonce})
#
# seg('Bid')
# print('auctBids:', intUser.call_getter('auctBids'));
# test.call_method('makeBid', {'auction': auctAddr, 'data': '00', 'hash': bhash})
# dm()
# print('auctBids:', intUser.call_getter('auctBids'));
#
# seg('Other bids')
#
# print(auctInfo[auctAddr])
