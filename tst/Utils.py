import tonos_ts4.ts4 as ts4
from Wrappers import WrapperParentClass

class Utils:
    shush: bool = False

    @staticmethod
    def silence(shush):
        Utils.shush = shush
        ts4.set_verbose(not shush)

    @staticmethod
    def dboxed(text):
        if Utils.shush: return
        print('')
        print('╔═' + ('═' * len(text)) + '═╗')
        print('║ ' + text + ' ║')
        print('╚═' + ('═' * len(text)) + '═╝')
        print('')

    @staticmethod
    def boxed(text):
        if Utils.shush: return
        print('┌─' + ('─' * len(text)) + '─┐')
        print('│ ' + text + ' │')
        print('└─' + ('─' * len(text)) + '─┘')

    @staticmethod
    def static_keypair():
        return ('1b5d84f798478416f9e3c3914d85ffb4659bf28772115240e2b8c98c2caa1154'
                'b3982dc3a7ae6132b87e974284c3ca6de353a09a1ec63d52d0aba5e6be9ea8b5',
                '0xb3982dc3a7ae6132b87e974284c3ca6de353a09a1ec63d52d0aba5e6be9ea8b5')

    @staticmethod
    def static_privkey():
        return Utils.static_keypair()[0]

    @staticmethod
    def static_pubkey():
        return Utils.static_keypair()[1]

    @staticmethod
    def static_nonce():
        return '0x1234567890ABCDEF'

    @staticmethod
    def address(head):
        return ts4.Address('0:' + head + ('F' * (64 - len(head))))

    @staticmethod
    def hex(s: str):
        return s.encode('ASCII').hex()

    @staticmethod
    def dm(s: str):
        ts4.dispatch_messages()

    @staticmethod
    def gr(g: int = 1):
        return g * ts4.GRAM

    @staticmethod
    def d(d: int = 1):
        return d * 24 * 60 * 60

    @staticmethod
    def b(acct):
        if isinstance(acct, WrapperParentClass):
            return acct.C_.balance / Utils.gr() if acct.C_.balance is not None else '-'
        return acct.balance / Utils.gr() if acct.balance is not None else '-'
