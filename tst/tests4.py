import tonos_ts4.ts4 as ts4, json
from Wrappers import *

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
root = WrapD4Root(Root())

seg('Code installation')
cinst = {
    'Base': 'Base',
    'Cert': 'Certificate',
    'Auct': 'Auction',
    'User': 'User'
}
for i in cinst:
    root.C_.call_method_signed('set' + cinst[i] + 'Code', {'code': code[i]})

seg('Upgrade (setCode)')
root.setRootCode(code['Root'], ts4_sign=True)  # root.call_method_signed('setRootCode', {'code': code['Root']})

seg('Create user contracts')
uc, ui = dict(), dict()
for i in range(0, 10):
    # c = WrapD4Test(Test(str(i) + '000', static_key_pair if i == 0 else None))
    sid = str(i) + '000'
    uc[i] = WrapD4Test(ts4.BaseContract('D4Test', {'root': root.A_}, nickname='Test' + sid.rstrip('0'),
                                        override_address=lad('e', 64 - len(sid), sid)))
    uc[i].makeIntUser()
    ui[i] = WrapD4User(ts4.BaseContract('D4User', {}, address=uc[i].iaddr(), nickname='IntUser' + sid.rstrip('0')))

test, intUser = uc[0], ui[0]

seg('Create auction')
test.createAuction(h('test'), 2)
auct = WrapD4Auct(ts4.BaseContract('D4Auct', {}, address=intUser.lastCreatedAuction(), nickname='testAuct'))

def mkbid(i, amount):
    ainfo = ui[i].auctInfo()
    if auct.A_ not in ainfo:
        uc[i].queryAuct(auct.A_)
        ainfo = ui[i].auctInfo()
    bhash = ui[i].utilBidHash(auct.A_, ainfo[auct.A_]['startTime'], uc[i].A_, amount, nonce)
    uc[i].makeBid(auct.A_, '00', bhash)

seg('Perform bid')
mkbid(0, gr(10))

seg('And some other bids')
bids = {1:5, 2:8, 3:2, 4:6, 5: 15, 6:13}
for k in bids:
    mkbid(k, gr(bids[k]))

ainfo = intUser.auctInfo()[auct.A_]

ts4.core.set_now(ainfo['bidEnds'] + 1)

seg('Reveals (time warp)')

def rev(idx):
    seg('Reveal #{}: amount is {}'.format(idx, bids[idx]))
    uc[idx].revealBid(auct.A_, gr(bids[idx]), nonce)

rev(1), rev(2), rev(3), rev(4)

seg('Finalize')
ts4.core.set_now(ainfo['revEnds'] + 1)
test.finalize(auct.A_)
# test.call_method('finalize', {'auction': test.la})
dm()

certAddr = root.resolveFull(1, h('test'))
cert = WrapD4Cert(ts4.BaseContract('D4Cert', {}, address=certAddr, nickname='testCert'))

cert.getOwner(0)

seg('Set value')
uc[2].setValue(certAddr, 0, root.A_)
cert.getValue(0)

uc[2].resetValue(certAddr, 0)
cert.getValue(0, ts4_expect_ec=50)

ts4.reset_all()

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
