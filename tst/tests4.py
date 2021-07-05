import tonos_ts4.ts4 as ts4, json

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

class Root(ts4.BaseContract):
    def __init__(self):
        kp = static_key_pair  # ts4.make_keypair()
        super(Root, self).__init__('D4Root', {}, keypair=kp, nickname='Root',
                                   override_address=ts4.Address('0:' + (64 * 'a')))

def h(s: str): return s.encode('ASCII').hex()
def seg(s: str): print('#\n# {}\n#'.format(s))
def dm(): ts4.dispatch_messages()
def gr(g: int = 1): return g * ts4.GRAM
def b(acct): return acct.balance / gr() if acct.balance is not None else '-'
def cg(acct, meth): return acct.call_getter(meth)

ts4.core.set_now(baseTime)
nonce = '0x123456789'

seg('Root initialization')
root = Root()

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
root.call_method_signed('setRootCode', {'code': code['Root']})

seg('Create user contracts')
test = ts4.BaseContract('D4Test', {}, nickname='Test', override_address=ts4.Address('0:' + (64 * 'e')))

test.call_method('makeIntUser', {'root': root.address})
dm()

# noinspection PyTypeChecker
intUser = ts4.BaseContract('D4User', {}, address=test.call_getter('addr'), nickname='IntUser')

test.call_method('makeExtUser', {'root': root.address, 'pk': root.keypair[1]})
dm()

# noinspection PyTypeChecker
extUser = ts4.BaseContract('D4User', {}, address=test.call_getter('addr'), nickname='ExtUser', keypair=static_key_pair)

seg('Create auction')
extUser.call_method_signed('createAuction', {'name': h('test'), 'duration': 2})
dm()

# TODO: warning: messages are misordered???

seg('Find auction')
auctAddr = root.call_getter('resolveFull', {'_answer_id': 0, 'ct_type': 2, 'fullname': h('test')})

# noinspection PyTypeChecker
auct = ts4.BaseContract('D4Auct', {}, address=auctAddr, nickname='testAuct')

seg('Query again')
extUser.call_method_signed('queryAuct', {'target': auctAddr})
dm()

seg('Read information')
auctInfo = extUser.call_getter('auctInfo')

user = extUser.call_getter('st_parent')
bhash = extUser.call_getter('utilBidHash', {'auction': auctAddr, 'startTime': baseTime,
                                            'user': user, 'amount': gr(10), 'nonce': nonce})

seg('Bid')
extUser.call_method_signed('makeBid', {'auction': auctAddr, 'data': '', 'hash': bhash})
dm()



