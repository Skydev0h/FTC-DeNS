import tonos_ts4.ts4 as ts4, json
from Machine import *
from Wrappers import *

mach = Machine('../out/', 'D4Auct D4Base D4Cert D4Root D4Test D4User'.split(' '))

mach.deploy_root()
mach.root_install_code_images()
mach.create_users(6)
mach.show_balances()
mach.start_auction(1, 'test', 2)
mach.show_balances()

Utils.dboxed('Make bids')
bids = {1:5, 2:8, 3:2, 4:6, 5:15, 6:13}
for k in bids:
    mach.make_bid(k, 'test', Utils.gr(bids[k]))
mach.show_balances()

mach.advance_time(Utils.d(14))  # bid -> reveal

Utils.dboxed('Reveal bids')
for i in range(1, 4+1):
    mach.reveal_bid(i, 'test')
mach.show_balances()

mach.advance_time(Utils.d(2))

Utils.dboxed('Finalize auction')
mach.finalize_auction(2, 'test')
mach.show_balances()

cert = mach.resolve_cert('test')
print(cert.getOwner())

mach.tests[2].setValue(cert.A_, 0, mach.root.A_)
print(cert.getValue(0))
