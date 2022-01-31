from AbstLayer import AbstLayer
from Utils import Utils as ut
import unittest

################################
# Tested with tonos-ts4==0.4.1 #
################################


class D4Tests(unittest.TestCase):
    # noinspection PyPep8Naming
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.al = AbstLayer('../out/', ['D4Auct', 'D4Base', 'D4Cert', 'D4Root', 'D4Test', 'D4User'], True)

    def setUp(self):
        al = self.al
        al.reset(True)
        al.deploy_root()
        al.root_install_code_images()
        al.create_users(10)

    def test_initial_balances(self):
        al = self.al
        self.assertEqual(ut.b(al.root), 100)
        for i in range(1, 11):
            self.assertEqual(ut.b(al.tests[i]), 99)
            self.assertEqual(ut.b(al.users[i]), 1)

    def test_auction(self):
        al = self.al

        al.start_auction(1, 'test', 2)
        self.assertEqual(98.1, ut.b(al.tests[1]))

        bids = {1:1, 2:8, 3:2, 4:6, 5:15, 6:13}
        for k in bids:
            al.make_bid(k, 'test', ut.gr(bids[k]))

        self.assertEqual(97.2, ut.b(al.tests[1]))
        self.assertEqual(1.9,  ut.b(al.users[1]))
        for i in range(2, 7):
            self.assertEqual(98.1, ut.b(al.tests[i]))
            self.assertEqual(1.9,  ut.b(al.users[i]))

        al.advance_time(ut.d(14))  # bid -> reveal
        for i in range(1, 6):
            al.reveal_bid(i, 'test')

        for i in range(1, 6):
            self.assertAlmostEqual((97.2 if i == 1 else 98.1) - bids[i] - 1, ut.b(al.tests[i]))
            self.assertAlmostEqual(1.9 + (0 if i == 5 else bids[i]) + 0.9, ut.b(al.users[i]))
            self.assertAlmostEqual(1.8, al.users[i].withdrawable() / ut.gr())

        al.advance_time(ut.d(2))  # reveal -> finalize

        for i in range(1, 5):
            self.assertAlmostEqual(1.8 + (0 if i == 5 else bids[i]), al.users[i].withdrawable() / ut.gr())

        al.finalize_auction(5, 'test')
        self.assertAlmostEqual(ut.b(al.tests[5]), 82.1 - 0.01)
        self.assertAlmostEqual(ut.b(al.users[5]),  9.9 + 0.01)

        cert, cow, cif = al.resolve_cert('test'), al.users[5], al.tests[5]
        self.assertEqual(cert.getOwner(), cow.A_)

        cif.setValue(cert.A_, 0, al.root.A_)
        cif.setValue(cert.A_, 1, cif.A_)
        self.assertEqual(cert.getValue(0), al.root.A_)
        self.assertEqual(cert.getValue(1), cif.A_)

    def test_name_filtering(self):
        al = self.al

        al.start_auction(1, 'test.bad', 3, 183)
        al.start_auction(1, 'test/bad', 3, 182)
        al.start_auction(1, '', 3, 181)

        al.start_auction(1, 'test\nbad', 3, 185)
        al.start_auction(1, 'testэтоbad', 3, 185)


if __name__ == '__main__':
    unittest.main()
