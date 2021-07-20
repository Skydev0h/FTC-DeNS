import tonos_ts4.ts4 as ts4

class WrapperGlobal:
    auto_dispatch_messages: bool = True

class WrapperParentClass:
        def __init__(self):
            self.C_: ts4.BaseContract = None
            self.A_: ts4.Address = None

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4Auct(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def registrationPreflightCallback(self, value0, expiry_, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.registrationPreflightCallback
        :rtype: 
        :param value0: uint128
        :param expiry_: uint32
        """
        if ts4_sign:
            return self.S_registrationPreflightCallback(value0, expiry_, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_registrationPreflightCallback(value0, expiry_, ts4_expect_ec=ts4_expect_ec)

    def G_registrationPreflightCallback(self, value0, expiry_, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.registrationPreflightCallback getter
        :rtype: 
        :param value0: uint128
        :param expiry_: uint32
        """
        return self.C_.call_getter('registrationPreflightCallback', {'value0': value0, 'expiry_': expiry_}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_registrationPreflightCallback(self, value0, expiry_, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.registrationPreflightCallback raw getter
        :rtype: 
        :param value0: uint128
        :param expiry_: uint32
        """
        return self.C_.call_getter_raw('registrationPreflightCallback', {'value0': value0, 'expiry_': expiry_}, expect_ec=ts4_expect_ec)

    def M_registrationPreflightCallback(self, value0, expiry_, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.registrationPreflightCallback method call
        :param value0: uint128
        :param expiry_: uint32
        """
        _r_ = self.C_.call_method('registrationPreflightCallback', {'value0': value0, 'expiry_': expiry_}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_registrationPreflightCallback(self, value0, expiry_, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.registrationPreflightCallback signed method call
        :param value0: uint128
        :param expiry_: uint32
        """
        _r_ = self.C_.call_method_signed('registrationPreflightCallback', {'value0': value0, 'expiry_': expiry_}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getInfo(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.getInfo
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.G_getInfo(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getInfo(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.getInfo getter
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getInfo', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getInfo(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.getInfo raw getter
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getInfo', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getInfo(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.getInfo method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getInfo', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getInfo(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.getInfo signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getInfo', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def commit(self, result, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.commit
        :rtype: 
        :param result: bool
        """
        if ts4_sign:
            return self.S_commit(result, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_commit(result, ts4_expect_ec=ts4_expect_ec)

    def G_commit(self, result, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.commit getter
        :rtype: 
        :param result: bool
        """
        return self.C_.call_getter('commit', {'result': result}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_commit(self, result, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.commit raw getter
        :rtype: 
        :param result: bool
        """
        return self.C_.call_getter_raw('commit', {'result': result}, expect_ec=ts4_expect_ec)

    def M_commit(self, result, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.commit method call
        :param result: bool
        """
        _r_ = self.C_.call_method('commit', {'result': result}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_commit(self, result, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.commit signed method call
        :param result: bool
        """
        _r_ = self.C_.call_method_signed('commit', {'result': result}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def accountBid(self, user, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.accountBid
        :rtype: 
        :param user: address
        """
        if ts4_sign:
            return self.S_accountBid(user, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_accountBid(user, ts4_expect_ec=ts4_expect_ec)

    def G_accountBid(self, user, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.accountBid getter
        :rtype: 
        :param user: address
        """
        return self.C_.call_getter('accountBid', {'user': user}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_accountBid(self, user, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.accountBid raw getter
        :rtype: 
        :param user: address
        """
        return self.C_.call_getter_raw('accountBid', {'user': user}, expect_ec=ts4_expect_ec)

    def M_accountBid(self, user, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.accountBid method call
        :param user: address
        """
        _r_ = self.C_.call_method('accountBid', {'user': user}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_accountBid(self, user, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.accountBid signed method call
        :param user: address
        """
        _r_ = self.C_.call_method_signed('accountBid', {'user': user}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def revealBid(self, user, bid_time, amount, nonce, prover, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.revealBid
        :rtype: 
        :param user: address
        :param bid_time: uint32
        :param amount: uint128
        :param nonce: uint128
        :param prover: uint256
        """
        if ts4_sign:
            return self.S_revealBid(user, bid_time, amount, nonce, prover, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_revealBid(user, bid_time, amount, nonce, prover, ts4_expect_ec=ts4_expect_ec)

    def G_revealBid(self, user, bid_time, amount, nonce, prover, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.revealBid getter
        :rtype: 
        :param user: address
        :param bid_time: uint32
        :param amount: uint128
        :param nonce: uint128
        :param prover: uint256
        """
        return self.C_.call_getter('revealBid', {'user': user, 'bid_time': bid_time, 'amount': amount, 'nonce': nonce, 'prover': prover}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_revealBid(self, user, bid_time, amount, nonce, prover, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revealBid raw getter
        :rtype: 
        :param user: address
        :param bid_time: uint32
        :param amount: uint128
        :param nonce: uint128
        :param prover: uint256
        """
        return self.C_.call_getter_raw('revealBid', {'user': user, 'bid_time': bid_time, 'amount': amount, 'nonce': nonce, 'prover': prover}, expect_ec=ts4_expect_ec)

    def M_revealBid(self, user, bid_time, amount, nonce, prover, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.revealBid method call
        :param user: address
        :param bid_time: uint32
        :param amount: uint128
        :param nonce: uint128
        :param prover: uint256
        """
        _r_ = self.C_.call_method('revealBid', {'user': user, 'bid_time': bid_time, 'amount': amount, 'nonce': nonce, 'prover': prover}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_revealBid(self, user, bid_time, amount, nonce, prover, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revealBid signed method call
        :param user: address
        :param bid_time: uint32
        :param amount: uint128
        :param nonce: uint128
        :param prover: uint256
        """
        _r_ = self.C_.call_method_signed('revealBid', {'user': user, 'bid_time': bid_time, 'amount': amount, 'nonce': nonce, 'prover': prover}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requiredAmountForProlong(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.requiredAmountForProlong
        :rtype: uint128
        :param _answer_id: uint32
        """
        return self.G_requiredAmountForProlong(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_requiredAmountForProlong(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.requiredAmountForProlong getter
        :rtype: uint128
        :param _answer_id: uint32
        """
        return self.C_.call_getter('requiredAmountForProlong', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requiredAmountForProlong(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.requiredAmountForProlong raw getter
        :rtype: uint128
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('requiredAmountForProlong', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_requiredAmountForProlong(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.requiredAmountForProlong method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('requiredAmountForProlong', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requiredAmountForProlong(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.requiredAmountForProlong signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('requiredAmountForProlong', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def prolong(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.prolong
        :rtype: 
        """
        if ts4_sign:
            return self.S_prolong(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_prolong(ts4_expect_ec=ts4_expect_ec)

    def G_prolong(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.prolong getter
        :rtype: 
        """
        return self.C_.call_getter('prolong', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_prolong(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.prolong raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('prolong', {}, expect_ec=ts4_expect_ec)

    def M_prolong(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.prolong method call
        """
        _r_ = self.C_.call_method('prolong', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_prolong(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.prolong signed method call
        """
        _r_ = self.C_.call_method_signed('prolong', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def finalize(self, user, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.finalize
        :rtype: 
        :param user: address
        """
        if ts4_sign:
            return self.S_finalize(user, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_finalize(user, ts4_expect_ec=ts4_expect_ec)

    def G_finalize(self, user, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.finalize getter
        :rtype: 
        :param user: address
        """
        return self.C_.call_getter('finalize', {'user': user}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_finalize(self, user, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.finalize raw getter
        :rtype: 
        :param user: address
        """
        return self.C_.call_getter_raw('finalize', {'user': user}, expect_ec=ts4_expect_ec)

    def M_finalize(self, user, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.finalize method call
        :param user: address
        """
        _r_ = self.C_.call_method('finalize', {'user': user}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_finalize(self, user, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.finalize signed method call
        :param user: address
        """
        _r_ = self.C_.call_method_signed('finalize', {'user': user}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def applyAuctionCallback(self, success, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.applyAuctionCallback
        :rtype: 
        :param success: bool
        """
        if ts4_sign:
            return self.S_applyAuctionCallback(success, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_applyAuctionCallback(success, ts4_expect_ec=ts4_expect_ec)

    def G_applyAuctionCallback(self, success, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.applyAuctionCallback getter
        :rtype: 
        :param success: bool
        """
        return self.C_.call_getter('applyAuctionCallback', {'success': success}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_applyAuctionCallback(self, success, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.applyAuctionCallback raw getter
        :rtype: 
        :param success: bool
        """
        return self.C_.call_getter_raw('applyAuctionCallback', {'success': success}, expect_ec=ts4_expect_ec)

    def M_applyAuctionCallback(self, success, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.applyAuctionCallback method call
        :param success: bool
        """
        _r_ = self.C_.call_method('applyAuctionCallback', {'success': success}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_applyAuctionCallback(self, success, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.applyAuctionCallback signed method call
        :param success: bool
        """
        _r_ = self.C_.call_method_signed('applyAuctionCallback', {'success': success}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def sink(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.sink
        :rtype: 
        """
        if ts4_sign:
            return self.S_sink(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_sink(ts4_expect_ec=ts4_expect_ec)

    def G_sink(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.sink getter
        :rtype: 
        """
        return self.C_.call_getter('sink', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.sink raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('sink', {}, expect_ec=ts4_expect_ec)

    def M_sink(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.sink method call
        """
        _r_ = self.C_.call_method('sink', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.sink signed method call
        """
        _r_ = self.C_.call_method_signed('sink', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.st_root
        :rtype: address
        """
        return self.G_st_root(ts4_expect_ec=ts4_expect_ec)

    def G_st_root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.st_root getter
        :rtype: address
        """
        return self.C_.call_getter('st_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_root', {}, expect_ec=ts4_expect_ec)

    def M_st_root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.st_root method call
        """
        _r_ = self.C_.call_method('st_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_root signed method call
        """
        _r_ = self.C_.call_method_signed('st_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_type(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.st_type
        :rtype: uint8
        """
        return self.G_st_type(ts4_expect_ec=ts4_expect_ec)

    def G_st_type(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.st_type getter
        :rtype: uint8
        """
        return self.C_.call_getter('st_type', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_type raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('st_type', {}, expect_ec=ts4_expect_ec)

    def M_st_type(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.st_type method call
        """
        _r_ = self.C_.call_method('st_type', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_type signed method call
        """
        _r_ = self.C_.call_method_signed('st_type', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_name(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.st_name
        :rtype: bytes
        """
        return self.G_st_name(ts4_expect_ec=ts4_expect_ec)

    def G_st_name(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.st_name getter
        :rtype: bytes
        """
        return self.C_.call_getter('st_name', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_name raw getter
        :rtype: bytes
        """
        return self.C_.call_getter_raw('st_name', {}, expect_ec=ts4_expect_ec)

    def M_st_name(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.st_name method call
        """
        _r_ = self.C_.call_method('st_name', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_name signed method call
        """
        _r_ = self.C_.call_method_signed('st_name', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_parent(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.st_parent
        :rtype: address
        """
        return self.G_st_parent(ts4_expect_ec=ts4_expect_ec)

    def G_st_parent(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.st_parent getter
        :rtype: address
        """
        return self.C_.call_getter('st_parent', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_parent raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_parent', {}, expect_ec=ts4_expect_ec)

    def M_st_parent(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.st_parent method call
        """
        _r_ = self.C_.call_method('st_parent', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.st_parent signed method call
        """
        _r_ = self.C_.call_method_signed('st_parent', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.base_code
        :rtype: cell
        """
        return self.G_base_code(ts4_expect_ec=ts4_expect_ec)

    def G_base_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.base_code getter
        :rtype: cell
        """
        return self.C_.call_getter('base_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.base_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('base_code', {}, expect_ec=ts4_expect_ec)

    def M_base_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.base_code method call
        """
        _r_ = self.C_.call_method('base_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.base_code signed method call
        """
        _r_ = self.C_.call_method_signed('base_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_version(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.m_version
        :rtype: uint16
        """
        return self.G_m_version(ts4_expect_ec=ts4_expect_ec)

    def G_m_version(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.m_version getter
        :rtype: uint16
        """
        return self.C_.call_getter('m_version', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.m_version raw getter
        :rtype: uint16
        """
        return self.C_.call_getter_raw('m_version', {}, expect_ec=ts4_expect_ec)

    def M_m_version(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.m_version method call
        """
        _r_ = self.C_.call_method('m_version', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.m_version signed method call
        """
        _r_ = self.C_.call_method_signed('m_version', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.m_revision
        :rtype: uint32
        """
        return self.G_m_revision(ts4_expect_ec=ts4_expect_ec)

    def G_m_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.m_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('m_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.m_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('m_revision', {}, expect_ec=ts4_expect_ec)

    def M_m_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.m_revision method call
        """
        _r_ = self.C_.call_method('m_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.m_revision signed method call
        """
        _r_ = self.C_.call_method_signed('m_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def startTime(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.startTime
        :rtype: uint32
        """
        return self.G_startTime(ts4_expect_ec=ts4_expect_ec)

    def G_startTime(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.startTime getter
        :rtype: uint32
        """
        return self.C_.call_getter('startTime', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_startTime(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.startTime raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('startTime', {}, expect_ec=ts4_expect_ec)

    def M_startTime(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.startTime method call
        """
        _r_ = self.C_.call_method('startTime', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_startTime(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.startTime signed method call
        """
        _r_ = self.C_.call_method_signed('startTime', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def bidEnds(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.bidEnds
        :rtype: uint32
        """
        return self.G_bidEnds(ts4_expect_ec=ts4_expect_ec)

    def G_bidEnds(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.bidEnds getter
        :rtype: uint32
        """
        return self.C_.call_getter('bidEnds', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_bidEnds(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.bidEnds raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('bidEnds', {}, expect_ec=ts4_expect_ec)

    def M_bidEnds(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.bidEnds method call
        """
        _r_ = self.C_.call_method('bidEnds', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_bidEnds(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.bidEnds signed method call
        """
        _r_ = self.C_.call_method_signed('bidEnds', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def revEnds(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.revEnds
        :rtype: uint32
        """
        return self.G_revEnds(ts4_expect_ec=ts4_expect_ec)

    def G_revEnds(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.revEnds getter
        :rtype: uint32
        """
        return self.C_.call_getter('revEnds', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_revEnds(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revEnds raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('revEnds', {}, expect_ec=ts4_expect_ec)

    def M_revEnds(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.revEnds method call
        """
        _r_ = self.C_.call_method('revEnds', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_revEnds(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revEnds signed method call
        """
        _r_ = self.C_.call_method_signed('revEnds', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def durationYears(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.durationYears
        :rtype: uint8
        """
        return self.G_durationYears(ts4_expect_ec=ts4_expect_ec)

    def G_durationYears(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.durationYears getter
        :rtype: uint8
        """
        return self.C_.call_getter('durationYears', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_durationYears(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.durationYears raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('durationYears', {}, expect_ec=ts4_expect_ec)

    def M_durationYears(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.durationYears method call
        """
        _r_ = self.C_.call_method('durationYears', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_durationYears(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.durationYears signed method call
        """
        _r_ = self.C_.call_method_signed('durationYears', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def expiryBase(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.expiryBase
        :rtype: uint32
        """
        return self.G_expiryBase(ts4_expect_ec=ts4_expect_ec)

    def G_expiryBase(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.expiryBase getter
        :rtype: uint32
        """
        return self.C_.call_getter('expiryBase', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_expiryBase(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.expiryBase raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('expiryBase', {}, expect_ec=ts4_expect_ec)

    def M_expiryBase(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.expiryBase method call
        """
        _r_ = self.C_.call_method('expiryBase', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_expiryBase(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.expiryBase signed method call
        """
        _r_ = self.C_.call_method_signed('expiryBase', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def expiryTarget(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.expiryTarget
        :rtype: uint32
        """
        return self.G_expiryTarget(ts4_expect_ec=ts4_expect_ec)

    def G_expiryTarget(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.expiryTarget getter
        :rtype: uint32
        """
        return self.C_.call_getter('expiryTarget', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_expiryTarget(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.expiryTarget raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('expiryTarget', {}, expect_ec=ts4_expect_ec)

    def M_expiryTarget(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.expiryTarget method call
        """
        _r_ = self.C_.call_method('expiryTarget', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_expiryTarget(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.expiryTarget signed method call
        """
        _r_ = self.C_.call_method_signed('expiryTarget', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def finalizeAfter(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.finalizeAfter
        :rtype: uint32
        """
        return self.G_finalizeAfter(ts4_expect_ec=ts4_expect_ec)

    def G_finalizeAfter(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.finalizeAfter getter
        :rtype: uint32
        """
        return self.C_.call_getter('finalizeAfter', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_finalizeAfter(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.finalizeAfter raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('finalizeAfter', {}, expect_ec=ts4_expect_ec)

    def M_finalizeAfter(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.finalizeAfter method call
        """
        _r_ = self.C_.call_method('finalizeAfter', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_finalizeAfter(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.finalizeAfter signed method call
        """
        _r_ = self.C_.call_method_signed('finalizeAfter', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def instigator(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.instigator
        :rtype: address
        """
        return self.G_instigator(ts4_expect_ec=ts4_expect_ec)

    def G_instigator(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.instigator getter
        :rtype: address
        """
        return self.C_.call_getter('instigator', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_instigator(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.instigator raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('instigator', {}, expect_ec=ts4_expect_ec)

    def M_instigator(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.instigator method call
        """
        _r_ = self.C_.call_method('instigator', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_instigator(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.instigator signed method call
        """
        _r_ = self.C_.call_method_signed('instigator', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def bids(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.bids
        :rtype: uint32
        """
        return self.G_bids(ts4_expect_ec=ts4_expect_ec)

    def G_bids(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.bids getter
        :rtype: uint32
        """
        return self.C_.call_getter('bids', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_bids(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.bids raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('bids', {}, expect_ec=ts4_expect_ec)

    def M_bids(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.bids method call
        """
        _r_ = self.C_.call_method('bids', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_bids(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.bids signed method call
        """
        _r_ = self.C_.call_method_signed('bids', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def revs(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.revs
        :rtype: uint32
        """
        return self.G_revs(ts4_expect_ec=ts4_expect_ec)

    def G_revs(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.revs getter
        :rtype: uint32
        """
        return self.C_.call_getter('revs', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_revs(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revs raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('revs', {}, expect_ec=ts4_expect_ec)

    def M_revs(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.revs method call
        """
        _r_ = self.C_.call_method('revs', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_revs(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.revs signed method call
        """
        _r_ = self.C_.call_method_signed('revs', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def top1(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.top1
        :rtype: address
        """
        return self.G_top1(ts4_expect_ec=ts4_expect_ec)

    def G_top1(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.top1 getter
        :rtype: address
        """
        return self.C_.call_getter('top1', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_top1(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.top1 raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('top1', {}, expect_ec=ts4_expect_ec)

    def M_top1(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.top1 method call
        """
        _r_ = self.C_.call_method('top1', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_top1(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.top1 signed method call
        """
        _r_ = self.C_.call_method_signed('top1', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def amt1(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.amt1
        :rtype: uint128
        """
        return self.G_amt1(ts4_expect_ec=ts4_expect_ec)

    def G_amt1(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.amt1 getter
        :rtype: uint128
        """
        return self.C_.call_getter('amt1', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_amt1(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.amt1 raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('amt1', {}, expect_ec=ts4_expect_ec)

    def M_amt1(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.amt1 method call
        """
        _r_ = self.C_.call_method('amt1', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_amt1(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.amt1 signed method call
        """
        _r_ = self.C_.call_method_signed('amt1', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def top2(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.top2
        :rtype: address
        """
        return self.G_top2(ts4_expect_ec=ts4_expect_ec)

    def G_top2(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.top2 getter
        :rtype: address
        """
        return self.C_.call_getter('top2', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_top2(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.top2 raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('top2', {}, expect_ec=ts4_expect_ec)

    def M_top2(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.top2 method call
        """
        _r_ = self.C_.call_method('top2', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_top2(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.top2 signed method call
        """
        _r_ = self.C_.call_method_signed('top2', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def amt2(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Auct.amt2
        :rtype: uint128
        """
        return self.G_amt2(ts4_expect_ec=ts4_expect_ec)

    def G_amt2(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Auct.amt2 getter
        :rtype: uint128
        """
        return self.C_.call_getter('amt2', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_amt2(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.amt2 raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('amt2', {}, expect_ec=ts4_expect_ec)

    def M_amt2(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Auct.amt2 method call
        """
        _r_ = self.C_.call_method('amt2', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_amt2(self, ts4_expect_ec=0):
        """
        Wrapper for D4Auct.amt2 signed method call
        """
        _r_ = self.C_.call_method_signed('amt2', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4Base(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, code, revision, param, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.constructor
        :rtype: 
        :param code: cell
        :param revision: uint32
        :param param: cell
        """
        if ts4_sign:
            return self.S_constructor(code, revision, param, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(code, revision, param, ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, code, revision, param, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.constructor getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        :param param: cell
        """
        return self.C_.call_getter('constructor', {'code': code, 'revision': revision, 'param': param}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, code, revision, param, ts4_expect_ec=0):
        """
        Wrapper for D4Base.constructor raw getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        :param param: cell
        """
        return self.C_.call_getter_raw('constructor', {'code': code, 'revision': revision, 'param': param}, expect_ec=ts4_expect_ec)

    def M_constructor(self, code, revision, param, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.constructor method call
        :param code: cell
        :param revision: uint32
        :param param: cell
        """
        _r_ = self.C_.call_method('constructor', {'code': code, 'revision': revision, 'param': param}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, code, revision, param, ts4_expect_ec=0):
        """
        Wrapper for D4Base.constructor signed method call
        :param code: cell
        :param revision: uint32
        :param param: cell
        """
        _r_ = self.C_.call_method_signed('constructor', {'code': code, 'revision': revision, 'param': param}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.registrationPreflight
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.G_registrationPreflight(requestId, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_registrationPreflight(self, requestId, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.registrationPreflight getter
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.C_.call_getter('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Base.registrationPreflight raw getter
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.C_.call_getter_raw('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, expect_ec=ts4_expect_ec)

    def M_registrationPreflight(self, requestId, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.registrationPreflight method call
        :param _answer_id: uint32
        :param requestId: uint128
        """
        _r_ = self.C_.call_method('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Base.registrationPreflight signed method call
        :param _answer_id: uint32
        :param requestId: uint128
        """
        _r_ = self.C_.call_method_signed('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def destroy(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.destroy
        :rtype: 
        """
        if ts4_sign:
            return self.S_destroy(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_destroy(ts4_expect_ec=ts4_expect_ec)

    def G_destroy(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.destroy getter
        :rtype: 
        """
        return self.C_.call_getter('destroy', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_destroy(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.destroy raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('destroy', {}, expect_ec=ts4_expect_ec)

    def M_destroy(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.destroy method call
        """
        _r_ = self.C_.call_method('destroy', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_destroy(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.destroy signed method call
        """
        _r_ = self.C_.call_method_signed('destroy', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.st_root
        :rtype: address
        """
        return self.G_st_root(ts4_expect_ec=ts4_expect_ec)

    def G_st_root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.st_root getter
        :rtype: address
        """
        return self.C_.call_getter('st_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_root', {}, expect_ec=ts4_expect_ec)

    def M_st_root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.st_root method call
        """
        _r_ = self.C_.call_method('st_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_root signed method call
        """
        _r_ = self.C_.call_method_signed('st_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_type(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.st_type
        :rtype: uint8
        """
        return self.G_st_type(ts4_expect_ec=ts4_expect_ec)

    def G_st_type(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.st_type getter
        :rtype: uint8
        """
        return self.C_.call_getter('st_type', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_type raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('st_type', {}, expect_ec=ts4_expect_ec)

    def M_st_type(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.st_type method call
        """
        _r_ = self.C_.call_method('st_type', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_type signed method call
        """
        _r_ = self.C_.call_method_signed('st_type', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_name(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.st_name
        :rtype: bytes
        """
        return self.G_st_name(ts4_expect_ec=ts4_expect_ec)

    def G_st_name(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.st_name getter
        :rtype: bytes
        """
        return self.C_.call_getter('st_name', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_name raw getter
        :rtype: bytes
        """
        return self.C_.call_getter_raw('st_name', {}, expect_ec=ts4_expect_ec)

    def M_st_name(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.st_name method call
        """
        _r_ = self.C_.call_method('st_name', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_name signed method call
        """
        _r_ = self.C_.call_method_signed('st_name', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_parent(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.st_parent
        :rtype: address
        """
        return self.G_st_parent(ts4_expect_ec=ts4_expect_ec)

    def G_st_parent(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.st_parent getter
        :rtype: address
        """
        return self.C_.call_getter('st_parent', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_parent raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_parent', {}, expect_ec=ts4_expect_ec)

    def M_st_parent(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.st_parent method call
        """
        _r_ = self.C_.call_method('st_parent', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.st_parent signed method call
        """
        _r_ = self.C_.call_method_signed('st_parent', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.base_code
        :rtype: cell
        """
        return self.G_base_code(ts4_expect_ec=ts4_expect_ec)

    def G_base_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.base_code getter
        :rtype: cell
        """
        return self.C_.call_getter('base_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.base_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('base_code', {}, expect_ec=ts4_expect_ec)

    def M_base_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.base_code method call
        """
        _r_ = self.C_.call_method('base_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.base_code signed method call
        """
        _r_ = self.C_.call_method_signed('base_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_version(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.m_version
        :rtype: uint16
        """
        return self.G_m_version(ts4_expect_ec=ts4_expect_ec)

    def G_m_version(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.m_version getter
        :rtype: uint16
        """
        return self.C_.call_getter('m_version', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.m_version raw getter
        :rtype: uint16
        """
        return self.C_.call_getter_raw('m_version', {}, expect_ec=ts4_expect_ec)

    def M_m_version(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.m_version method call
        """
        _r_ = self.C_.call_method('m_version', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.m_version signed method call
        """
        _r_ = self.C_.call_method_signed('m_version', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Base.m_revision
        :rtype: uint32
        """
        return self.G_m_revision(ts4_expect_ec=ts4_expect_ec)

    def G_m_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Base.m_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('m_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.m_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('m_revision', {}, expect_ec=ts4_expect_ec)

    def M_m_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Base.m_revision method call
        """
        _r_ = self.C_.call_method('m_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Base.m_revision signed method call
        """
        _r_ = self.C_.call_method_signed('m_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4Cert(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestUpgrade(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.requestUpgrade
        :rtype: 
        """
        if ts4_sign:
            return self.S_requestUpgrade(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestUpgrade(ts4_expect_ec=ts4_expect_ec)

    def G_requestUpgrade(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.requestUpgrade getter
        :rtype: 
        """
        return self.C_.call_getter('requestUpgrade', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.requestUpgrade raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('requestUpgrade', {}, expect_ec=ts4_expect_ec)

    def M_requestUpgrade(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.requestUpgrade method call
        """
        _r_ = self.C_.call_method('requestUpgrade', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.requestUpgrade signed method call
        """
        _r_ = self.C_.call_method_signed('requestUpgrade', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgrade(self, code, revision, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.upgrade
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        if ts4_sign:
            return self.S_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)

    def G_upgrade(self, code, revision, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.upgrade getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter('upgrade', {'code': code, 'revision': revision}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.upgrade raw getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter_raw('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)

    def M_upgrade(self, code, revision, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.upgrade method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method('upgrade', {'code': code, 'revision': revision}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.upgrade signed method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method_signed('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgradeNotNeeded(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.upgradeNotNeeded
        :rtype: 
        """
        if ts4_sign:
            return self.S_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)

    def G_upgradeNotNeeded(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.upgradeNotNeeded getter
        :rtype: 
        """
        return self.C_.call_getter('upgradeNotNeeded', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.upgradeNotNeeded raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)

    def M_upgradeNotNeeded(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.upgradeNotNeeded method call
        """
        _r_ = self.C_.call_method('upgradeNotNeeded', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.upgradeNotNeeded signed method call
        """
        _r_ = self.C_.call_method_signed('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getInfo(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.getInfo
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.G_getInfo(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getInfo(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.getInfo getter
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getInfo', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getInfo(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getInfo raw getter
        :rtype: tuple
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getInfo', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getInfo(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.getInfo method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getInfo', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getInfo(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getInfo signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getInfo', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getValue(self, index, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.getValue
        :rtype: address
        :param _answer_id: uint32
        :param index: int16
        """
        return self.G_getValue(index, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getValue(self, index, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.getValue getter
        :rtype: address
        :param _answer_id: uint32
        :param index: int16
        """
        return self.C_.call_getter('getValue', {'_answer_id': _answer_id, 'index': index}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getValue(self, index, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getValue raw getter
        :rtype: address
        :param _answer_id: uint32
        :param index: int16
        """
        return self.C_.call_getter_raw('getValue', {'_answer_id': _answer_id, 'index': index}, expect_ec=ts4_expect_ec)

    def M_getValue(self, index, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.getValue method call
        :param _answer_id: uint32
        :param index: int16
        """
        _r_ = self.C_.call_method('getValue', {'_answer_id': _answer_id, 'index': index}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getValue(self, index, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getValue signed method call
        :param _answer_id: uint32
        :param index: int16
        """
        _r_ = self.C_.call_method_signed('getValue', {'_answer_id': _answer_id, 'index': index}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setValue(self, index, new_value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.setValue
        :rtype: 
        :param index: int16
        :param new_value: address
        """
        if ts4_sign:
            return self.S_setValue(index, new_value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setValue(index, new_value, ts4_expect_ec=ts4_expect_ec)

    def G_setValue(self, index, new_value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.setValue getter
        :rtype: 
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter('setValue', {'index': index, 'new_value': new_value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setValue(self, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.setValue raw getter
        :rtype: 
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter_raw('setValue', {'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)

    def M_setValue(self, index, new_value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.setValue method call
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method('setValue', {'index': index, 'new_value': new_value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setValue(self, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.setValue signed method call
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method_signed('setValue', {'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resetValue(self, index, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.resetValue
        :rtype: 
        :param index: int16
        """
        if ts4_sign:
            return self.S_resetValue(index, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_resetValue(index, ts4_expect_ec=ts4_expect_ec)

    def G_resetValue(self, index, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.resetValue getter
        :rtype: 
        :param index: int16
        """
        return self.C_.call_getter('resetValue', {'index': index}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resetValue(self, index, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.resetValue raw getter
        :rtype: 
        :param index: int16
        """
        return self.C_.call_getter_raw('resetValue', {'index': index}, expect_ec=ts4_expect_ec)

    def M_resetValue(self, index, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.resetValue method call
        :param index: int16
        """
        _r_ = self.C_.call_method('resetValue', {'index': index}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resetValue(self, index, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.resetValue signed method call
        :param index: int16
        """
        _r_ = self.C_.call_method_signed('resetValue', {'index': index}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def clearValues(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.clearValues
        :rtype: 
        """
        if ts4_sign:
            return self.S_clearValues(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_clearValues(ts4_expect_ec=ts4_expect_ec)

    def G_clearValues(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.clearValues getter
        :rtype: 
        """
        return self.C_.call_getter('clearValues', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_clearValues(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.clearValues raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('clearValues', {}, expect_ec=ts4_expect_ec)

    def M_clearValues(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.clearValues method call
        """
        _r_ = self.C_.call_method('clearValues', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_clearValues(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.clearValues signed method call
        """
        _r_ = self.C_.call_method_signed('clearValues', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.registrationPreflight
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.G_registrationPreflight(requestId, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_registrationPreflight(self, requestId, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.registrationPreflight getter
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.C_.call_getter('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.registrationPreflight raw getter
        :rtype: uint128, uint32
        :param _answer_id: uint32
        :param requestId: uint128
        """
        return self.C_.call_getter_raw('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, expect_ec=ts4_expect_ec)

    def M_registrationPreflight(self, requestId, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.registrationPreflight method call
        :param _answer_id: uint32
        :param requestId: uint128
        """
        _r_ = self.C_.call_method('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_registrationPreflight(self, requestId, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.registrationPreflight signed method call
        :param _answer_id: uint32
        :param requestId: uint128
        """
        _r_ = self.C_.call_method_signed('registrationPreflight', {'_answer_id': _answer_id, 'requestId': requestId}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def applyAuctionResult(self, new_owner, new_expiry, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.applyAuctionResult
        :rtype: bool
        :param _answer_id: uint32
        :param new_owner: address
        :param new_expiry: uint32
        """
        return self.G_applyAuctionResult(new_owner, new_expiry, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_applyAuctionResult(self, new_owner, new_expiry, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.applyAuctionResult getter
        :rtype: bool
        :param _answer_id: uint32
        :param new_owner: address
        :param new_expiry: uint32
        """
        return self.C_.call_getter('applyAuctionResult', {'_answer_id': _answer_id, 'new_owner': new_owner, 'new_expiry': new_expiry}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_applyAuctionResult(self, new_owner, new_expiry, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.applyAuctionResult raw getter
        :rtype: bool
        :param _answer_id: uint32
        :param new_owner: address
        :param new_expiry: uint32
        """
        return self.C_.call_getter_raw('applyAuctionResult', {'_answer_id': _answer_id, 'new_owner': new_owner, 'new_expiry': new_expiry}, expect_ec=ts4_expect_ec)

    def M_applyAuctionResult(self, new_owner, new_expiry, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.applyAuctionResult method call
        :param _answer_id: uint32
        :param new_owner: address
        :param new_expiry: uint32
        """
        _r_ = self.C_.call_method('applyAuctionResult', {'_answer_id': _answer_id, 'new_owner': new_owner, 'new_expiry': new_expiry}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_applyAuctionResult(self, new_owner, new_expiry, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.applyAuctionResult signed method call
        :param _answer_id: uint32
        :param new_owner: address
        :param new_expiry: uint32
        """
        _r_ = self.C_.call_method_signed('applyAuctionResult', {'_answer_id': _answer_id, 'new_owner': new_owner, 'new_expiry': new_expiry}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def ensureExpiry(self, expiry, retval, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.ensureExpiry
        :rtype: 
        :param expiry: uint32
        :param retval: bool
        """
        if ts4_sign:
            return self.S_ensureExpiry(expiry, retval, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_ensureExpiry(expiry, retval, ts4_expect_ec=ts4_expect_ec)

    def G_ensureExpiry(self, expiry, retval, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.ensureExpiry getter
        :rtype: 
        :param expiry: uint32
        :param retval: bool
        """
        return self.C_.call_getter('ensureExpiry', {'expiry': expiry, 'retval': retval}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_ensureExpiry(self, expiry, retval, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.ensureExpiry raw getter
        :rtype: 
        :param expiry: uint32
        :param retval: bool
        """
        return self.C_.call_getter_raw('ensureExpiry', {'expiry': expiry, 'retval': retval}, expect_ec=ts4_expect_ec)

    def M_ensureExpiry(self, expiry, retval, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.ensureExpiry method call
        :param expiry: uint32
        :param retval: bool
        """
        _r_ = self.C_.call_method('ensureExpiry', {'expiry': expiry, 'retval': retval}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_ensureExpiry(self, expiry, retval, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.ensureExpiry signed method call
        :param expiry: uint32
        :param retval: bool
        """
        _r_ = self.C_.call_method_signed('ensureExpiry', {'expiry': expiry, 'retval': retval}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getOwner(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.getOwner
        :rtype: address
        :param _answer_id: uint32
        """
        return self.G_getOwner(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getOwner(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.getOwner getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getOwner', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getOwner raw getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getOwner(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.getOwner method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getOwner', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getOwner signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getPendingOwner(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.getPendingOwner
        :rtype: address
        :param _answer_id: uint32
        """
        return self.G_getPendingOwner(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getPendingOwner(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.getPendingOwner getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getPendingOwner', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getPendingOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getPendingOwner raw getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getPendingOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getPendingOwner(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.getPendingOwner method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getPendingOwner', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getPendingOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.getPendingOwner signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getPendingOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def transferOwner(self, new_owner, deadline, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.transferOwner
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        if ts4_sign:
            return self.S_transferOwner(new_owner, deadline, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_transferOwner(new_owner, deadline, ts4_expect_ec=ts4_expect_ec)

    def G_transferOwner(self, new_owner, deadline, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.transferOwner getter
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_transferOwner(self, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.transferOwner raw getter
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter_raw('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)

    def M_transferOwner(self, new_owner, deadline, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.transferOwner method call
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_transferOwner(self, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.transferOwner signed method call
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method_signed('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def cancelTransferOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.cancelTransferOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_cancelTransferOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_cancelTransferOwner(ts4_expect_ec=ts4_expect_ec)

    def G_cancelTransferOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.cancelTransferOwner getter
        :rtype: 
        """
        return self.C_.call_getter('cancelTransferOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_cancelTransferOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.cancelTransferOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('cancelTransferOwner', {}, expect_ec=ts4_expect_ec)

    def M_cancelTransferOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.cancelTransferOwner method call
        """
        _r_ = self.C_.call_method('cancelTransferOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_cancelTransferOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.cancelTransferOwner signed method call
        """
        _r_ = self.C_.call_method_signed('cancelTransferOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def acceptTransfer(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.acceptTransfer
        :rtype: 
        """
        if ts4_sign:
            return self.S_acceptTransfer(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_acceptTransfer(ts4_expect_ec=ts4_expect_ec)

    def G_acceptTransfer(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.acceptTransfer getter
        :rtype: 
        """
        return self.C_.call_getter('acceptTransfer', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_acceptTransfer(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.acceptTransfer raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('acceptTransfer', {}, expect_ec=ts4_expect_ec)

    def M_acceptTransfer(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.acceptTransfer method call
        """
        _r_ = self.C_.call_method('acceptTransfer', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_acceptTransfer(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.acceptTransfer signed method call
        """
        _r_ = self.C_.call_method_signed('acceptTransfer', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def relinquishOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.relinquishOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_relinquishOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_relinquishOwner(ts4_expect_ec=ts4_expect_ec)

    def G_relinquishOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.relinquishOwner getter
        :rtype: 
        """
        return self.C_.call_getter('relinquishOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_relinquishOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.relinquishOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('relinquishOwner', {}, expect_ec=ts4_expect_ec)

    def M_relinquishOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.relinquishOwner method call
        """
        _r_ = self.C_.call_method('relinquishOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_relinquishOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.relinquishOwner signed method call
        """
        _r_ = self.C_.call_method_signed('relinquishOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestProlong(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.requestProlong
        :rtype: 
        """
        if ts4_sign:
            return self.S_requestProlong(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestProlong(ts4_expect_ec=ts4_expect_ec)

    def G_requestProlong(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.requestProlong getter
        :rtype: 
        """
        return self.C_.call_getter('requestProlong', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestProlong(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.requestProlong raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('requestProlong', {}, expect_ec=ts4_expect_ec)

    def M_requestProlong(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.requestProlong method call
        """
        _r_ = self.C_.call_method('requestProlong', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestProlong(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.requestProlong signed method call
        """
        _r_ = self.C_.call_method_signed('requestProlong', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def deploySub(self, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.deploySub
        :rtype: 
        :param name: bytes
        """
        if ts4_sign:
            return self.S_deploySub(name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_deploySub(name, ts4_expect_ec=ts4_expect_ec)

    def G_deploySub(self, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.deploySub getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter('deploySub', {'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_deploySub(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.deploySub raw getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter_raw('deploySub', {'name': name}, expect_ec=ts4_expect_ec)

    def M_deploySub(self, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.deploySub method call
        :param name: bytes
        """
        _r_ = self.C_.call_method('deploySub', {'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_deploySub(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.deploySub signed method call
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('deploySub', {'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def syncSub(self, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.syncSub
        :rtype: 
        :param name: bytes
        """
        if ts4_sign:
            return self.S_syncSub(name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_syncSub(name, ts4_expect_ec=ts4_expect_ec)

    def G_syncSub(self, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.syncSub getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter('syncSub', {'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_syncSub(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.syncSub raw getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter_raw('syncSub', {'name': name}, expect_ec=ts4_expect_ec)

    def M_syncSub(self, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.syncSub method call
        :param name: bytes
        """
        _r_ = self.C_.call_method('syncSub', {'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_syncSub(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.syncSub signed method call
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('syncSub', {'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def subSynchronize(self, new_owner, new_expiry, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.subSynchronize
        :rtype: 
        :param new_owner: address
        :param new_expiry: uint32
        """
        if ts4_sign:
            return self.S_subSynchronize(new_owner, new_expiry, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_subSynchronize(new_owner, new_expiry, ts4_expect_ec=ts4_expect_ec)

    def G_subSynchronize(self, new_owner, new_expiry, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.subSynchronize getter
        :rtype: 
        :param new_owner: address
        :param new_expiry: uint32
        """
        return self.C_.call_getter('subSynchronize', {'new_owner': new_owner, 'new_expiry': new_expiry}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_subSynchronize(self, new_owner, new_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.subSynchronize raw getter
        :rtype: 
        :param new_owner: address
        :param new_expiry: uint32
        """
        return self.C_.call_getter_raw('subSynchronize', {'new_owner': new_owner, 'new_expiry': new_expiry}, expect_ec=ts4_expect_ec)

    def M_subSynchronize(self, new_owner, new_expiry, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.subSynchronize method call
        :param new_owner: address
        :param new_expiry: uint32
        """
        _r_ = self.C_.call_method('subSynchronize', {'new_owner': new_owner, 'new_expiry': new_expiry}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_subSynchronize(self, new_owner, new_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.subSynchronize signed method call
        :param new_owner: address
        :param new_expiry: uint32
        """
        _r_ = self.C_.call_method_signed('subSynchronize', {'new_owner': new_owner, 'new_expiry': new_expiry}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def passToOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.passToOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_passToOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_passToOwner(ts4_expect_ec=ts4_expect_ec)

    def G_passToOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.passToOwner getter
        :rtype: 
        """
        return self.C_.call_getter('passToOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.passToOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('passToOwner', {}, expect_ec=ts4_expect_ec)

    def M_passToOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.passToOwner method call
        """
        _r_ = self.C_.call_method('passToOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.passToOwner signed method call
        """
        _r_ = self.C_.call_method_signed('passToOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdrawExcess(self, dest, amount, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.withdrawExcess
        :rtype: 
        :param dest: address
        :param amount: uint128
        """
        if ts4_sign:
            return self.S_withdrawExcess(dest, amount, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_withdrawExcess(dest, amount, ts4_expect_ec=ts4_expect_ec)

    def G_withdrawExcess(self, dest, amount, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.withdrawExcess getter
        :rtype: 
        :param dest: address
        :param amount: uint128
        """
        return self.C_.call_getter('withdrawExcess', {'dest': dest, 'amount': amount}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdrawExcess(self, dest, amount, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.withdrawExcess raw getter
        :rtype: 
        :param dest: address
        :param amount: uint128
        """
        return self.C_.call_getter_raw('withdrawExcess', {'dest': dest, 'amount': amount}, expect_ec=ts4_expect_ec)

    def M_withdrawExcess(self, dest, amount, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.withdrawExcess method call
        :param dest: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method('withdrawExcess', {'dest': dest, 'amount': amount}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdrawExcess(self, dest, amount, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.withdrawExcess signed method call
        :param dest: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method_signed('withdrawExcess', {'dest': dest, 'amount': amount}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def sink(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.sink
        :rtype: 
        """
        if ts4_sign:
            return self.S_sink(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_sink(ts4_expect_ec=ts4_expect_ec)

    def G_sink(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.sink getter
        :rtype: 
        """
        return self.C_.call_getter('sink', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.sink raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('sink', {}, expect_ec=ts4_expect_ec)

    def M_sink(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.sink method call
        """
        _r_ = self.C_.call_method('sink', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.sink signed method call
        """
        _r_ = self.C_.call_method_signed('sink', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.st_root
        :rtype: address
        """
        return self.G_st_root(ts4_expect_ec=ts4_expect_ec)

    def G_st_root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.st_root getter
        :rtype: address
        """
        return self.C_.call_getter('st_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_root', {}, expect_ec=ts4_expect_ec)

    def M_st_root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.st_root method call
        """
        _r_ = self.C_.call_method('st_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_root signed method call
        """
        _r_ = self.C_.call_method_signed('st_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_type(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.st_type
        :rtype: uint8
        """
        return self.G_st_type(ts4_expect_ec=ts4_expect_ec)

    def G_st_type(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.st_type getter
        :rtype: uint8
        """
        return self.C_.call_getter('st_type', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_type raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('st_type', {}, expect_ec=ts4_expect_ec)

    def M_st_type(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.st_type method call
        """
        _r_ = self.C_.call_method('st_type', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_type signed method call
        """
        _r_ = self.C_.call_method_signed('st_type', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_name(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.st_name
        :rtype: bytes
        """
        return self.G_st_name(ts4_expect_ec=ts4_expect_ec)

    def G_st_name(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.st_name getter
        :rtype: bytes
        """
        return self.C_.call_getter('st_name', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_name raw getter
        :rtype: bytes
        """
        return self.C_.call_getter_raw('st_name', {}, expect_ec=ts4_expect_ec)

    def M_st_name(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.st_name method call
        """
        _r_ = self.C_.call_method('st_name', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_name signed method call
        """
        _r_ = self.C_.call_method_signed('st_name', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_parent(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.st_parent
        :rtype: address
        """
        return self.G_st_parent(ts4_expect_ec=ts4_expect_ec)

    def G_st_parent(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.st_parent getter
        :rtype: address
        """
        return self.C_.call_getter('st_parent', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_parent raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_parent', {}, expect_ec=ts4_expect_ec)

    def M_st_parent(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.st_parent method call
        """
        _r_ = self.C_.call_method('st_parent', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.st_parent signed method call
        """
        _r_ = self.C_.call_method_signed('st_parent', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.base_code
        :rtype: cell
        """
        return self.G_base_code(ts4_expect_ec=ts4_expect_ec)

    def G_base_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.base_code getter
        :rtype: cell
        """
        return self.C_.call_getter('base_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.base_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('base_code', {}, expect_ec=ts4_expect_ec)

    def M_base_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.base_code method call
        """
        _r_ = self.C_.call_method('base_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.base_code signed method call
        """
        _r_ = self.C_.call_method_signed('base_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_version(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.m_version
        :rtype: uint16
        """
        return self.G_m_version(ts4_expect_ec=ts4_expect_ec)

    def G_m_version(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.m_version getter
        :rtype: uint16
        """
        return self.C_.call_getter('m_version', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.m_version raw getter
        :rtype: uint16
        """
        return self.C_.call_getter_raw('m_version', {}, expect_ec=ts4_expect_ec)

    def M_m_version(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.m_version method call
        """
        _r_ = self.C_.call_method('m_version', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.m_version signed method call
        """
        _r_ = self.C_.call_method_signed('m_version', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.m_revision
        :rtype: uint32
        """
        return self.G_m_revision(ts4_expect_ec=ts4_expect_ec)

    def G_m_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.m_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('m_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.m_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('m_revision', {}, expect_ec=ts4_expect_ec)

    def M_m_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.m_revision method call
        """
        _r_ = self.C_.call_method('m_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.m_revision signed method call
        """
        _r_ = self.C_.call_method_signed('m_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def owner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.owner
        :rtype: address
        """
        return self.G_owner(ts4_expect_ec=ts4_expect_ec)

    def G_owner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.owner getter
        :rtype: address
        """
        return self.C_.call_getter('owner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.owner raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('owner', {}, expect_ec=ts4_expect_ec)

    def M_owner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.owner method call
        """
        _r_ = self.C_.call_method('owner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.owner signed method call
        """
        _r_ = self.C_.call_method_signed('owner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def pending_owner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.pending_owner
        :rtype: address
        """
        return self.G_pending_owner(ts4_expect_ec=ts4_expect_ec)

    def G_pending_owner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.pending_owner getter
        :rtype: address
        """
        return self.C_.call_getter('pending_owner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_pending_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.pending_owner raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('pending_owner', {}, expect_ec=ts4_expect_ec)

    def M_pending_owner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.pending_owner method call
        """
        _r_ = self.C_.call_method('pending_owner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_pending_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.pending_owner signed method call
        """
        _r_ = self.C_.call_method_signed('pending_owner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def owner_transfer_deadline(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.owner_transfer_deadline
        :rtype: uint32
        """
        return self.G_owner_transfer_deadline(ts4_expect_ec=ts4_expect_ec)

    def G_owner_transfer_deadline(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.owner_transfer_deadline getter
        :rtype: uint32
        """
        return self.C_.call_getter('owner_transfer_deadline', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_owner_transfer_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.owner_transfer_deadline raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('owner_transfer_deadline', {}, expect_ec=ts4_expect_ec)

    def M_owner_transfer_deadline(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.owner_transfer_deadline method call
        """
        _r_ = self.C_.call_method('owner_transfer_deadline', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_owner_transfer_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.owner_transfer_deadline signed method call
        """
        _r_ = self.C_.call_method_signed('owner_transfer_deadline', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def relinquish_owner_deadline(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.relinquish_owner_deadline
        :rtype: uint32
        """
        return self.G_relinquish_owner_deadline(ts4_expect_ec=ts4_expect_ec)

    def G_relinquish_owner_deadline(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.relinquish_owner_deadline getter
        :rtype: uint32
        """
        return self.C_.call_getter('relinquish_owner_deadline', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_relinquish_owner_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.relinquish_owner_deadline raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('relinquish_owner_deadline', {}, expect_ec=ts4_expect_ec)

    def M_relinquish_owner_deadline(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.relinquish_owner_deadline method call
        """
        _r_ = self.C_.call_method('relinquish_owner_deadline', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_relinquish_owner_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.relinquish_owner_deadline signed method call
        """
        _r_ = self.C_.call_method_signed('relinquish_owner_deadline', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def value(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.value
        :rtype: map(int16,address)
        """
        return self.G_value(ts4_expect_ec=ts4_expect_ec)

    def G_value(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.value getter
        :rtype: map(int16,address)
        """
        return self.C_.call_getter('value', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_value(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.value raw getter
        :rtype: map(int16,address)
        """
        return self.C_.call_getter_raw('value', {}, expect_ec=ts4_expect_ec)

    def M_value(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.value method call
        """
        _r_ = self.C_.call_method('value', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_value(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.value signed method call
        """
        _r_ = self.C_.call_method_signed('value', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def registered(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.registered
        :rtype: uint32
        """
        return self.G_registered(ts4_expect_ec=ts4_expect_ec)

    def G_registered(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.registered getter
        :rtype: uint32
        """
        return self.C_.call_getter('registered', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_registered(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.registered raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('registered', {}, expect_ec=ts4_expect_ec)

    def M_registered(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.registered method call
        """
        _r_ = self.C_.call_method('registered', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_registered(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.registered signed method call
        """
        _r_ = self.C_.call_method_signed('registered', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auctioned(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.auctioned
        :rtype: uint32
        """
        return self.G_auctioned(ts4_expect_ec=ts4_expect_ec)

    def G_auctioned(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.auctioned getter
        :rtype: uint32
        """
        return self.C_.call_getter('auctioned', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auctioned(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.auctioned raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('auctioned', {}, expect_ec=ts4_expect_ec)

    def M_auctioned(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.auctioned method call
        """
        _r_ = self.C_.call_method('auctioned', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auctioned(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.auctioned signed method call
        """
        _r_ = self.C_.call_method_signed('auctioned', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def expires(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Cert.expires
        :rtype: uint32
        """
        return self.G_expires(ts4_expect_ec=ts4_expect_ec)

    def G_expires(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Cert.expires getter
        :rtype: uint32
        """
        return self.C_.call_getter('expires', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_expires(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.expires raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('expires', {}, expect_ec=ts4_expect_ec)

    def M_expires(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Cert.expires method call
        """
        _r_ = self.C_.call_method('expires', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_expires(self, ts4_expect_ec=0):
        """
        Wrapper for D4Cert.expires signed method call
        """
        _r_ = self.C_.call_method_signed('expires', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4DeBot(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4DeBot.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4DeBot.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4DeBot.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4DeBot.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4DeBot.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4MFT128(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4MFT128.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4MFT128.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4MFT128.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4MFT128.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4MFT128.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4Root(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def dropAdminFlag(self, flags, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.dropAdminFlag
        :rtype: 
        :param flags: uint8
        """
        if ts4_sign:
            return self.S_dropAdminFlag(flags, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_dropAdminFlag(flags, ts4_expect_ec=ts4_expect_ec)

    def G_dropAdminFlag(self, flags, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.dropAdminFlag getter
        :rtype: 
        :param flags: uint8
        """
        return self.C_.call_getter('dropAdminFlag', {'flags': flags}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_dropAdminFlag(self, flags, ts4_expect_ec=0):
        """
        Wrapper for D4Root.dropAdminFlag raw getter
        :rtype: 
        :param flags: uint8
        """
        return self.C_.call_getter_raw('dropAdminFlag', {'flags': flags}, expect_ec=ts4_expect_ec)

    def M_dropAdminFlag(self, flags, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.dropAdminFlag method call
        :param flags: uint8
        """
        _r_ = self.C_.call_method('dropAdminFlag', {'flags': flags}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_dropAdminFlag(self, flags, ts4_expect_ec=0):
        """
        Wrapper for D4Root.dropAdminFlag signed method call
        :param flags: uint8
        """
        _r_ = self.C_.call_method_signed('dropAdminFlag', {'flags': flags}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminDeploy(self, name, set_owner, set_expiry, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminDeploy
        :rtype: 
        :param name: bytes
        :param set_owner: address
        :param set_expiry: uint32
        """
        if ts4_sign:
            return self.S_adminDeploy(name, set_owner, set_expiry, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminDeploy(name, set_owner, set_expiry, ts4_expect_ec=ts4_expect_ec)

    def G_adminDeploy(self, name, set_owner, set_expiry, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminDeploy getter
        :rtype: 
        :param name: bytes
        :param set_owner: address
        :param set_expiry: uint32
        """
        return self.C_.call_getter('adminDeploy', {'name': name, 'set_owner': set_owner, 'set_expiry': set_expiry}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminDeploy(self, name, set_owner, set_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminDeploy raw getter
        :rtype: 
        :param name: bytes
        :param set_owner: address
        :param set_expiry: uint32
        """
        return self.C_.call_getter_raw('adminDeploy', {'name': name, 'set_owner': set_owner, 'set_expiry': set_expiry}, expect_ec=ts4_expect_ec)

    def M_adminDeploy(self, name, set_owner, set_expiry, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminDeploy method call
        :param name: bytes
        :param set_owner: address
        :param set_expiry: uint32
        """
        _r_ = self.C_.call_method('adminDeploy', {'name': name, 'set_owner': set_owner, 'set_expiry': set_expiry}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminDeploy(self, name, set_owner, set_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminDeploy signed method call
        :param name: bytes
        :param set_owner: address
        :param set_expiry: uint32
        """
        _r_ = self.C_.call_method_signed('adminDeploy', {'name': name, 'set_owner': set_owner, 'set_expiry': set_expiry}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminReserve(self, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminReserve
        :rtype: 
        :param name: bytes
        """
        if ts4_sign:
            return self.S_adminReserve(name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminReserve(name, ts4_expect_ec=ts4_expect_ec)

    def G_adminReserve(self, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminReserve getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter('adminReserve', {'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminReserve(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminReserve raw getter
        :rtype: 
        :param name: bytes
        """
        return self.C_.call_getter_raw('adminReserve', {'name': name}, expect_ec=ts4_expect_ec)

    def M_adminReserve(self, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminReserve method call
        :param name: bytes
        """
        _r_ = self.C_.call_method('adminReserve', {'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminReserve(self, name, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminReserve signed method call
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('adminReserve', {'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminChown(self, name, set_owner, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminChown
        :rtype: 
        :param name: bytes
        :param set_owner: address
        """
        if ts4_sign:
            return self.S_adminChown(name, set_owner, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminChown(name, set_owner, ts4_expect_ec=ts4_expect_ec)

    def G_adminChown(self, name, set_owner, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminChown getter
        :rtype: 
        :param name: bytes
        :param set_owner: address
        """
        return self.C_.call_getter('adminChown', {'name': name, 'set_owner': set_owner}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminChown(self, name, set_owner, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminChown raw getter
        :rtype: 
        :param name: bytes
        :param set_owner: address
        """
        return self.C_.call_getter_raw('adminChown', {'name': name, 'set_owner': set_owner}, expect_ec=ts4_expect_ec)

    def M_adminChown(self, name, set_owner, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminChown method call
        :param name: bytes
        :param set_owner: address
        """
        _r_ = self.C_.call_method('adminChown', {'name': name, 'set_owner': set_owner}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminChown(self, name, set_owner, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminChown signed method call
        :param name: bytes
        :param set_owner: address
        """
        _r_ = self.C_.call_method_signed('adminChown', {'name': name, 'set_owner': set_owner}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminChexp(self, name, set_expiry, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminChexp
        :rtype: 
        :param name: bytes
        :param set_expiry: uint32
        """
        if ts4_sign:
            return self.S_adminChexp(name, set_expiry, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminChexp(name, set_expiry, ts4_expect_ec=ts4_expect_ec)

    def G_adminChexp(self, name, set_expiry, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminChexp getter
        :rtype: 
        :param name: bytes
        :param set_expiry: uint32
        """
        return self.C_.call_getter('adminChexp', {'name': name, 'set_expiry': set_expiry}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminChexp(self, name, set_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminChexp raw getter
        :rtype: 
        :param name: bytes
        :param set_expiry: uint32
        """
        return self.C_.call_getter_raw('adminChexp', {'name': name, 'set_expiry': set_expiry}, expect_ec=ts4_expect_ec)

    def M_adminChexp(self, name, set_expiry, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminChexp method call
        :param name: bytes
        :param set_expiry: uint32
        """
        _r_ = self.C_.call_method('adminChexp', {'name': name, 'set_expiry': set_expiry}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminChexp(self, name, set_expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminChexp signed method call
        :param name: bytes
        :param set_expiry: uint32
        """
        _r_ = self.C_.call_method_signed('adminChexp', {'name': name, 'set_expiry': set_expiry}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminUpgradeUser(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminUpgradeUser
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_adminUpgradeUser(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminUpgradeUser(target, ts4_expect_ec=ts4_expect_ec)

    def G_adminUpgradeUser(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminUpgradeUser getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('adminUpgradeUser', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminUpgradeUser(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminUpgradeUser raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('adminUpgradeUser', {'target': target}, expect_ec=ts4_expect_ec)

    def M_adminUpgradeUser(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminUpgradeUser method call
        :param target: address
        """
        _r_ = self.C_.call_method('adminUpgradeUser', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminUpgradeUser(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminUpgradeUser signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('adminUpgradeUser', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def adminUpgradeCert(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.adminUpgradeCert
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_adminUpgradeCert(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_adminUpgradeCert(target, ts4_expect_ec=ts4_expect_ec)

    def G_adminUpgradeCert(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.adminUpgradeCert getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('adminUpgradeCert', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_adminUpgradeCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminUpgradeCert raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('adminUpgradeCert', {'target': target}, expect_ec=ts4_expect_ec)

    def M_adminUpgradeCert(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.adminUpgradeCert method call
        :param target: address
        """
        _r_ = self.C_.call_method('adminUpgradeCert', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_adminUpgradeCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Root.adminUpgradeCert signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('adminUpgradeCert', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def onProposalPassed(self, proposalInfo, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.onProposalPassed
        :rtype: 
        :param proposalInfo: tuple
        """
        if ts4_sign:
            return self.S_onProposalPassed(proposalInfo, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_onProposalPassed(proposalInfo, ts4_expect_ec=ts4_expect_ec)

    def G_onProposalPassed(self, proposalInfo, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.onProposalPassed getter
        :rtype: 
        :param proposalInfo: tuple
        """
        return self.C_.call_getter('onProposalPassed', {'proposalInfo': proposalInfo}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_onProposalPassed(self, proposalInfo, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalPassed raw getter
        :rtype: 
        :param proposalInfo: tuple
        """
        return self.C_.call_getter_raw('onProposalPassed', {'proposalInfo': proposalInfo}, expect_ec=ts4_expect_ec)

    def M_onProposalPassed(self, proposalInfo, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.onProposalPassed method call
        :param proposalInfo: tuple
        """
        _r_ = self.C_.call_method('onProposalPassed', {'proposalInfo': proposalInfo}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_onProposalPassed(self, proposalInfo, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalPassed signed method call
        :param proposalInfo: tuple
        """
        _r_ = self.C_.call_method_signed('onProposalPassed', {'proposalInfo': proposalInfo}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def onProposalRejected(self, proposalInfo, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.onProposalRejected
        :rtype: 
        :param proposalInfo: tuple
        """
        if ts4_sign:
            return self.S_onProposalRejected(proposalInfo, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_onProposalRejected(proposalInfo, ts4_expect_ec=ts4_expect_ec)

    def G_onProposalRejected(self, proposalInfo, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.onProposalRejected getter
        :rtype: 
        :param proposalInfo: tuple
        """
        return self.C_.call_getter('onProposalRejected', {'proposalInfo': proposalInfo}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_onProposalRejected(self, proposalInfo, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalRejected raw getter
        :rtype: 
        :param proposalInfo: tuple
        """
        return self.C_.call_getter_raw('onProposalRejected', {'proposalInfo': proposalInfo}, expect_ec=ts4_expect_ec)

    def M_onProposalRejected(self, proposalInfo, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.onProposalRejected method call
        :param proposalInfo: tuple
        """
        _r_ = self.C_.call_method('onProposalRejected', {'proposalInfo': proposalInfo}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_onProposalRejected(self, proposalInfo, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalRejected signed method call
        :param proposalInfo: tuple
        """
        _r_ = self.C_.call_method_signed('onProposalRejected', {'proposalInfo': proposalInfo}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def onProposalDeploy(self, value0, proposalType, specific, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.onProposalDeploy
        :rtype: 
        :param value0: address
        :param proposalType: uint8
        :param specific: cell
        """
        if ts4_sign:
            return self.S_onProposalDeploy(value0, proposalType, specific, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_onProposalDeploy(value0, proposalType, specific, ts4_expect_ec=ts4_expect_ec)

    def G_onProposalDeploy(self, value0, proposalType, specific, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.onProposalDeploy getter
        :rtype: 
        :param value0: address
        :param proposalType: uint8
        :param specific: cell
        """
        return self.C_.call_getter('onProposalDeploy', {'value0': value0, 'proposalType': proposalType, 'specific': specific}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_onProposalDeploy(self, value0, proposalType, specific, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalDeploy raw getter
        :rtype: 
        :param value0: address
        :param proposalType: uint8
        :param specific: cell
        """
        return self.C_.call_getter_raw('onProposalDeploy', {'value0': value0, 'proposalType': proposalType, 'specific': specific}, expect_ec=ts4_expect_ec)

    def M_onProposalDeploy(self, value0, proposalType, specific, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.onProposalDeploy method call
        :param value0: address
        :param proposalType: uint8
        :param specific: cell
        """
        _r_ = self.C_.call_method('onProposalDeploy', {'value0': value0, 'proposalType': proposalType, 'specific': specific}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_onProposalDeploy(self, value0, proposalType, specific, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onProposalDeploy signed method call
        :param value0: address
        :param proposalType: uint8
        :param specific: cell
        """
        _r_ = self.C_.call_method_signed('onProposalDeploy', {'value0': value0, 'proposalType': proposalType, 'specific': specific}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def deployUserForMe(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.deployUserForMe
        :rtype: address
        :param _answer_id: uint32
        """
        return self.G_deployUserForMe(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_deployUserForMe(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.deployUserForMe getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter('deployUserForMe', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_deployUserForMe(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.deployUserForMe raw getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('deployUserForMe', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_deployUserForMe(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.deployUserForMe method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('deployUserForMe', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_deployUserForMe(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.deployUserForMe signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('deployUserForMe', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def deployUserForPubKey(self, pubkey, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.deployUserForPubKey
        :rtype: address
        :param _answer_id: uint32
        :param pubkey: uint256
        """
        return self.G_deployUserForPubKey(pubkey, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_deployUserForPubKey(self, pubkey, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.deployUserForPubKey getter
        :rtype: address
        :param _answer_id: uint32
        :param pubkey: uint256
        """
        return self.C_.call_getter('deployUserForPubKey', {'_answer_id': _answer_id, 'pubkey': pubkey}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_deployUserForPubKey(self, pubkey, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.deployUserForPubKey raw getter
        :rtype: address
        :param _answer_id: uint32
        :param pubkey: uint256
        """
        return self.C_.call_getter_raw('deployUserForPubKey', {'_answer_id': _answer_id, 'pubkey': pubkey}, expect_ec=ts4_expect_ec)

    def M_deployUserForPubKey(self, pubkey, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.deployUserForPubKey method call
        :param _answer_id: uint32
        :param pubkey: uint256
        """
        _r_ = self.C_.call_method('deployUserForPubKey', {'_answer_id': _answer_id, 'pubkey': pubkey}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_deployUserForPubKey(self, pubkey, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.deployUserForPubKey signed method call
        :param _answer_id: uint32
        :param pubkey: uint256
        """
        _r_ = self.C_.call_method_signed('deployUserForPubKey', {'_answer_id': _answer_id, 'pubkey': pubkey}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resolveUser(self, user, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.resolveUser
        :rtype: address
        :param _answer_id: uint32
        :param user: address
        """
        return self.G_resolveUser(user, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_resolveUser(self, user, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.resolveUser getter
        :rtype: address
        :param _answer_id: uint32
        :param user: address
        """
        return self.C_.call_getter('resolveUser', {'_answer_id': _answer_id, 'user': user}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resolveUser(self, user, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveUser raw getter
        :rtype: address
        :param _answer_id: uint32
        :param user: address
        """
        return self.C_.call_getter_raw('resolveUser', {'_answer_id': _answer_id, 'user': user}, expect_ec=ts4_expect_ec)

    def M_resolveUser(self, user, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.resolveUser method call
        :param _answer_id: uint32
        :param user: address
        """
        _r_ = self.C_.call_method('resolveUser', {'_answer_id': _answer_id, 'user': user}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resolveUser(self, user, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveUser signed method call
        :param _answer_id: uint32
        :param user: address
        """
        _r_ = self.C_.call_method_signed('resolveUser', {'_answer_id': _answer_id, 'user': user}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resolve(self, ct_type, name, parent, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.resolve
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        return self.G_resolve(ct_type, name, parent, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_resolve(self, ct_type, name, parent, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.resolve getter
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter('resolve', {'_answer_id': _answer_id, 'ct_type': ct_type, 'name': name, 'parent': parent}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resolve(self, ct_type, name, parent, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolve raw getter
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter_raw('resolve', {'_answer_id': _answer_id, 'ct_type': ct_type, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)

    def M_resolve(self, ct_type, name, parent, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.resolve method call
        :param _answer_id: uint32
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method('resolve', {'_answer_id': _answer_id, 'ct_type': ct_type, 'name': name, 'parent': parent}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resolve(self, ct_type, name, parent, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolve signed method call
        :param _answer_id: uint32
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method_signed('resolve', {'_answer_id': _answer_id, 'ct_type': ct_type, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resolveFull(self, ct_type, fullname, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.resolveFull
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param fullname: bytes
        """
        return self.G_resolveFull(ct_type, fullname, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_resolveFull(self, ct_type, fullname, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.resolveFull getter
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param fullname: bytes
        """
        return self.C_.call_getter('resolveFull', {'_answer_id': _answer_id, 'ct_type': ct_type, 'fullname': fullname}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resolveFull(self, ct_type, fullname, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveFull raw getter
        :rtype: address
        :param _answer_id: uint32
        :param ct_type: uint8
        :param fullname: bytes
        """
        return self.C_.call_getter_raw('resolveFull', {'_answer_id': _answer_id, 'ct_type': ct_type, 'fullname': fullname}, expect_ec=ts4_expect_ec)

    def M_resolveFull(self, ct_type, fullname, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.resolveFull method call
        :param _answer_id: uint32
        :param ct_type: uint8
        :param fullname: bytes
        """
        _r_ = self.C_.call_method('resolveFull', {'_answer_id': _answer_id, 'ct_type': ct_type, 'fullname': fullname}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resolveFull(self, ct_type, fullname, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveFull signed method call
        :param _answer_id: uint32
        :param ct_type: uint8
        :param fullname: bytes
        """
        _r_ = self.C_.call_method_signed('resolveFull', {'_answer_id': _answer_id, 'ct_type': ct_type, 'fullname': fullname}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def createAuction(self, origin, revision, name, duration, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.createAuction
        :rtype: address
        :param _answer_id: uint32
        :param origin: address
        :param revision: uint32
        :param name: bytes
        :param duration: uint8
        """
        return self.G_createAuction(origin, revision, name, duration, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_createAuction(self, origin, revision, name, duration, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.createAuction getter
        :rtype: address
        :param _answer_id: uint32
        :param origin: address
        :param revision: uint32
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter('createAuction', {'_answer_id': _answer_id, 'origin': origin, 'revision': revision, 'name': name, 'duration': duration}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_createAuction(self, origin, revision, name, duration, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.createAuction raw getter
        :rtype: address
        :param _answer_id: uint32
        :param origin: address
        :param revision: uint32
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter_raw('createAuction', {'_answer_id': _answer_id, 'origin': origin, 'revision': revision, 'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)

    def M_createAuction(self, origin, revision, name, duration, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.createAuction method call
        :param _answer_id: uint32
        :param origin: address
        :param revision: uint32
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method('createAuction', {'_answer_id': _answer_id, 'origin': origin, 'revision': revision, 'name': name, 'duration': duration}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_createAuction(self, origin, revision, name, duration, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.createAuction signed method call
        :param _answer_id: uint32
        :param origin: address
        :param revision: uint32
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method_signed('createAuction', {'_answer_id': _answer_id, 'origin': origin, 'revision': revision, 'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resolveAuction(self, name, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.resolveAuction
        :rtype: address
        :param _answer_id: uint32
        :param name: bytes
        """
        return self.G_resolveAuction(name, _answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_resolveAuction(self, name, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.resolveAuction getter
        :rtype: address
        :param _answer_id: uint32
        :param name: bytes
        """
        return self.C_.call_getter('resolveAuction', {'_answer_id': _answer_id, 'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resolveAuction(self, name, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveAuction raw getter
        :rtype: address
        :param _answer_id: uint32
        :param name: bytes
        """
        return self.C_.call_getter_raw('resolveAuction', {'_answer_id': _answer_id, 'name': name}, expect_ec=ts4_expect_ec)

    def M_resolveAuction(self, name, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.resolveAuction method call
        :param _answer_id: uint32
        :param name: bytes
        """
        _r_ = self.C_.call_method('resolveAuction', {'_answer_id': _answer_id, 'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resolveAuction(self, name, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.resolveAuction signed method call
        :param _answer_id: uint32
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('resolveAuction', {'_answer_id': _answer_id, 'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def onAuctionResult(self, winner, exp, name, parent, deploy, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.onAuctionResult
        :rtype: 
        :param winner: address
        :param exp: uint32
        :param name: bytes
        :param parent: address
        :param deploy: bool
        """
        if ts4_sign:
            return self.S_onAuctionResult(winner, exp, name, parent, deploy, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_onAuctionResult(winner, exp, name, parent, deploy, ts4_expect_ec=ts4_expect_ec)

    def G_onAuctionResult(self, winner, exp, name, parent, deploy, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.onAuctionResult getter
        :rtype: 
        :param winner: address
        :param exp: uint32
        :param name: bytes
        :param parent: address
        :param deploy: bool
        """
        return self.C_.call_getter('onAuctionResult', {'winner': winner, 'exp': exp, 'name': name, 'parent': parent, 'deploy': deploy}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_onAuctionResult(self, winner, exp, name, parent, deploy, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onAuctionResult raw getter
        :rtype: 
        :param winner: address
        :param exp: uint32
        :param name: bytes
        :param parent: address
        :param deploy: bool
        """
        return self.C_.call_getter_raw('onAuctionResult', {'winner': winner, 'exp': exp, 'name': name, 'parent': parent, 'deploy': deploy}, expect_ec=ts4_expect_ec)

    def M_onAuctionResult(self, winner, exp, name, parent, deploy, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.onAuctionResult method call
        :param winner: address
        :param exp: uint32
        :param name: bytes
        :param parent: address
        :param deploy: bool
        """
        _r_ = self.C_.call_method('onAuctionResult', {'winner': winner, 'exp': exp, 'name': name, 'parent': parent, 'deploy': deploy}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_onAuctionResult(self, winner, exp, name, parent, deploy, ts4_expect_ec=0):
        """
        Wrapper for D4Root.onAuctionResult signed method call
        :param winner: address
        :param exp: uint32
        :param name: bytes
        :param parent: address
        :param deploy: bool
        """
        _r_ = self.C_.call_method_signed('onAuctionResult', {'winner': winner, 'exp': exp, 'name': name, 'parent': parent, 'deploy': deploy}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def applyAuctionCallback(self, success, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.applyAuctionCallback
        :rtype: 
        :param success: bool
        """
        if ts4_sign:
            return self.S_applyAuctionCallback(success, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_applyAuctionCallback(success, ts4_expect_ec=ts4_expect_ec)

    def G_applyAuctionCallback(self, success, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.applyAuctionCallback getter
        :rtype: 
        :param success: bool
        """
        return self.C_.call_getter('applyAuctionCallback', {'success': success}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_applyAuctionCallback(self, success, ts4_expect_ec=0):
        """
        Wrapper for D4Root.applyAuctionCallback raw getter
        :rtype: 
        :param success: bool
        """
        return self.C_.call_getter_raw('applyAuctionCallback', {'success': success}, expect_ec=ts4_expect_ec)

    def M_applyAuctionCallback(self, success, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.applyAuctionCallback method call
        :param success: bool
        """
        _r_ = self.C_.call_method('applyAuctionCallback', {'success': success}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_applyAuctionCallback(self, success, ts4_expect_ec=0):
        """
        Wrapper for D4Root.applyAuctionCallback signed method call
        :param success: bool
        """
        _r_ = self.C_.call_method_signed('applyAuctionCallback', {'success': success}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def subCertDepl(self, name, parent, subname, new_owner, expiry, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.subCertDepl
        :rtype: 
        :param name: bytes
        :param parent: address
        :param subname: bytes
        :param new_owner: address
        :param expiry: uint32
        """
        if ts4_sign:
            return self.S_subCertDepl(name, parent, subname, new_owner, expiry, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_subCertDepl(name, parent, subname, new_owner, expiry, ts4_expect_ec=ts4_expect_ec)

    def G_subCertDepl(self, name, parent, subname, new_owner, expiry, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.subCertDepl getter
        :rtype: 
        :param name: bytes
        :param parent: address
        :param subname: bytes
        :param new_owner: address
        :param expiry: uint32
        """
        return self.C_.call_getter('subCertDepl', {'name': name, 'parent': parent, 'subname': subname, 'new_owner': new_owner, 'expiry': expiry}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_subCertDepl(self, name, parent, subname, new_owner, expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.subCertDepl raw getter
        :rtype: 
        :param name: bytes
        :param parent: address
        :param subname: bytes
        :param new_owner: address
        :param expiry: uint32
        """
        return self.C_.call_getter_raw('subCertDepl', {'name': name, 'parent': parent, 'subname': subname, 'new_owner': new_owner, 'expiry': expiry}, expect_ec=ts4_expect_ec)

    def M_subCertDepl(self, name, parent, subname, new_owner, expiry, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.subCertDepl method call
        :param name: bytes
        :param parent: address
        :param subname: bytes
        :param new_owner: address
        :param expiry: uint32
        """
        _r_ = self.C_.call_method('subCertDepl', {'name': name, 'parent': parent, 'subname': subname, 'new_owner': new_owner, 'expiry': expiry}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_subCertDepl(self, name, parent, subname, new_owner, expiry, ts4_expect_ec=0):
        """
        Wrapper for D4Root.subCertDepl signed method call
        :param name: bytes
        :param parent: address
        :param subname: bytes
        :param new_owner: address
        :param expiry: uint32
        """
        _r_ = self.C_.call_method_signed('subCertDepl', {'name': name, 'parent': parent, 'subname': subname, 'new_owner': new_owner, 'expiry': expiry}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def receiveShards(self, ct_type, name, parent, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.receiveShards
        :rtype: 
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        if ts4_sign:
            return self.S_receiveShards(ct_type, name, parent, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_receiveShards(ct_type, name, parent, ts4_expect_ec=ts4_expect_ec)

    def G_receiveShards(self, ct_type, name, parent, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.receiveShards getter
        :rtype: 
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter('receiveShards', {'ct_type': ct_type, 'name': name, 'parent': parent}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_receiveShards(self, ct_type, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4Root.receiveShards raw getter
        :rtype: 
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter_raw('receiveShards', {'ct_type': ct_type, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)

    def M_receiveShards(self, ct_type, name, parent, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.receiveShards method call
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method('receiveShards', {'ct_type': ct_type, 'name': name, 'parent': parent}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_receiveShards(self, ct_type, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4Root.receiveShards signed method call
        :param ct_type: uint8
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method_signed('receiveShards', {'ct_type': ct_type, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setBaseCode(self, code, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.setBaseCode
        :rtype: 
        :param code: cell
        """
        if ts4_sign:
            return self.S_setBaseCode(code, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setBaseCode(code, ts4_expect_ec=ts4_expect_ec)

    def G_setBaseCode(self, code, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.setBaseCode getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter('setBaseCode', {'code': code}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setBaseCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setBaseCode raw getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter_raw('setBaseCode', {'code': code}, expect_ec=ts4_expect_ec)

    def M_setBaseCode(self, code, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.setBaseCode method call
        :param code: cell
        """
        _r_ = self.C_.call_method('setBaseCode', {'code': code}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setBaseCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setBaseCode signed method call
        :param code: cell
        """
        _r_ = self.C_.call_method_signed('setBaseCode', {'code': code}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setCertificateCode(self, code, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.setCertificateCode
        :rtype: 
        :param code: cell
        """
        if ts4_sign:
            return self.S_setCertificateCode(code, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setCertificateCode(code, ts4_expect_ec=ts4_expect_ec)

    def G_setCertificateCode(self, code, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.setCertificateCode getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter('setCertificateCode', {'code': code}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setCertificateCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setCertificateCode raw getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter_raw('setCertificateCode', {'code': code}, expect_ec=ts4_expect_ec)

    def M_setCertificateCode(self, code, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.setCertificateCode method call
        :param code: cell
        """
        _r_ = self.C_.call_method('setCertificateCode', {'code': code}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setCertificateCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setCertificateCode signed method call
        :param code: cell
        """
        _r_ = self.C_.call_method_signed('setCertificateCode', {'code': code}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setAuctionCode(self, code, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.setAuctionCode
        :rtype: 
        :param code: cell
        """
        if ts4_sign:
            return self.S_setAuctionCode(code, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setAuctionCode(code, ts4_expect_ec=ts4_expect_ec)

    def G_setAuctionCode(self, code, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.setAuctionCode getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter('setAuctionCode', {'code': code}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setAuctionCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setAuctionCode raw getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter_raw('setAuctionCode', {'code': code}, expect_ec=ts4_expect_ec)

    def M_setAuctionCode(self, code, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.setAuctionCode method call
        :param code: cell
        """
        _r_ = self.C_.call_method('setAuctionCode', {'code': code}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setAuctionCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setAuctionCode signed method call
        :param code: cell
        """
        _r_ = self.C_.call_method_signed('setAuctionCode', {'code': code}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setUserCode(self, code, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.setUserCode
        :rtype: 
        :param code: cell
        """
        if ts4_sign:
            return self.S_setUserCode(code, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setUserCode(code, ts4_expect_ec=ts4_expect_ec)

    def G_setUserCode(self, code, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.setUserCode getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter('setUserCode', {'code': code}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setUserCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setUserCode raw getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter_raw('setUserCode', {'code': code}, expect_ec=ts4_expect_ec)

    def M_setUserCode(self, code, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.setUserCode method call
        :param code: cell
        """
        _r_ = self.C_.call_method('setUserCode', {'code': code}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setUserCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setUserCode signed method call
        :param code: cell
        """
        _r_ = self.C_.call_method_signed('setUserCode', {'code': code}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setRootCode(self, code, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.setRootCode
        :rtype: 
        :param code: cell
        """
        if ts4_sign:
            return self.S_setRootCode(code, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setRootCode(code, ts4_expect_ec=ts4_expect_ec)

    def G_setRootCode(self, code, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.setRootCode getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter('setRootCode', {'code': code}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setRootCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setRootCode raw getter
        :rtype: 
        :param code: cell
        """
        return self.C_.call_getter_raw('setRootCode', {'code': code}, expect_ec=ts4_expect_ec)

    def M_setRootCode(self, code, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.setRootCode method call
        :param code: cell
        """
        _r_ = self.C_.call_method('setRootCode', {'code': code}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setRootCode(self, code, ts4_expect_ec=0):
        """
        Wrapper for D4Root.setRootCode signed method call
        :param code: cell
        """
        _r_ = self.C_.call_method_signed('setRootCode', {'code': code}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgradeMeRequest(self, ct_type, my_revision, my_hash, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.upgradeMeRequest
        :rtype: 
        :param ct_type: uint8
        :param my_revision: uint32
        :param my_hash: uint256
        """
        if ts4_sign:
            return self.S_upgradeMeRequest(ct_type, my_revision, my_hash, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgradeMeRequest(ct_type, my_revision, my_hash, ts4_expect_ec=ts4_expect_ec)

    def G_upgradeMeRequest(self, ct_type, my_revision, my_hash, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.upgradeMeRequest getter
        :rtype: 
        :param ct_type: uint8
        :param my_revision: uint32
        :param my_hash: uint256
        """
        return self.C_.call_getter('upgradeMeRequest', {'ct_type': ct_type, 'my_revision': my_revision, 'my_hash': my_hash}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgradeMeRequest(self, ct_type, my_revision, my_hash, ts4_expect_ec=0):
        """
        Wrapper for D4Root.upgradeMeRequest raw getter
        :rtype: 
        :param ct_type: uint8
        :param my_revision: uint32
        :param my_hash: uint256
        """
        return self.C_.call_getter_raw('upgradeMeRequest', {'ct_type': ct_type, 'my_revision': my_revision, 'my_hash': my_hash}, expect_ec=ts4_expect_ec)

    def M_upgradeMeRequest(self, ct_type, my_revision, my_hash, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.upgradeMeRequest method call
        :param ct_type: uint8
        :param my_revision: uint32
        :param my_hash: uint256
        """
        _r_ = self.C_.call_method('upgradeMeRequest', {'ct_type': ct_type, 'my_revision': my_revision, 'my_hash': my_hash}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgradeMeRequest(self, ct_type, my_revision, my_hash, ts4_expect_ec=0):
        """
        Wrapper for D4Root.upgradeMeRequest signed method call
        :param ct_type: uint8
        :param my_revision: uint32
        :param my_hash: uint256
        """
        _r_ = self.C_.call_method_signed('upgradeMeRequest', {'ct_type': ct_type, 'my_revision': my_revision, 'my_hash': my_hash}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def assignSmvContract(self, smv_addr, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.assignSmvContract
        :rtype: 
        :param smv_addr: address
        """
        if ts4_sign:
            return self.S_assignSmvContract(smv_addr, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_assignSmvContract(smv_addr, ts4_expect_ec=ts4_expect_ec)

    def G_assignSmvContract(self, smv_addr, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.assignSmvContract getter
        :rtype: 
        :param smv_addr: address
        """
        return self.C_.call_getter('assignSmvContract', {'smv_addr': smv_addr}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_assignSmvContract(self, smv_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Root.assignSmvContract raw getter
        :rtype: 
        :param smv_addr: address
        """
        return self.C_.call_getter_raw('assignSmvContract', {'smv_addr': smv_addr}, expect_ec=ts4_expect_ec)

    def M_assignSmvContract(self, smv_addr, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.assignSmvContract method call
        :param smv_addr: address
        """
        _r_ = self.C_.call_method('assignSmvContract', {'smv_addr': smv_addr}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_assignSmvContract(self, smv_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Root.assignSmvContract signed method call
        :param smv_addr: address
        """
        _r_ = self.C_.call_method_signed('assignSmvContract', {'smv_addr': smv_addr}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def restrictAuctions(self, until, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.restrictAuctions
        :rtype: 
        :param until: uint32
        """
        if ts4_sign:
            return self.S_restrictAuctions(until, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_restrictAuctions(until, ts4_expect_ec=ts4_expect_ec)

    def G_restrictAuctions(self, until, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.restrictAuctions getter
        :rtype: 
        :param until: uint32
        """
        return self.C_.call_getter('restrictAuctions', {'until': until}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_restrictAuctions(self, until, ts4_expect_ec=0):
        """
        Wrapper for D4Root.restrictAuctions raw getter
        :rtype: 
        :param until: uint32
        """
        return self.C_.call_getter_raw('restrictAuctions', {'until': until}, expect_ec=ts4_expect_ec)

    def M_restrictAuctions(self, until, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.restrictAuctions method call
        :param until: uint32
        """
        _r_ = self.C_.call_method('restrictAuctions', {'until': until}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_restrictAuctions(self, until, ts4_expect_ec=0):
        """
        Wrapper for D4Root.restrictAuctions signed method call
        :param until: uint32
        """
        _r_ = self.C_.call_method_signed('restrictAuctions', {'until': until}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getOwner(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.getOwner
        :rtype: address
        :param _answer_id: uint32
        """
        return self.G_getOwner(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getOwner(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.getOwner getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getOwner', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.getOwner raw getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getOwner(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.getOwner method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getOwner', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.getOwner signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def getPendingOwner(self, _answer_id=0, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.getPendingOwner
        :rtype: address
        :param _answer_id: uint32
        """
        return self.G_getPendingOwner(_answer_id=0, ts4_expect_ec=ts4_expect_ec)

    def G_getPendingOwner(self, _answer_id=0, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.getPendingOwner getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter('getPendingOwner', {'_answer_id': _answer_id}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_getPendingOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.getPendingOwner raw getter
        :rtype: address
        :param _answer_id: uint32
        """
        return self.C_.call_getter_raw('getPendingOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)

    def M_getPendingOwner(self, _answer_id=0, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.getPendingOwner method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method('getPendingOwner', {'_answer_id': _answer_id}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_getPendingOwner(self, _answer_id=0, ts4_expect_ec=0):
        """
        Wrapper for D4Root.getPendingOwner signed method call
        :param _answer_id: uint32
        """
        _r_ = self.C_.call_method_signed('getPendingOwner', {'_answer_id': _answer_id}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def transferOwner(self, new_owner, deadline, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.transferOwner
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        if ts4_sign:
            return self.S_transferOwner(new_owner, deadline, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_transferOwner(new_owner, deadline, ts4_expect_ec=ts4_expect_ec)

    def G_transferOwner(self, new_owner, deadline, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.transferOwner getter
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_transferOwner(self, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Root.transferOwner raw getter
        :rtype: 
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter_raw('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)

    def M_transferOwner(self, new_owner, deadline, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.transferOwner method call
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_transferOwner(self, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Root.transferOwner signed method call
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method_signed('transferOwner', {'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def cancelTransferOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.cancelTransferOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_cancelTransferOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_cancelTransferOwner(ts4_expect_ec=ts4_expect_ec)

    def G_cancelTransferOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.cancelTransferOwner getter
        :rtype: 
        """
        return self.C_.call_getter('cancelTransferOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_cancelTransferOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.cancelTransferOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('cancelTransferOwner', {}, expect_ec=ts4_expect_ec)

    def M_cancelTransferOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.cancelTransferOwner method call
        """
        _r_ = self.C_.call_method('cancelTransferOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_cancelTransferOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.cancelTransferOwner signed method call
        """
        _r_ = self.C_.call_method_signed('cancelTransferOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def acceptTransfer(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.acceptTransfer
        :rtype: 
        """
        if ts4_sign:
            return self.S_acceptTransfer(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_acceptTransfer(ts4_expect_ec=ts4_expect_ec)

    def G_acceptTransfer(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.acceptTransfer getter
        :rtype: 
        """
        return self.C_.call_getter('acceptTransfer', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_acceptTransfer(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.acceptTransfer raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('acceptTransfer', {}, expect_ec=ts4_expect_ec)

    def M_acceptTransfer(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.acceptTransfer method call
        """
        _r_ = self.C_.call_method('acceptTransfer', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_acceptTransfer(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.acceptTransfer signed method call
        """
        _r_ = self.C_.call_method_signed('acceptTransfer', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def relinquishOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.relinquishOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_relinquishOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_relinquishOwner(ts4_expect_ec=ts4_expect_ec)

    def G_relinquishOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.relinquishOwner getter
        :rtype: 
        """
        return self.C_.call_getter('relinquishOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_relinquishOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.relinquishOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('relinquishOwner', {}, expect_ec=ts4_expect_ec)

    def M_relinquishOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.relinquishOwner method call
        """
        _r_ = self.C_.call_method('relinquishOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_relinquishOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.relinquishOwner signed method call
        """
        _r_ = self.C_.call_method_signed('relinquishOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdrawable(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.withdrawable
        :rtype: uint128
        """
        return self.G_withdrawable(ts4_expect_ec=ts4_expect_ec)

    def G_withdrawable(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.withdrawable getter
        :rtype: uint128
        """
        return self.C_.call_getter('withdrawable', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.withdrawable raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('withdrawable', {}, expect_ec=ts4_expect_ec)

    def M_withdrawable(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.withdrawable method call
        """
        _r_ = self.C_.call_method('withdrawable', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.withdrawable signed method call
        """
        _r_ = self.C_.call_method_signed('withdrawable', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdraw(self, dest, value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.withdraw
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        if ts4_sign:
            return self.S_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)

    def G_withdraw(self, dest, value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.withdraw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter('withdraw', {'dest': dest, 'value': value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4Root.withdraw raw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter_raw('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)

    def M_withdraw(self, dest, value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.withdraw method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method('withdraw', {'dest': dest, 'value': value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4Root.withdraw signed method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method_signed('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_version(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.m_version
        :rtype: uint16
        """
        return self.G_m_version(ts4_expect_ec=ts4_expect_ec)

    def G_m_version(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.m_version getter
        :rtype: uint16
        """
        return self.C_.call_getter('m_version', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.m_version raw getter
        :rtype: uint16
        """
        return self.C_.call_getter_raw('m_version', {}, expect_ec=ts4_expect_ec)

    def M_m_version(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.m_version method call
        """
        _r_ = self.C_.call_method('m_version', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.m_version signed method call
        """
        _r_ = self.C_.call_method_signed('m_version', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.base_code
        :rtype: cell
        """
        return self.G_base_code(ts4_expect_ec=ts4_expect_ec)

    def G_base_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.base_code getter
        :rtype: cell
        """
        return self.C_.call_getter('base_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.base_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('base_code', {}, expect_ec=ts4_expect_ec)

    def M_base_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.base_code method call
        """
        _r_ = self.C_.call_method('base_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.base_code signed method call
        """
        _r_ = self.C_.call_method_signed('base_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certificate_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.certificate_code
        :rtype: cell
        """
        return self.G_certificate_code(ts4_expect_ec=ts4_expect_ec)

    def G_certificate_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.certificate_code getter
        :rtype: cell
        """
        return self.C_.call_getter('certificate_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certificate_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.certificate_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('certificate_code', {}, expect_ec=ts4_expect_ec)

    def M_certificate_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.certificate_code method call
        """
        _r_ = self.C_.call_method('certificate_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certificate_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.certificate_code signed method call
        """
        _r_ = self.C_.call_method_signed('certificate_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auction_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.auction_code
        :rtype: cell
        """
        return self.G_auction_code(ts4_expect_ec=ts4_expect_ec)

    def G_auction_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.auction_code getter
        :rtype: cell
        """
        return self.C_.call_getter('auction_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auction_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.auction_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('auction_code', {}, expect_ec=ts4_expect_ec)

    def M_auction_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.auction_code method call
        """
        _r_ = self.C_.call_method('auction_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auction_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.auction_code signed method call
        """
        _r_ = self.C_.call_method_signed('auction_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def user_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.user_code
        :rtype: cell
        """
        return self.G_user_code(ts4_expect_ec=ts4_expect_ec)

    def G_user_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.user_code getter
        :rtype: cell
        """
        return self.C_.call_getter('user_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_user_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.user_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('user_code', {}, expect_ec=ts4_expect_ec)

    def M_user_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.user_code method call
        """
        _r_ = self.C_.call_method('user_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_user_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.user_code signed method call
        """
        _r_ = self.C_.call_method_signed('user_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.base_revision
        :rtype: uint32
        """
        return self.G_base_revision(ts4_expect_ec=ts4_expect_ec)

    def G_base_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.base_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('base_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.base_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('base_revision', {}, expect_ec=ts4_expect_ec)

    def M_base_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.base_revision method call
        """
        _r_ = self.C_.call_method('base_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.base_revision signed method call
        """
        _r_ = self.C_.call_method_signed('base_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certificate_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.certificate_revision
        :rtype: uint32
        """
        return self.G_certificate_revision(ts4_expect_ec=ts4_expect_ec)

    def G_certificate_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.certificate_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('certificate_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certificate_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.certificate_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('certificate_revision', {}, expect_ec=ts4_expect_ec)

    def M_certificate_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.certificate_revision method call
        """
        _r_ = self.C_.call_method('certificate_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certificate_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.certificate_revision signed method call
        """
        _r_ = self.C_.call_method_signed('certificate_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auction_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.auction_revision
        :rtype: uint32
        """
        return self.G_auction_revision(ts4_expect_ec=ts4_expect_ec)

    def G_auction_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.auction_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('auction_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auction_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.auction_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('auction_revision', {}, expect_ec=ts4_expect_ec)

    def M_auction_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.auction_revision method call
        """
        _r_ = self.C_.call_method('auction_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auction_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.auction_revision signed method call
        """
        _r_ = self.C_.call_method_signed('auction_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def user_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.user_revision
        :rtype: uint32
        """
        return self.G_user_revision(ts4_expect_ec=ts4_expect_ec)

    def G_user_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.user_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('user_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_user_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.user_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('user_revision', {}, expect_ec=ts4_expect_ec)

    def M_user_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.user_revision method call
        """
        _r_ = self.C_.call_method('user_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_user_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.user_revision signed method call
        """
        _r_ = self.C_.call_method_signed('user_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def owner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.owner
        :rtype: address
        """
        return self.G_owner(ts4_expect_ec=ts4_expect_ec)

    def G_owner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.owner getter
        :rtype: address
        """
        return self.C_.call_getter('owner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.owner raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('owner', {}, expect_ec=ts4_expect_ec)

    def M_owner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.owner method call
        """
        _r_ = self.C_.call_method('owner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.owner signed method call
        """
        _r_ = self.C_.call_method_signed('owner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def pending_owner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.pending_owner
        :rtype: address
        """
        return self.G_pending_owner(ts4_expect_ec=ts4_expect_ec)

    def G_pending_owner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.pending_owner getter
        :rtype: address
        """
        return self.C_.call_getter('pending_owner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_pending_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.pending_owner raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('pending_owner', {}, expect_ec=ts4_expect_ec)

    def M_pending_owner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.pending_owner method call
        """
        _r_ = self.C_.call_method('pending_owner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_pending_owner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.pending_owner signed method call
        """
        _r_ = self.C_.call_method_signed('pending_owner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def owner_transfer_deadline(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.owner_transfer_deadline
        :rtype: uint32
        """
        return self.G_owner_transfer_deadline(ts4_expect_ec=ts4_expect_ec)

    def G_owner_transfer_deadline(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.owner_transfer_deadline getter
        :rtype: uint32
        """
        return self.C_.call_getter('owner_transfer_deadline', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_owner_transfer_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.owner_transfer_deadline raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('owner_transfer_deadline', {}, expect_ec=ts4_expect_ec)

    def M_owner_transfer_deadline(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.owner_transfer_deadline method call
        """
        _r_ = self.C_.call_method('owner_transfer_deadline', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_owner_transfer_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.owner_transfer_deadline signed method call
        """
        _r_ = self.C_.call_method_signed('owner_transfer_deadline', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def relinquish_owner_deadline(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.relinquish_owner_deadline
        :rtype: uint32
        """
        return self.G_relinquish_owner_deadline(ts4_expect_ec=ts4_expect_ec)

    def G_relinquish_owner_deadline(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.relinquish_owner_deadline getter
        :rtype: uint32
        """
        return self.C_.call_getter('relinquish_owner_deadline', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_relinquish_owner_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.relinquish_owner_deadline raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('relinquish_owner_deadline', {}, expect_ec=ts4_expect_ec)

    def M_relinquish_owner_deadline(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.relinquish_owner_deadline method call
        """
        _r_ = self.C_.call_method('relinquish_owner_deadline', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_relinquish_owner_deadline(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.relinquish_owner_deadline signed method call
        """
        _r_ = self.C_.call_method_signed('relinquish_owner_deadline', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def smv_root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.smv_root
        :rtype: address
        """
        return self.G_smv_root(ts4_expect_ec=ts4_expect_ec)

    def G_smv_root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.smv_root getter
        :rtype: address
        """
        return self.C_.call_getter('smv_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_smv_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.smv_root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('smv_root', {}, expect_ec=ts4_expect_ec)

    def M_smv_root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.smv_root method call
        """
        _r_ = self.C_.call_method('smv_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_smv_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.smv_root signed method call
        """
        _r_ = self.C_.call_method_signed('smv_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def no_auctions_until(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.no_auctions_until
        :rtype: uint32
        """
        return self.G_no_auctions_until(ts4_expect_ec=ts4_expect_ec)

    def G_no_auctions_until(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.no_auctions_until getter
        :rtype: uint32
        """
        return self.C_.call_getter('no_auctions_until', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_no_auctions_until(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.no_auctions_until raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('no_auctions_until', {}, expect_ec=ts4_expect_ec)

    def M_no_auctions_until(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.no_auctions_until method call
        """
        _r_ = self.C_.call_method('no_auctions_until', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_no_auctions_until(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.no_auctions_until signed method call
        """
        _r_ = self.C_.call_method_signed('no_auctions_until', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def admin_enabled(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Root.admin_enabled
        :rtype: uint8
        """
        return self.G_admin_enabled(ts4_expect_ec=ts4_expect_ec)

    def G_admin_enabled(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Root.admin_enabled getter
        :rtype: uint8
        """
        return self.C_.call_getter('admin_enabled', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_admin_enabled(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.admin_enabled raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('admin_enabled', {}, expect_ec=ts4_expect_ec)

    def M_admin_enabled(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Root.admin_enabled method call
        """
        _r_ = self.C_.call_method('admin_enabled', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_admin_enabled(self, ts4_expect_ec=0):
        """
        Wrapper for D4Root.admin_enabled signed method call
        """
        _r_ = self.C_.call_method_signed('admin_enabled', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4Test(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, root, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.constructor
        :rtype: 
        :param root: address
        """
        if ts4_sign:
            return self.S_constructor(root, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(root, ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, root, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.constructor getter
        :rtype: 
        :param root: address
        """
        return self.C_.call_getter('constructor', {'root': root}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, root, ts4_expect_ec=0):
        """
        Wrapper for D4Test.constructor raw getter
        :rtype: 
        :param root: address
        """
        return self.C_.call_getter_raw('constructor', {'root': root}, expect_ec=ts4_expect_ec)

    def M_constructor(self, root, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.constructor method call
        :param root: address
        """
        _r_ = self.C_.call_method('constructor', {'root': root}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, root, ts4_expect_ec=0):
        """
        Wrapper for D4Test.constructor signed method call
        :param root: address
        """
        _r_ = self.C_.call_method_signed('constructor', {'root': root}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def makeIntUser(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.makeIntUser
        :rtype: 
        """
        if ts4_sign:
            return self.S_makeIntUser(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_makeIntUser(ts4_expect_ec=ts4_expect_ec)

    def G_makeIntUser(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.makeIntUser getter
        :rtype: 
        """
        return self.C_.call_getter('makeIntUser', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_makeIntUser(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeIntUser raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('makeIntUser', {}, expect_ec=ts4_expect_ec)

    def M_makeIntUser(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.makeIntUser method call
        """
        _r_ = self.C_.call_method('makeIntUser', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_makeIntUser(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeIntUser signed method call
        """
        _r_ = self.C_.call_method_signed('makeIntUser', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def makeExtUser(self, pk, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.makeExtUser
        :rtype: 
        :param pk: uint256
        """
        if ts4_sign:
            return self.S_makeExtUser(pk, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_makeExtUser(pk, ts4_expect_ec=ts4_expect_ec)

    def G_makeExtUser(self, pk, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.makeExtUser getter
        :rtype: 
        :param pk: uint256
        """
        return self.C_.call_getter('makeExtUser', {'pk': pk}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_makeExtUser(self, pk, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeExtUser raw getter
        :rtype: 
        :param pk: uint256
        """
        return self.C_.call_getter_raw('makeExtUser', {'pk': pk}, expect_ec=ts4_expect_ec)

    def M_makeExtUser(self, pk, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.makeExtUser method call
        :param pk: uint256
        """
        _r_ = self.C_.call_method('makeExtUser', {'pk': pk}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_makeExtUser(self, pk, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeExtUser signed method call
        :param pk: uint256
        """
        _r_ = self.C_.call_method_signed('makeExtUser', {'pk': pk}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def addressCallbackInt(self, user_addr, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.addressCallbackInt
        :rtype: 
        :param user_addr: address
        """
        if ts4_sign:
            return self.S_addressCallbackInt(user_addr, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_addressCallbackInt(user_addr, ts4_expect_ec=ts4_expect_ec)

    def G_addressCallbackInt(self, user_addr, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.addressCallbackInt getter
        :rtype: 
        :param user_addr: address
        """
        return self.C_.call_getter('addressCallbackInt', {'user_addr': user_addr}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_addressCallbackInt(self, user_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addressCallbackInt raw getter
        :rtype: 
        :param user_addr: address
        """
        return self.C_.call_getter_raw('addressCallbackInt', {'user_addr': user_addr}, expect_ec=ts4_expect_ec)

    def M_addressCallbackInt(self, user_addr, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.addressCallbackInt method call
        :param user_addr: address
        """
        _r_ = self.C_.call_method('addressCallbackInt', {'user_addr': user_addr}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_addressCallbackInt(self, user_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addressCallbackInt signed method call
        :param user_addr: address
        """
        _r_ = self.C_.call_method_signed('addressCallbackInt', {'user_addr': user_addr}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def addressCallbackExt(self, user_addr, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.addressCallbackExt
        :rtype: 
        :param user_addr: address
        """
        if ts4_sign:
            return self.S_addressCallbackExt(user_addr, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_addressCallbackExt(user_addr, ts4_expect_ec=ts4_expect_ec)

    def G_addressCallbackExt(self, user_addr, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.addressCallbackExt getter
        :rtype: 
        :param user_addr: address
        """
        return self.C_.call_getter('addressCallbackExt', {'user_addr': user_addr}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_addressCallbackExt(self, user_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addressCallbackExt raw getter
        :rtype: 
        :param user_addr: address
        """
        return self.C_.call_getter_raw('addressCallbackExt', {'user_addr': user_addr}, expect_ec=ts4_expect_ec)

    def M_addressCallbackExt(self, user_addr, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.addressCallbackExt method call
        :param user_addr: address
        """
        _r_ = self.C_.call_method('addressCallbackExt', {'user_addr': user_addr}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_addressCallbackExt(self, user_addr, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addressCallbackExt signed method call
        :param user_addr: address
        """
        _r_ = self.C_.call_method_signed('addressCallbackExt', {'user_addr': user_addr}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def addLocked(self, until, name, parent, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.addLocked
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        if ts4_sign:
            return self.S_addLocked(until, name, parent, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_addLocked(until, name, parent, ts4_expect_ec=ts4_expect_ec)

    def G_addLocked(self, until, name, parent, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.addLocked getter
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter('addLocked', {'until': until, 'name': name, 'parent': parent}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_addLocked(self, until, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addLocked raw getter
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter_raw('addLocked', {'until': until, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)

    def M_addLocked(self, until, name, parent, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.addLocked method call
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method('addLocked', {'until': until, 'name': name, 'parent': parent}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_addLocked(self, until, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4Test.addLocked signed method call
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method_signed('addLocked', {'until': until, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestUpgrade(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.requestUpgrade
        :rtype: 
        """
        if ts4_sign:
            return self.S_requestUpgrade(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestUpgrade(ts4_expect_ec=ts4_expect_ec)

    def G_requestUpgrade(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.requestUpgrade getter
        :rtype: 
        """
        return self.C_.call_getter('requestUpgrade', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.requestUpgrade raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('requestUpgrade', {}, expect_ec=ts4_expect_ec)

    def M_requestUpgrade(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.requestUpgrade method call
        """
        _r_ = self.C_.call_method('requestUpgrade', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.requestUpgrade signed method call
        """
        _r_ = self.C_.call_method_signed('requestUpgrade', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def sweepLocks(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.sweepLocks
        :rtype: 
        """
        if ts4_sign:
            return self.S_sweepLocks(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_sweepLocks(ts4_expect_ec=ts4_expect_ec)

    def G_sweepLocks(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.sweepLocks getter
        :rtype: 
        """
        return self.C_.call_getter('sweepLocks', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_sweepLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.sweepLocks raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('sweepLocks', {}, expect_ec=ts4_expect_ec)

    def M_sweepLocks(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.sweepLocks method call
        """
        _r_ = self.C_.call_method('sweepLocks', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_sweepLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.sweepLocks signed method call
        """
        _r_ = self.C_.call_method_signed('sweepLocks', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdraw(self, dest, value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.withdraw
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        if ts4_sign:
            return self.S_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)

    def G_withdraw(self, dest, value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.withdraw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter('withdraw', {'dest': dest, 'value': value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.withdraw raw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter_raw('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)

    def M_withdraw(self, dest, value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.withdraw method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method('withdraw', {'dest': dest, 'value': value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.withdraw signed method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method_signed('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def pull(self, value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.pull
        :rtype: 
        :param value: uint128
        """
        if ts4_sign:
            return self.S_pull(value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_pull(value, ts4_expect_ec=ts4_expect_ec)

    def G_pull(self, value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.pull getter
        :rtype: 
        :param value: uint128
        """
        return self.C_.call_getter('pull', {'value': value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_pull(self, value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.pull raw getter
        :rtype: 
        :param value: uint128
        """
        return self.C_.call_getter_raw('pull', {'value': value}, expect_ec=ts4_expect_ec)

    def M_pull(self, value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.pull method call
        :param value: uint128
        """
        _r_ = self.C_.call_method('pull', {'value': value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_pull(self, value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.pull signed method call
        :param value: uint128
        """
        _r_ = self.C_.call_method_signed('pull', {'value': value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdrawable(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.withdrawable
        :rtype: uint128
        """
        return self.G_withdrawable(ts4_expect_ec=ts4_expect_ec)

    def G_withdrawable(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.withdrawable getter
        :rtype: uint128
        """
        return self.C_.call_getter('withdrawable', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.withdrawable raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('withdrawable', {}, expect_ec=ts4_expect_ec)

    def M_withdrawable(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.withdrawable method call
        """
        _r_ = self.C_.call_method('withdrawable', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.withdrawable signed method call
        """
        _r_ = self.C_.call_method_signed('withdrawable', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setMasterKey(self, newMasterKey, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.setMasterKey
        :rtype: 
        :param newMasterKey: bytes
        """
        if ts4_sign:
            return self.S_setMasterKey(newMasterKey, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setMasterKey(newMasterKey, ts4_expect_ec=ts4_expect_ec)

    def G_setMasterKey(self, newMasterKey, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.setMasterKey getter
        :rtype: 
        :param newMasterKey: bytes
        """
        return self.C_.call_getter('setMasterKey', {'newMasterKey': newMasterKey}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setMasterKey(self, newMasterKey, ts4_expect_ec=0):
        """
        Wrapper for D4Test.setMasterKey raw getter
        :rtype: 
        :param newMasterKey: bytes
        """
        return self.C_.call_getter_raw('setMasterKey', {'newMasterKey': newMasterKey}, expect_ec=ts4_expect_ec)

    def M_setMasterKey(self, newMasterKey, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.setMasterKey method call
        :param newMasterKey: bytes
        """
        _r_ = self.C_.call_method('setMasterKey', {'newMasterKey': newMasterKey}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setMasterKey(self, newMasterKey, ts4_expect_ec=0):
        """
        Wrapper for D4Test.setMasterKey signed method call
        :param newMasterKey: bytes
        """
        _r_ = self.C_.call_method_signed('setMasterKey', {'newMasterKey': newMasterKey}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def createAuction(self, name, duration, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.createAuction
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        if ts4_sign:
            return self.S_createAuction(name, duration, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_createAuction(name, duration, ts4_expect_ec=ts4_expect_ec)

    def G_createAuction(self, name, duration, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.createAuction getter
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter('createAuction', {'name': name, 'duration': duration}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_createAuction(self, name, duration, ts4_expect_ec=0):
        """
        Wrapper for D4Test.createAuction raw getter
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter_raw('createAuction', {'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)

    def M_createAuction(self, name, duration, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.createAuction method call
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method('createAuction', {'name': name, 'duration': duration}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_createAuction(self, name, duration, ts4_expect_ec=0):
        """
        Wrapper for D4Test.createAuction signed method call
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method_signed('createAuction', {'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def makeBid(self, auction, data, hash, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.makeBid
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        if ts4_sign:
            return self.S_makeBid(auction, data, hash, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_makeBid(auction, data, hash, ts4_expect_ec=ts4_expect_ec)

    def G_makeBid(self, auction, data, hash, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.makeBid getter
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        return self.C_.call_getter('makeBid', {'auction': auction, 'data': data, 'hash': hash}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_makeBid(self, auction, data, hash, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeBid raw getter
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        return self.C_.call_getter_raw('makeBid', {'auction': auction, 'data': data, 'hash': hash}, expect_ec=ts4_expect_ec)

    def M_makeBid(self, auction, data, hash, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.makeBid method call
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        _r_ = self.C_.call_method('makeBid', {'auction': auction, 'data': data, 'hash': hash}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_makeBid(self, auction, data, hash, ts4_expect_ec=0):
        """
        Wrapper for D4Test.makeBid signed method call
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        _r_ = self.C_.call_method_signed('makeBid', {'auction': auction, 'data': data, 'hash': hash}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def revealBid(self, auction, amount, nonce, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.revealBid
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        if ts4_sign:
            return self.S_revealBid(auction, amount, nonce, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_revealBid(auction, amount, nonce, ts4_expect_ec=ts4_expect_ec)

    def G_revealBid(self, auction, amount, nonce, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.revealBid getter
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_revealBid(self, auction, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4Test.revealBid raw getter
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter_raw('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)

    def M_revealBid(self, auction, amount, nonce, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.revealBid method call
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_revealBid(self, auction, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4Test.revealBid signed method call
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method_signed('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def bidRevealComplete(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.bidRevealComplete
        :rtype: 
        """
        if ts4_sign:
            return self.S_bidRevealComplete(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_bidRevealComplete(ts4_expect_ec=ts4_expect_ec)

    def G_bidRevealComplete(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.bidRevealComplete getter
        :rtype: 
        """
        return self.C_.call_getter('bidRevealComplete', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_bidRevealComplete(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.bidRevealComplete raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('bidRevealComplete', {}, expect_ec=ts4_expect_ec)

    def M_bidRevealComplete(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.bidRevealComplete method call
        """
        _r_ = self.C_.call_method('bidRevealComplete', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_bidRevealComplete(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.bidRevealComplete signed method call
        """
        _r_ = self.C_.call_method_signed('bidRevealComplete', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def finalize(self, auction, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.finalize
        :rtype: 
        :param auction: address
        """
        if ts4_sign:
            return self.S_finalize(auction, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_finalize(auction, ts4_expect_ec=ts4_expect_ec)

    def G_finalize(self, auction, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.finalize getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter('finalize', {'auction': auction}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_finalize(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4Test.finalize raw getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter_raw('finalize', {'auction': auction}, expect_ec=ts4_expect_ec)

    def M_finalize(self, auction, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.finalize method call
        :param auction: address
        """
        _r_ = self.C_.call_method('finalize', {'auction': auction}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_finalize(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4Test.finalize signed method call
        :param auction: address
        """
        _r_ = self.C_.call_method_signed('finalize', {'auction': auction}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryCert(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.queryCert
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_queryCert(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryCert(target, ts4_expect_ec=ts4_expect_ec)

    def G_queryCert(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.queryCert getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('queryCert', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryCert raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('queryCert', {'target': target}, expect_ec=ts4_expect_ec)

    def M_queryCert(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.queryCert method call
        :param target: address
        """
        _r_ = self.C_.call_method('queryCert', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryCert signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('queryCert', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryAuct(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.queryAuct
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_queryAuct(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryAuct(target, ts4_expect_ec=ts4_expect_ec)

    def G_queryAuct(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.queryAuct getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('queryAuct', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryAuct raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('queryAuct', {'target': target}, expect_ec=ts4_expect_ec)

    def M_queryAuct(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.queryAuct method call
        :param target: address
        """
        _r_ = self.C_.call_method('queryAuct', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryAuct signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('queryAuct', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def forgetCert(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.forgetCert
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_forgetCert(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_forgetCert(target, ts4_expect_ec=ts4_expect_ec)

    def G_forgetCert(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.forgetCert getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('forgetCert', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_forgetCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.forgetCert raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('forgetCert', {'target': target}, expect_ec=ts4_expect_ec)

    def M_forgetCert(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.forgetCert method call
        :param target: address
        """
        _r_ = self.C_.call_method('forgetCert', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_forgetCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.forgetCert signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('forgetCert', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def forgetAuct(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.forgetAuct
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_forgetAuct(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_forgetAuct(target, ts4_expect_ec=ts4_expect_ec)

    def G_forgetAuct(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.forgetAuct getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('forgetAuct', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_forgetAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.forgetAuct raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('forgetAuct', {'target': target}, expect_ec=ts4_expect_ec)

    def M_forgetAuct(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.forgetAuct method call
        :param target: address
        """
        _r_ = self.C_.call_method('forgetAuct', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_forgetAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.forgetAuct signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('forgetAuct', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setValue(self, target, index, new_value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.setValue
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        if ts4_sign:
            return self.S_setValue(target, index, new_value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setValue(target, index, new_value, ts4_expect_ec=ts4_expect_ec)

    def G_setValue(self, target, index, new_value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.setValue getter
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter('setValue', {'target': target, 'index': index, 'new_value': new_value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setValue(self, target, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.setValue raw getter
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter_raw('setValue', {'target': target, 'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)

    def M_setValue(self, target, index, new_value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.setValue method call
        :param target: address
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method('setValue', {'target': target, 'index': index, 'new_value': new_value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setValue(self, target, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4Test.setValue signed method call
        :param target: address
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method_signed('setValue', {'target': target, 'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resetValue(self, target, index, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.resetValue
        :rtype: 
        :param target: address
        :param index: int16
        """
        if ts4_sign:
            return self.S_resetValue(target, index, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_resetValue(target, index, ts4_expect_ec=ts4_expect_ec)

    def G_resetValue(self, target, index, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.resetValue getter
        :rtype: 
        :param target: address
        :param index: int16
        """
        return self.C_.call_getter('resetValue', {'target': target, 'index': index}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resetValue(self, target, index, ts4_expect_ec=0):
        """
        Wrapper for D4Test.resetValue raw getter
        :rtype: 
        :param target: address
        :param index: int16
        """
        return self.C_.call_getter_raw('resetValue', {'target': target, 'index': index}, expect_ec=ts4_expect_ec)

    def M_resetValue(self, target, index, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.resetValue method call
        :param target: address
        :param index: int16
        """
        _r_ = self.C_.call_method('resetValue', {'target': target, 'index': index}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resetValue(self, target, index, ts4_expect_ec=0):
        """
        Wrapper for D4Test.resetValue signed method call
        :param target: address
        :param index: int16
        """
        _r_ = self.C_.call_method_signed('resetValue', {'target': target, 'index': index}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def clearValues(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.clearValues
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_clearValues(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_clearValues(target, ts4_expect_ec=ts4_expect_ec)

    def G_clearValues(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.clearValues getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('clearValues', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_clearValues(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.clearValues raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('clearValues', {'target': target}, expect_ec=ts4_expect_ec)

    def M_clearValues(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.clearValues method call
        :param target: address
        """
        _r_ = self.C_.call_method('clearValues', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_clearValues(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.clearValues signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('clearValues', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certWithdrawExcess(self, target, amount, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certWithdrawExcess
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        if ts4_sign:
            return self.S_certWithdrawExcess(target, amount, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certWithdrawExcess(target, amount, ts4_expect_ec=ts4_expect_ec)

    def G_certWithdrawExcess(self, target, amount, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certWithdrawExcess getter
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        return self.C_.call_getter('certWithdrawExcess', {'target': target, 'amount': amount}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certWithdrawExcess(self, target, amount, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certWithdrawExcess raw getter
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        return self.C_.call_getter_raw('certWithdrawExcess', {'target': target, 'amount': amount}, expect_ec=ts4_expect_ec)

    def M_certWithdrawExcess(self, target, amount, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certWithdrawExcess method call
        :param target: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method('certWithdrawExcess', {'target': target, 'amount': amount}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certWithdrawExcess(self, target, amount, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certWithdrawExcess signed method call
        :param target: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method_signed('certWithdrawExcess', {'target': target, 'amount': amount}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certRequestUpgrade(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certRequestUpgrade
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certRequestUpgrade(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certRequestUpgrade(target, ts4_expect_ec=ts4_expect_ec)

    def G_certRequestUpgrade(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certRequestUpgrade getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certRequestUpgrade', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certRequestUpgrade(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certRequestUpgrade raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certRequestUpgrade', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certRequestUpgrade(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certRequestUpgrade method call
        :param target: address
        """
        _r_ = self.C_.call_method('certRequestUpgrade', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certRequestUpgrade(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certRequestUpgrade signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certRequestUpgrade', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestProlong(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.requestProlong
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_requestProlong(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestProlong(target, ts4_expect_ec=ts4_expect_ec)

    def G_requestProlong(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.requestProlong getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('requestProlong', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestProlong(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.requestProlong raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('requestProlong', {'target': target}, expect_ec=ts4_expect_ec)

    def M_requestProlong(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.requestProlong method call
        :param target: address
        """
        _r_ = self.C_.call_method('requestProlong', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestProlong(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.requestProlong signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('requestProlong', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def deploySub(self, target, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.deploySub
        :rtype: 
        :param target: address
        :param name: bytes
        """
        if ts4_sign:
            return self.S_deploySub(target, name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_deploySub(target, name, ts4_expect_ec=ts4_expect_ec)

    def G_deploySub(self, target, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.deploySub getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter('deploySub', {'target': target, 'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_deploySub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4Test.deploySub raw getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter_raw('deploySub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)

    def M_deploySub(self, target, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.deploySub method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method('deploySub', {'target': target, 'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_deploySub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4Test.deploySub signed method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('deploySub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def syncSub(self, target, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.syncSub
        :rtype: 
        :param target: address
        :param name: bytes
        """
        if ts4_sign:
            return self.S_syncSub(target, name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_syncSub(target, name, ts4_expect_ec=ts4_expect_ec)

    def G_syncSub(self, target, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.syncSub getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter('syncSub', {'target': target, 'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_syncSub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4Test.syncSub raw getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter_raw('syncSub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)

    def M_syncSub(self, target, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.syncSub method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method('syncSub', {'target': target, 'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_syncSub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4Test.syncSub signed method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('syncSub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryCertCallback(self, info, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.queryCertCallback
        :rtype: 
        :param info: tuple
        """
        if ts4_sign:
            return self.S_queryCertCallback(info, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryCertCallback(info, ts4_expect_ec=ts4_expect_ec)

    def G_queryCertCallback(self, info, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.queryCertCallback getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter('queryCertCallback', {'info': info}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryCertCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryCertCallback raw getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter_raw('queryCertCallback', {'info': info}, expect_ec=ts4_expect_ec)

    def M_queryCertCallback(self, info, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.queryCertCallback method call
        :param info: tuple
        """
        _r_ = self.C_.call_method('queryCertCallback', {'info': info}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryCertCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryCertCallback signed method call
        :param info: tuple
        """
        _r_ = self.C_.call_method_signed('queryCertCallback', {'info': info}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryAuctCallback(self, info, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.queryAuctCallback
        :rtype: 
        :param info: tuple
        """
        if ts4_sign:
            return self.S_queryAuctCallback(info, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryAuctCallback(info, ts4_expect_ec=ts4_expect_ec)

    def G_queryAuctCallback(self, info, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.queryAuctCallback getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter('queryAuctCallback', {'info': info}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryAuctCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryAuctCallback raw getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter_raw('queryAuctCallback', {'info': info}, expect_ec=ts4_expect_ec)

    def M_queryAuctCallback(self, info, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.queryAuctCallback method call
        :param info: tuple
        """
        _r_ = self.C_.call_method('queryAuctCallback', {'info': info}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryAuctCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4Test.queryAuctCallback signed method call
        :param info: tuple
        """
        _r_ = self.C_.call_method_signed('queryAuctCallback', {'info': info}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certTransferOwner
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        if ts4_sign:
            return self.S_certTransferOwner(target, new_owner, deadline, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certTransferOwner(target, new_owner, deadline, ts4_expect_ec=ts4_expect_ec)

    def G_certTransferOwner(self, target, new_owner, deadline, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certTransferOwner getter
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certTransferOwner raw getter
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter_raw('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)

    def M_certTransferOwner(self, target, new_owner, deadline, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certTransferOwner method call
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certTransferOwner signed method call
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method_signed('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certCancelTransferOwner(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certCancelTransferOwner
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certCancelTransferOwner(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certCancelTransferOwner(target, ts4_expect_ec=ts4_expect_ec)

    def G_certCancelTransferOwner(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certCancelTransferOwner getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certCancelTransferOwner', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certCancelTransferOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certCancelTransferOwner raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certCancelTransferOwner', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certCancelTransferOwner(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certCancelTransferOwner method call
        :param target: address
        """
        _r_ = self.C_.call_method('certCancelTransferOwner', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certCancelTransferOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certCancelTransferOwner signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certCancelTransferOwner', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certAcceptTransfer(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certAcceptTransfer
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certAcceptTransfer(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certAcceptTransfer(target, ts4_expect_ec=ts4_expect_ec)

    def G_certAcceptTransfer(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certAcceptTransfer getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certAcceptTransfer', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certAcceptTransfer(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certAcceptTransfer raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certAcceptTransfer', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certAcceptTransfer(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certAcceptTransfer method call
        :param target: address
        """
        _r_ = self.C_.call_method('certAcceptTransfer', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certAcceptTransfer(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certAcceptTransfer signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certAcceptTransfer', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certRelinquishOwner(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.certRelinquishOwner
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certRelinquishOwner(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certRelinquishOwner(target, ts4_expect_ec=ts4_expect_ec)

    def G_certRelinquishOwner(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.certRelinquishOwner getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certRelinquishOwner', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certRelinquishOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certRelinquishOwner raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certRelinquishOwner', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certRelinquishOwner(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.certRelinquishOwner method call
        :param target: address
        """
        _r_ = self.C_.call_method('certRelinquishOwner', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certRelinquishOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4Test.certRelinquishOwner signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certRelinquishOwner', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def passToOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.passToOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_passToOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_passToOwner(ts4_expect_ec=ts4_expect_ec)

    def G_passToOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.passToOwner getter
        :rtype: 
        """
        return self.C_.call_getter('passToOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.passToOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('passToOwner', {}, expect_ec=ts4_expect_ec)

    def M_passToOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.passToOwner method call
        """
        _r_ = self.C_.call_method('passToOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.passToOwner signed method call
        """
        _r_ = self.C_.call_method_signed('passToOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgrade(self, code, revision, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.upgrade
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        if ts4_sign:
            return self.S_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)

    def G_upgrade(self, code, revision, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.upgrade getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter('upgrade', {'code': code, 'revision': revision}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4Test.upgrade raw getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter_raw('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)

    def M_upgrade(self, code, revision, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.upgrade method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method('upgrade', {'code': code, 'revision': revision}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4Test.upgrade signed method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method_signed('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgradeNotNeeded(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.upgradeNotNeeded
        :rtype: 
        """
        if ts4_sign:
            return self.S_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)

    def G_upgradeNotNeeded(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.upgradeNotNeeded getter
        :rtype: 
        """
        return self.C_.call_getter('upgradeNotNeeded', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.upgradeNotNeeded raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)

    def M_upgradeNotNeeded(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.upgradeNotNeeded method call
        """
        _r_ = self.C_.call_method('upgradeNotNeeded', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.upgradeNotNeeded signed method call
        """
        _r_ = self.C_.call_method_signed('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def _root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test._root
        :rtype: address
        """
        return self.G__root(ts4_expect_ec=ts4_expect_ec)

    def G__root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test._root getter
        :rtype: address
        """
        return self.C_.call_getter('_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R__root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test._root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('_root', {}, expect_ec=ts4_expect_ec)

    def M__root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test._root method call
        """
        _r_ = self.C_.call_method('_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S__root(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test._root signed method call
        """
        _r_ = self.C_.call_method_signed('_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def iaddr(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.iaddr
        :rtype: address
        """
        return self.G_iaddr(ts4_expect_ec=ts4_expect_ec)

    def G_iaddr(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.iaddr getter
        :rtype: address
        """
        return self.C_.call_getter('iaddr', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_iaddr(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.iaddr raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('iaddr', {}, expect_ec=ts4_expect_ec)

    def M_iaddr(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.iaddr method call
        """
        _r_ = self.C_.call_method('iaddr', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_iaddr(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.iaddr signed method call
        """
        _r_ = self.C_.call_method_signed('iaddr', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def eaddr(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4Test.eaddr
        :rtype: address
        """
        return self.G_eaddr(ts4_expect_ec=ts4_expect_ec)

    def G_eaddr(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4Test.eaddr getter
        :rtype: address
        """
        return self.C_.call_getter('eaddr', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_eaddr(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.eaddr raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('eaddr', {}, expect_ec=ts4_expect_ec)

    def M_eaddr(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4Test.eaddr method call
        """
        _r_ = self.C_.call_method('eaddr', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_eaddr(self, ts4_expect_ec=0):
        """
        Wrapper for D4Test.eaddr signed method call
        """
        _r_ = self.C_.call_method_signed('eaddr', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins
class WrapD4User(WrapperParentClass):
    def __init__(self, contract):
        self.C_ = contract
        self.A_ = contract.address

    def constructor(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.constructor
        :rtype: 
        """
        if ts4_sign:
            return self.S_constructor(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_constructor(ts4_expect_ec=ts4_expect_ec)

    def G_constructor(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.constructor getter
        :rtype: 
        """
        return self.C_.call_getter('constructor', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.constructor raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('constructor', {}, expect_ec=ts4_expect_ec)

    def M_constructor(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.constructor method call
        """
        _r_ = self.C_.call_method('constructor', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_constructor(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.constructor signed method call
        """
        _r_ = self.C_.call_method_signed('constructor', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setMasterKey(self, newMasterKey, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.setMasterKey
        :rtype: 
        :param newMasterKey: bytes
        """
        if ts4_sign:
            return self.S_setMasterKey(newMasterKey, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setMasterKey(newMasterKey, ts4_expect_ec=ts4_expect_ec)

    def G_setMasterKey(self, newMasterKey, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.setMasterKey getter
        :rtype: 
        :param newMasterKey: bytes
        """
        return self.C_.call_getter('setMasterKey', {'newMasterKey': newMasterKey}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setMasterKey(self, newMasterKey, ts4_expect_ec=0):
        """
        Wrapper for D4User.setMasterKey raw getter
        :rtype: 
        :param newMasterKey: bytes
        """
        return self.C_.call_getter_raw('setMasterKey', {'newMasterKey': newMasterKey}, expect_ec=ts4_expect_ec)

    def M_setMasterKey(self, newMasterKey, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.setMasterKey method call
        :param newMasterKey: bytes
        """
        _r_ = self.C_.call_method('setMasterKey', {'newMasterKey': newMasterKey}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setMasterKey(self, newMasterKey, ts4_expect_ec=0):
        """
        Wrapper for D4User.setMasterKey signed method call
        :param newMasterKey: bytes
        """
        _r_ = self.C_.call_method_signed('setMasterKey', {'newMasterKey': newMasterKey}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestUpgrade(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.requestUpgrade
        :rtype: 
        """
        if ts4_sign:
            return self.S_requestUpgrade(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestUpgrade(ts4_expect_ec=ts4_expect_ec)

    def G_requestUpgrade(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.requestUpgrade getter
        :rtype: 
        """
        return self.C_.call_getter('requestUpgrade', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.requestUpgrade raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('requestUpgrade', {}, expect_ec=ts4_expect_ec)

    def M_requestUpgrade(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.requestUpgrade method call
        """
        _r_ = self.C_.call_method('requestUpgrade', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestUpgrade(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.requestUpgrade signed method call
        """
        _r_ = self.C_.call_method_signed('requestUpgrade', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgrade(self, code, revision, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.upgrade
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        if ts4_sign:
            return self.S_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgrade(code, revision, ts4_expect_ec=ts4_expect_ec)

    def G_upgrade(self, code, revision, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.upgrade getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter('upgrade', {'code': code, 'revision': revision}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4User.upgrade raw getter
        :rtype: 
        :param code: cell
        :param revision: uint32
        """
        return self.C_.call_getter_raw('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)

    def M_upgrade(self, code, revision, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.upgrade method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method('upgrade', {'code': code, 'revision': revision}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgrade(self, code, revision, ts4_expect_ec=0):
        """
        Wrapper for D4User.upgrade signed method call
        :param code: cell
        :param revision: uint32
        """
        _r_ = self.C_.call_method_signed('upgrade', {'code': code, 'revision': revision}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def upgradeNotNeeded(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.upgradeNotNeeded
        :rtype: 
        """
        if ts4_sign:
            return self.S_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_upgradeNotNeeded(ts4_expect_ec=ts4_expect_ec)

    def G_upgradeNotNeeded(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.upgradeNotNeeded getter
        :rtype: 
        """
        return self.C_.call_getter('upgradeNotNeeded', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.upgradeNotNeeded raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)

    def M_upgradeNotNeeded(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.upgradeNotNeeded method call
        """
        _r_ = self.C_.call_method('upgradeNotNeeded', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_upgradeNotNeeded(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.upgradeNotNeeded signed method call
        """
        _r_ = self.C_.call_method_signed('upgradeNotNeeded', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def createAuction(self, name, duration, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.createAuction
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        if ts4_sign:
            return self.S_createAuction(name, duration, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_createAuction(name, duration, ts4_expect_ec=ts4_expect_ec)

    def G_createAuction(self, name, duration, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.createAuction getter
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter('createAuction', {'name': name, 'duration': duration}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_createAuction(self, name, duration, ts4_expect_ec=0):
        """
        Wrapper for D4User.createAuction raw getter
        :rtype: 
        :param name: bytes
        :param duration: uint8
        """
        return self.C_.call_getter_raw('createAuction', {'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)

    def M_createAuction(self, name, duration, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.createAuction method call
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method('createAuction', {'name': name, 'duration': duration}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_createAuction(self, name, duration, ts4_expect_ec=0):
        """
        Wrapper for D4User.createAuction signed method call
        :param name: bytes
        :param duration: uint8
        """
        _r_ = self.C_.call_method_signed('createAuction', {'name': name, 'duration': duration}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def createAuctionCallback(self, auction, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.createAuctionCallback
        :rtype: 
        :param auction: address
        """
        if ts4_sign:
            return self.S_createAuctionCallback(auction, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_createAuctionCallback(auction, ts4_expect_ec=ts4_expect_ec)

    def G_createAuctionCallback(self, auction, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.createAuctionCallback getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter('createAuctionCallback', {'auction': auction}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_createAuctionCallback(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4User.createAuctionCallback raw getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter_raw('createAuctionCallback', {'auction': auction}, expect_ec=ts4_expect_ec)

    def M_createAuctionCallback(self, auction, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.createAuctionCallback method call
        :param auction: address
        """
        _r_ = self.C_.call_method('createAuctionCallback', {'auction': auction}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_createAuctionCallback(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4User.createAuctionCallback signed method call
        :param auction: address
        """
        _r_ = self.C_.call_method_signed('createAuctionCallback', {'auction': auction}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def makeBid(self, auction, data, hash, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.makeBid
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        if ts4_sign:
            return self.S_makeBid(auction, data, hash, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_makeBid(auction, data, hash, ts4_expect_ec=ts4_expect_ec)

    def G_makeBid(self, auction, data, hash, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.makeBid getter
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        return self.C_.call_getter('makeBid', {'auction': auction, 'data': data, 'hash': hash}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_makeBid(self, auction, data, hash, ts4_expect_ec=0):
        """
        Wrapper for D4User.makeBid raw getter
        :rtype: 
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        return self.C_.call_getter_raw('makeBid', {'auction': auction, 'data': data, 'hash': hash}, expect_ec=ts4_expect_ec)

    def M_makeBid(self, auction, data, hash, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.makeBid method call
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        _r_ = self.C_.call_method('makeBid', {'auction': auction, 'data': data, 'hash': hash}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_makeBid(self, auction, data, hash, ts4_expect_ec=0):
        """
        Wrapper for D4User.makeBid signed method call
        :param auction: address
        :param data: bytes
        :param hash: uint256
        """
        _r_ = self.C_.call_method_signed('makeBid', {'auction': auction, 'data': data, 'hash': hash}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def revealBid(self, auction, amount, nonce, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.revealBid
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        if ts4_sign:
            return self.S_revealBid(auction, amount, nonce, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_revealBid(auction, amount, nonce, ts4_expect_ec=ts4_expect_ec)

    def G_revealBid(self, auction, amount, nonce, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.revealBid getter
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_revealBid(self, auction, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4User.revealBid raw getter
        :rtype: 
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter_raw('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)

    def M_revealBid(self, auction, amount, nonce, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.revealBid method call
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_revealBid(self, auction, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4User.revealBid signed method call
        :param auction: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method_signed('revealBid', {'auction': auction, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def bidRevealComplete(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.bidRevealComplete
        :rtype: 
        """
        if ts4_sign:
            return self.S_bidRevealComplete(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_bidRevealComplete(ts4_expect_ec=ts4_expect_ec)

    def G_bidRevealComplete(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.bidRevealComplete getter
        :rtype: 
        """
        return self.C_.call_getter('bidRevealComplete', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_bidRevealComplete(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.bidRevealComplete raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('bidRevealComplete', {}, expect_ec=ts4_expect_ec)

    def M_bidRevealComplete(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.bidRevealComplete method call
        """
        _r_ = self.C_.call_method('bidRevealComplete', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_bidRevealComplete(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.bidRevealComplete signed method call
        """
        _r_ = self.C_.call_method_signed('bidRevealComplete', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def finalize(self, auction, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.finalize
        :rtype: 
        :param auction: address
        """
        if ts4_sign:
            return self.S_finalize(auction, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_finalize(auction, ts4_expect_ec=ts4_expect_ec)

    def G_finalize(self, auction, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.finalize getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter('finalize', {'auction': auction}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_finalize(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4User.finalize raw getter
        :rtype: 
        :param auction: address
        """
        return self.C_.call_getter_raw('finalize', {'auction': auction}, expect_ec=ts4_expect_ec)

    def M_finalize(self, auction, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.finalize method call
        :param auction: address
        """
        _r_ = self.C_.call_method('finalize', {'auction': auction}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_finalize(self, auction, ts4_expect_ec=0):
        """
        Wrapper for D4User.finalize signed method call
        :param auction: address
        """
        _r_ = self.C_.call_method_signed('finalize', {'auction': auction}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def utilBidHash(self, auction, startTime, user, amount, nonce, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.utilBidHash
        :rtype: uint256
        :param auction: address
        :param startTime: uint32
        :param user: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.G_utilBidHash(auction, startTime, user, amount, nonce, ts4_expect_ec=ts4_expect_ec)

    def G_utilBidHash(self, auction, startTime, user, amount, nonce, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.utilBidHash getter
        :rtype: uint256
        :param auction: address
        :param startTime: uint32
        :param user: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter('utilBidHash', {'auction': auction, 'startTime': startTime, 'user': user, 'amount': amount, 'nonce': nonce}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_utilBidHash(self, auction, startTime, user, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4User.utilBidHash raw getter
        :rtype: uint256
        :param auction: address
        :param startTime: uint32
        :param user: address
        :param amount: uint128
        :param nonce: uint128
        """
        return self.C_.call_getter_raw('utilBidHash', {'auction': auction, 'startTime': startTime, 'user': user, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)

    def M_utilBidHash(self, auction, startTime, user, amount, nonce, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.utilBidHash method call
        :param auction: address
        :param startTime: uint32
        :param user: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method('utilBidHash', {'auction': auction, 'startTime': startTime, 'user': user, 'amount': amount, 'nonce': nonce}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_utilBidHash(self, auction, startTime, user, amount, nonce, ts4_expect_ec=0):
        """
        Wrapper for D4User.utilBidHash signed method call
        :param auction: address
        :param startTime: uint32
        :param user: address
        :param amount: uint128
        :param nonce: uint128
        """
        _r_ = self.C_.call_method_signed('utilBidHash', {'auction': auction, 'startTime': startTime, 'user': user, 'amount': amount, 'nonce': nonce}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryCert(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.queryCert
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_queryCert(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryCert(target, ts4_expect_ec=ts4_expect_ec)

    def G_queryCert(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.queryCert getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('queryCert', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryCert raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('queryCert', {'target': target}, expect_ec=ts4_expect_ec)

    def M_queryCert(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.queryCert method call
        :param target: address
        """
        _r_ = self.C_.call_method('queryCert', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryCert signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('queryCert', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryAuct(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.queryAuct
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_queryAuct(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryAuct(target, ts4_expect_ec=ts4_expect_ec)

    def G_queryAuct(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.queryAuct getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('queryAuct', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryAuct raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('queryAuct', {'target': target}, expect_ec=ts4_expect_ec)

    def M_queryAuct(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.queryAuct method call
        :param target: address
        """
        _r_ = self.C_.call_method('queryAuct', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryAuct signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('queryAuct', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def forgetCert(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.forgetCert
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_forgetCert(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_forgetCert(target, ts4_expect_ec=ts4_expect_ec)

    def G_forgetCert(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.forgetCert getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('forgetCert', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_forgetCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.forgetCert raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('forgetCert', {'target': target}, expect_ec=ts4_expect_ec)

    def M_forgetCert(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.forgetCert method call
        :param target: address
        """
        _r_ = self.C_.call_method('forgetCert', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_forgetCert(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.forgetCert signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('forgetCert', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def forgetAuct(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.forgetAuct
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_forgetAuct(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_forgetAuct(target, ts4_expect_ec=ts4_expect_ec)

    def G_forgetAuct(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.forgetAuct getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('forgetAuct', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_forgetAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.forgetAuct raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('forgetAuct', {'target': target}, expect_ec=ts4_expect_ec)

    def M_forgetAuct(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.forgetAuct method call
        :param target: address
        """
        _r_ = self.C_.call_method('forgetAuct', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_forgetAuct(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.forgetAuct signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('forgetAuct', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryCertCallback(self, info, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.queryCertCallback
        :rtype: 
        :param info: tuple
        """
        if ts4_sign:
            return self.S_queryCertCallback(info, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryCertCallback(info, ts4_expect_ec=ts4_expect_ec)

    def G_queryCertCallback(self, info, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.queryCertCallback getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter('queryCertCallback', {'info': info}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryCertCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryCertCallback raw getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter_raw('queryCertCallback', {'info': info}, expect_ec=ts4_expect_ec)

    def M_queryCertCallback(self, info, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.queryCertCallback method call
        :param info: tuple
        """
        _r_ = self.C_.call_method('queryCertCallback', {'info': info}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryCertCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryCertCallback signed method call
        :param info: tuple
        """
        _r_ = self.C_.call_method_signed('queryCertCallback', {'info': info}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def queryAuctCallback(self, info, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.queryAuctCallback
        :rtype: 
        :param info: tuple
        """
        if ts4_sign:
            return self.S_queryAuctCallback(info, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_queryAuctCallback(info, ts4_expect_ec=ts4_expect_ec)

    def G_queryAuctCallback(self, info, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.queryAuctCallback getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter('queryAuctCallback', {'info': info}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_queryAuctCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryAuctCallback raw getter
        :rtype: 
        :param info: tuple
        """
        return self.C_.call_getter_raw('queryAuctCallback', {'info': info}, expect_ec=ts4_expect_ec)

    def M_queryAuctCallback(self, info, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.queryAuctCallback method call
        :param info: tuple
        """
        _r_ = self.C_.call_method('queryAuctCallback', {'info': info}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_queryAuctCallback(self, info, ts4_expect_ec=0):
        """
        Wrapper for D4User.queryAuctCallback signed method call
        :param info: tuple
        """
        _r_ = self.C_.call_method_signed('queryAuctCallback', {'info': info}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def setValue(self, target, index, new_value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.setValue
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        if ts4_sign:
            return self.S_setValue(target, index, new_value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_setValue(target, index, new_value, ts4_expect_ec=ts4_expect_ec)

    def G_setValue(self, target, index, new_value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.setValue getter
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter('setValue', {'target': target, 'index': index, 'new_value': new_value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_setValue(self, target, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4User.setValue raw getter
        :rtype: 
        :param target: address
        :param index: int16
        :param new_value: address
        """
        return self.C_.call_getter_raw('setValue', {'target': target, 'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)

    def M_setValue(self, target, index, new_value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.setValue method call
        :param target: address
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method('setValue', {'target': target, 'index': index, 'new_value': new_value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_setValue(self, target, index, new_value, ts4_expect_ec=0):
        """
        Wrapper for D4User.setValue signed method call
        :param target: address
        :param index: int16
        :param new_value: address
        """
        _r_ = self.C_.call_method_signed('setValue', {'target': target, 'index': index, 'new_value': new_value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def resetValue(self, target, index, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.resetValue
        :rtype: 
        :param target: address
        :param index: int16
        """
        if ts4_sign:
            return self.S_resetValue(target, index, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_resetValue(target, index, ts4_expect_ec=ts4_expect_ec)

    def G_resetValue(self, target, index, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.resetValue getter
        :rtype: 
        :param target: address
        :param index: int16
        """
        return self.C_.call_getter('resetValue', {'target': target, 'index': index}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_resetValue(self, target, index, ts4_expect_ec=0):
        """
        Wrapper for D4User.resetValue raw getter
        :rtype: 
        :param target: address
        :param index: int16
        """
        return self.C_.call_getter_raw('resetValue', {'target': target, 'index': index}, expect_ec=ts4_expect_ec)

    def M_resetValue(self, target, index, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.resetValue method call
        :param target: address
        :param index: int16
        """
        _r_ = self.C_.call_method('resetValue', {'target': target, 'index': index}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_resetValue(self, target, index, ts4_expect_ec=0):
        """
        Wrapper for D4User.resetValue signed method call
        :param target: address
        :param index: int16
        """
        _r_ = self.C_.call_method_signed('resetValue', {'target': target, 'index': index}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def clearValues(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.clearValues
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_clearValues(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_clearValues(target, ts4_expect_ec=ts4_expect_ec)

    def G_clearValues(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.clearValues getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('clearValues', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_clearValues(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.clearValues raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('clearValues', {'target': target}, expect_ec=ts4_expect_ec)

    def M_clearValues(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.clearValues method call
        :param target: address
        """
        _r_ = self.C_.call_method('clearValues', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_clearValues(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.clearValues signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('clearValues', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certWithdrawExcess(self, target, amount, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certWithdrawExcess
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        if ts4_sign:
            return self.S_certWithdrawExcess(target, amount, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certWithdrawExcess(target, amount, ts4_expect_ec=ts4_expect_ec)

    def G_certWithdrawExcess(self, target, amount, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certWithdrawExcess getter
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        return self.C_.call_getter('certWithdrawExcess', {'target': target, 'amount': amount}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certWithdrawExcess(self, target, amount, ts4_expect_ec=0):
        """
        Wrapper for D4User.certWithdrawExcess raw getter
        :rtype: 
        :param target: address
        :param amount: uint128
        """
        return self.C_.call_getter_raw('certWithdrawExcess', {'target': target, 'amount': amount}, expect_ec=ts4_expect_ec)

    def M_certWithdrawExcess(self, target, amount, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certWithdrawExcess method call
        :param target: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method('certWithdrawExcess', {'target': target, 'amount': amount}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certWithdrawExcess(self, target, amount, ts4_expect_ec=0):
        """
        Wrapper for D4User.certWithdrawExcess signed method call
        :param target: address
        :param amount: uint128
        """
        _r_ = self.C_.call_method_signed('certWithdrawExcess', {'target': target, 'amount': amount}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certRequestUpgrade(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certRequestUpgrade
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certRequestUpgrade(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certRequestUpgrade(target, ts4_expect_ec=ts4_expect_ec)

    def G_certRequestUpgrade(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certRequestUpgrade getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certRequestUpgrade', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certRequestUpgrade(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certRequestUpgrade raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certRequestUpgrade', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certRequestUpgrade(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certRequestUpgrade method call
        :param target: address
        """
        _r_ = self.C_.call_method('certRequestUpgrade', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certRequestUpgrade(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certRequestUpgrade signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certRequestUpgrade', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def requestProlong(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.requestProlong
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_requestProlong(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_requestProlong(target, ts4_expect_ec=ts4_expect_ec)

    def G_requestProlong(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.requestProlong getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('requestProlong', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_requestProlong(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.requestProlong raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('requestProlong', {'target': target}, expect_ec=ts4_expect_ec)

    def M_requestProlong(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.requestProlong method call
        :param target: address
        """
        _r_ = self.C_.call_method('requestProlong', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_requestProlong(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.requestProlong signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('requestProlong', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def deploySub(self, target, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.deploySub
        :rtype: 
        :param target: address
        :param name: bytes
        """
        if ts4_sign:
            return self.S_deploySub(target, name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_deploySub(target, name, ts4_expect_ec=ts4_expect_ec)

    def G_deploySub(self, target, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.deploySub getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter('deploySub', {'target': target, 'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_deploySub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4User.deploySub raw getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter_raw('deploySub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)

    def M_deploySub(self, target, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.deploySub method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method('deploySub', {'target': target, 'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_deploySub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4User.deploySub signed method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('deploySub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def syncSub(self, target, name, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.syncSub
        :rtype: 
        :param target: address
        :param name: bytes
        """
        if ts4_sign:
            return self.S_syncSub(target, name, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_syncSub(target, name, ts4_expect_ec=ts4_expect_ec)

    def G_syncSub(self, target, name, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.syncSub getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter('syncSub', {'target': target, 'name': name}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_syncSub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4User.syncSub raw getter
        :rtype: 
        :param target: address
        :param name: bytes
        """
        return self.C_.call_getter_raw('syncSub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)

    def M_syncSub(self, target, name, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.syncSub method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method('syncSub', {'target': target, 'name': name}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_syncSub(self, target, name, ts4_expect_ec=0):
        """
        Wrapper for D4User.syncSub signed method call
        :param target: address
        :param name: bytes
        """
        _r_ = self.C_.call_method_signed('syncSub', {'target': target, 'name': name}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certTransferOwner
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        if ts4_sign:
            return self.S_certTransferOwner(target, new_owner, deadline, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certTransferOwner(target, new_owner, deadline, ts4_expect_ec=ts4_expect_ec)

    def G_certTransferOwner(self, target, new_owner, deadline, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certTransferOwner getter
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4User.certTransferOwner raw getter
        :rtype: 
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        return self.C_.call_getter_raw('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)

    def M_certTransferOwner(self, target, new_owner, deadline, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certTransferOwner method call
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certTransferOwner(self, target, new_owner, deadline, ts4_expect_ec=0):
        """
        Wrapper for D4User.certTransferOwner signed method call
        :param target: address
        :param new_owner: address
        :param deadline: uint32
        """
        _r_ = self.C_.call_method_signed('certTransferOwner', {'target': target, 'new_owner': new_owner, 'deadline': deadline}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certCancelTransferOwner(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certCancelTransferOwner
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certCancelTransferOwner(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certCancelTransferOwner(target, ts4_expect_ec=ts4_expect_ec)

    def G_certCancelTransferOwner(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certCancelTransferOwner getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certCancelTransferOwner', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certCancelTransferOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certCancelTransferOwner raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certCancelTransferOwner', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certCancelTransferOwner(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certCancelTransferOwner method call
        :param target: address
        """
        _r_ = self.C_.call_method('certCancelTransferOwner', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certCancelTransferOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certCancelTransferOwner signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certCancelTransferOwner', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certAcceptTransfer(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certAcceptTransfer
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certAcceptTransfer(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certAcceptTransfer(target, ts4_expect_ec=ts4_expect_ec)

    def G_certAcceptTransfer(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certAcceptTransfer getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certAcceptTransfer', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certAcceptTransfer(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certAcceptTransfer raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certAcceptTransfer', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certAcceptTransfer(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certAcceptTransfer method call
        :param target: address
        """
        _r_ = self.C_.call_method('certAcceptTransfer', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certAcceptTransfer(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certAcceptTransfer signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certAcceptTransfer', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certRelinquishOwner(self, target, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certRelinquishOwner
        :rtype: 
        :param target: address
        """
        if ts4_sign:
            return self.S_certRelinquishOwner(target, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_certRelinquishOwner(target, ts4_expect_ec=ts4_expect_ec)

    def G_certRelinquishOwner(self, target, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certRelinquishOwner getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter('certRelinquishOwner', {'target': target}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certRelinquishOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certRelinquishOwner raw getter
        :rtype: 
        :param target: address
        """
        return self.C_.call_getter_raw('certRelinquishOwner', {'target': target}, expect_ec=ts4_expect_ec)

    def M_certRelinquishOwner(self, target, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certRelinquishOwner method call
        :param target: address
        """
        _r_ = self.C_.call_method('certRelinquishOwner', {'target': target}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certRelinquishOwner(self, target, ts4_expect_ec=0):
        """
        Wrapper for D4User.certRelinquishOwner signed method call
        :param target: address
        """
        _r_ = self.C_.call_method_signed('certRelinquishOwner', {'target': target}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def addLocked(self, until, name, parent, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.addLocked
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        if ts4_sign:
            return self.S_addLocked(until, name, parent, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_addLocked(until, name, parent, ts4_expect_ec=ts4_expect_ec)

    def G_addLocked(self, until, name, parent, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.addLocked getter
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter('addLocked', {'until': until, 'name': name, 'parent': parent}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_addLocked(self, until, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4User.addLocked raw getter
        :rtype: 
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        return self.C_.call_getter_raw('addLocked', {'until': until, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)

    def M_addLocked(self, until, name, parent, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.addLocked method call
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method('addLocked', {'until': until, 'name': name, 'parent': parent}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_addLocked(self, until, name, parent, ts4_expect_ec=0):
        """
        Wrapper for D4User.addLocked signed method call
        :param until: uint32
        :param name: bytes
        :param parent: address
        """
        _r_ = self.C_.call_method_signed('addLocked', {'until': until, 'name': name, 'parent': parent}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdrawable(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.withdrawable
        :rtype: uint128
        """
        return self.G_withdrawable(ts4_expect_ec=ts4_expect_ec)

    def G_withdrawable(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.withdrawable getter
        :rtype: uint128
        """
        return self.C_.call_getter('withdrawable', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.withdrawable raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('withdrawable', {}, expect_ec=ts4_expect_ec)

    def M_withdrawable(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.withdrawable method call
        """
        _r_ = self.C_.call_method('withdrawable', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdrawable(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.withdrawable signed method call
        """
        _r_ = self.C_.call_method_signed('withdrawable', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def sweepLocks(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.sweepLocks
        :rtype: 
        """
        if ts4_sign:
            return self.S_sweepLocks(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_sweepLocks(ts4_expect_ec=ts4_expect_ec)

    def G_sweepLocks(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.sweepLocks getter
        :rtype: 
        """
        return self.C_.call_getter('sweepLocks', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_sweepLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.sweepLocks raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('sweepLocks', {}, expect_ec=ts4_expect_ec)

    def M_sweepLocks(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.sweepLocks method call
        """
        _r_ = self.C_.call_method('sweepLocks', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_sweepLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.sweepLocks signed method call
        """
        _r_ = self.C_.call_method_signed('sweepLocks', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def withdraw(self, dest, value, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.withdraw
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        if ts4_sign:
            return self.S_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_withdraw(dest, value, ts4_expect_ec=ts4_expect_ec)

    def G_withdraw(self, dest, value, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.withdraw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter('withdraw', {'dest': dest, 'value': value}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4User.withdraw raw getter
        :rtype: 
        :param dest: address
        :param value: uint128
        """
        return self.C_.call_getter_raw('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)

    def M_withdraw(self, dest, value, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.withdraw method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method('withdraw', {'dest': dest, 'value': value}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_withdraw(self, dest, value, ts4_expect_ec=0):
        """
        Wrapper for D4User.withdraw signed method call
        :param dest: address
        :param value: uint128
        """
        _r_ = self.C_.call_method_signed('withdraw', {'dest': dest, 'value': value}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def passToOwner(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.passToOwner
        :rtype: 
        """
        if ts4_sign:
            return self.S_passToOwner(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_passToOwner(ts4_expect_ec=ts4_expect_ec)

    def G_passToOwner(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.passToOwner getter
        :rtype: 
        """
        return self.C_.call_getter('passToOwner', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.passToOwner raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('passToOwner', {}, expect_ec=ts4_expect_ec)

    def M_passToOwner(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.passToOwner method call
        """
        _r_ = self.C_.call_method('passToOwner', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_passToOwner(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.passToOwner signed method call
        """
        _r_ = self.C_.call_method_signed('passToOwner', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def sink(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.sink
        :rtype: 
        """
        if ts4_sign:
            return self.S_sink(ts4_expect_ec=ts4_expect_ec)
        else:
            return self.M_sink(ts4_expect_ec=ts4_expect_ec)

    def G_sink(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.sink getter
        :rtype: 
        """
        return self.C_.call_getter('sink', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.sink raw getter
        :rtype: 
        """
        return self.C_.call_getter_raw('sink', {}, expect_ec=ts4_expect_ec)

    def M_sink(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.sink method call
        """
        _r_ = self.C_.call_method('sink', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_sink(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.sink signed method call
        """
        _r_ = self.C_.call_method_signed('sink', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_root(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.st_root
        :rtype: address
        """
        return self.G_st_root(ts4_expect_ec=ts4_expect_ec)

    def G_st_root(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.st_root getter
        :rtype: address
        """
        return self.C_.call_getter('st_root', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_root raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_root', {}, expect_ec=ts4_expect_ec)

    def M_st_root(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.st_root method call
        """
        _r_ = self.C_.call_method('st_root', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_root(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_root signed method call
        """
        _r_ = self.C_.call_method_signed('st_root', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_type(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.st_type
        :rtype: uint8
        """
        return self.G_st_type(ts4_expect_ec=ts4_expect_ec)

    def G_st_type(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.st_type getter
        :rtype: uint8
        """
        return self.C_.call_getter('st_type', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_type raw getter
        :rtype: uint8
        """
        return self.C_.call_getter_raw('st_type', {}, expect_ec=ts4_expect_ec)

    def M_st_type(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.st_type method call
        """
        _r_ = self.C_.call_method('st_type', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_type(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_type signed method call
        """
        _r_ = self.C_.call_method_signed('st_type', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_name(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.st_name
        :rtype: bytes
        """
        return self.G_st_name(ts4_expect_ec=ts4_expect_ec)

    def G_st_name(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.st_name getter
        :rtype: bytes
        """
        return self.C_.call_getter('st_name', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_name raw getter
        :rtype: bytes
        """
        return self.C_.call_getter_raw('st_name', {}, expect_ec=ts4_expect_ec)

    def M_st_name(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.st_name method call
        """
        _r_ = self.C_.call_method('st_name', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_name(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_name signed method call
        """
        _r_ = self.C_.call_method_signed('st_name', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def st_parent(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.st_parent
        :rtype: address
        """
        return self.G_st_parent(ts4_expect_ec=ts4_expect_ec)

    def G_st_parent(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.st_parent getter
        :rtype: address
        """
        return self.C_.call_getter('st_parent', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_parent raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('st_parent', {}, expect_ec=ts4_expect_ec)

    def M_st_parent(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.st_parent method call
        """
        _r_ = self.C_.call_method('st_parent', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_st_parent(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.st_parent signed method call
        """
        _r_ = self.C_.call_method_signed('st_parent', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def base_code(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.base_code
        :rtype: cell
        """
        return self.G_base_code(ts4_expect_ec=ts4_expect_ec)

    def G_base_code(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.base_code getter
        :rtype: cell
        """
        return self.C_.call_getter('base_code', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.base_code raw getter
        :rtype: cell
        """
        return self.C_.call_getter_raw('base_code', {}, expect_ec=ts4_expect_ec)

    def M_base_code(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.base_code method call
        """
        _r_ = self.C_.call_method('base_code', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_base_code(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.base_code signed method call
        """
        _r_ = self.C_.call_method_signed('base_code', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_version(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.m_version
        :rtype: uint16
        """
        return self.G_m_version(ts4_expect_ec=ts4_expect_ec)

    def G_m_version(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.m_version getter
        :rtype: uint16
        """
        return self.C_.call_getter('m_version', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.m_version raw getter
        :rtype: uint16
        """
        return self.C_.call_getter_raw('m_version', {}, expect_ec=ts4_expect_ec)

    def M_m_version(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.m_version method call
        """
        _r_ = self.C_.call_method('m_version', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_version(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.m_version signed method call
        """
        _r_ = self.C_.call_method_signed('m_version', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def m_revision(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.m_revision
        :rtype: uint32
        """
        return self.G_m_revision(ts4_expect_ec=ts4_expect_ec)

    def G_m_revision(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.m_revision getter
        :rtype: uint32
        """
        return self.C_.call_getter('m_revision', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.m_revision raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('m_revision', {}, expect_ec=ts4_expect_ec)

    def M_m_revision(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.m_revision method call
        """
        _r_ = self.C_.call_method('m_revision', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_m_revision(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.m_revision signed method call
        """
        _r_ = self.C_.call_method_signed('m_revision', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def fundLocks(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.fundLocks
        :rtype: map(uint32,uint128)
        """
        return self.G_fundLocks(ts4_expect_ec=ts4_expect_ec)

    def G_fundLocks(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.fundLocks getter
        :rtype: map(uint32,uint128)
        """
        return self.C_.call_getter('fundLocks', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_fundLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.fundLocks raw getter
        :rtype: map(uint32,uint128)
        """
        return self.C_.call_getter_raw('fundLocks', {}, expect_ec=ts4_expect_ec)

    def M_fundLocks(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.fundLocks method call
        """
        _r_ = self.C_.call_method('fundLocks', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_fundLocks(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.fundLocks signed method call
        """
        _r_ = self.C_.call_method_signed('fundLocks', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def minLockTime(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.minLockTime
        :rtype: uint32
        """
        return self.G_minLockTime(ts4_expect_ec=ts4_expect_ec)

    def G_minLockTime(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.minLockTime getter
        :rtype: uint32
        """
        return self.C_.call_getter('minLockTime', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_minLockTime(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.minLockTime raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('minLockTime', {}, expect_ec=ts4_expect_ec)

    def M_minLockTime(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.minLockTime method call
        """
        _r_ = self.C_.call_method('minLockTime', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_minLockTime(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.minLockTime signed method call
        """
        _r_ = self.C_.call_method_signed('minLockTime', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def totalLocked(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.totalLocked
        :rtype: uint128
        """
        return self.G_totalLocked(ts4_expect_ec=ts4_expect_ec)

    def G_totalLocked(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.totalLocked getter
        :rtype: uint128
        """
        return self.C_.call_getter('totalLocked', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_totalLocked(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.totalLocked raw getter
        :rtype: uint128
        """
        return self.C_.call_getter_raw('totalLocked', {}, expect_ec=ts4_expect_ec)

    def M_totalLocked(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.totalLocked method call
        """
        _r_ = self.C_.call_method('totalLocked', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_totalLocked(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.totalLocked signed method call
        """
        _r_ = self.C_.call_method_signed('totalLocked', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def masterKey(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.masterKey
        :rtype: bytes
        """
        return self.G_masterKey(ts4_expect_ec=ts4_expect_ec)

    def G_masterKey(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.masterKey getter
        :rtype: bytes
        """
        return self.C_.call_getter('masterKey', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_masterKey(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.masterKey raw getter
        :rtype: bytes
        """
        return self.C_.call_getter_raw('masterKey', {}, expect_ec=ts4_expect_ec)

    def M_masterKey(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.masterKey method call
        """
        _r_ = self.C_.call_method('masterKey', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_masterKey(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.masterKey signed method call
        """
        _r_ = self.C_.call_method_signed('masterKey', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auctBook(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.auctBook
        :rtype: map(uint32,address)
        """
        return self.G_auctBook(ts4_expect_ec=ts4_expect_ec)

    def G_auctBook(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.auctBook getter
        :rtype: map(uint32,address)
        """
        return self.C_.call_getter('auctBook', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auctBook(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBook raw getter
        :rtype: map(uint32,address)
        """
        return self.C_.call_getter_raw('auctBook', {}, expect_ec=ts4_expect_ec)

    def M_auctBook(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.auctBook method call
        """
        _r_ = self.C_.call_method('auctBook', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auctBook(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBook signed method call
        """
        _r_ = self.C_.call_method_signed('auctBook', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auctInfo(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.auctInfo
        :rtype: map(address,tuple)
        """
        return self.G_auctInfo(ts4_expect_ec=ts4_expect_ec)

    def G_auctInfo(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.auctInfo getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter('auctInfo', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auctInfo(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctInfo raw getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter_raw('auctInfo', {}, expect_ec=ts4_expect_ec)

    def M_auctInfo(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.auctInfo method call
        """
        _r_ = self.C_.call_method('auctInfo', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auctInfo(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctInfo signed method call
        """
        _r_ = self.C_.call_method_signed('auctInfo', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auctBids(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.auctBids
        :rtype: map(address,tuple)
        """
        return self.G_auctBids(ts4_expect_ec=ts4_expect_ec)

    def G_auctBids(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.auctBids getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter('auctBids', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auctBids(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBids raw getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter_raw('auctBids', {}, expect_ec=ts4_expect_ec)

    def M_auctBids(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.auctBids method call
        """
        _r_ = self.C_.call_method('auctBids', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auctBids(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBids signed method call
        """
        _r_ = self.C_.call_method_signed('auctBids', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certBook(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certBook
        :rtype: map(uint32,address)
        """
        return self.G_certBook(ts4_expect_ec=ts4_expect_ec)

    def G_certBook(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certBook getter
        :rtype: map(uint32,address)
        """
        return self.C_.call_getter('certBook', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certBook(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certBook raw getter
        :rtype: map(uint32,address)
        """
        return self.C_.call_getter_raw('certBook', {}, expect_ec=ts4_expect_ec)

    def M_certBook(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certBook method call
        """
        _r_ = self.C_.call_method('certBook', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certBook(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certBook signed method call
        """
        _r_ = self.C_.call_method_signed('certBook', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certInfo(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certInfo
        :rtype: map(address,tuple)
        """
        return self.G_certInfo(ts4_expect_ec=ts4_expect_ec)

    def G_certInfo(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certInfo getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter('certInfo', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certInfo(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certInfo raw getter
        :rtype: map(address,tuple)
        """
        return self.C_.call_getter_raw('certInfo', {}, expect_ec=ts4_expect_ec)

    def M_certInfo(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certInfo method call
        """
        _r_ = self.C_.call_method('certInfo', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certInfo(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certInfo signed method call
        """
        _r_ = self.C_.call_method_signed('certInfo', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def auctBookNext(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.auctBookNext
        :rtype: uint32
        """
        return self.G_auctBookNext(ts4_expect_ec=ts4_expect_ec)

    def G_auctBookNext(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.auctBookNext getter
        :rtype: uint32
        """
        return self.C_.call_getter('auctBookNext', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_auctBookNext(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBookNext raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('auctBookNext', {}, expect_ec=ts4_expect_ec)

    def M_auctBookNext(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.auctBookNext method call
        """
        _r_ = self.C_.call_method('auctBookNext', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_auctBookNext(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.auctBookNext signed method call
        """
        _r_ = self.C_.call_method_signed('auctBookNext', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def certBookNext(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.certBookNext
        :rtype: uint32
        """
        return self.G_certBookNext(ts4_expect_ec=ts4_expect_ec)

    def G_certBookNext(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.certBookNext getter
        :rtype: uint32
        """
        return self.C_.call_getter('certBookNext', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_certBookNext(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certBookNext raw getter
        :rtype: uint32
        """
        return self.C_.call_getter_raw('certBookNext', {}, expect_ec=ts4_expect_ec)

    def M_certBookNext(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.certBookNext method call
        """
        _r_ = self.C_.call_method('certBookNext', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_certBookNext(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.certBookNext signed method call
        """
        _r_ = self.C_.call_method_signed('certBookNext', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def lastCreatedAuction(self, ts4_expect_ec=0, ts4_sign=False):
        """
        Wrapper for D4User.lastCreatedAuction
        :rtype: address
        """
        return self.G_lastCreatedAuction(ts4_expect_ec=ts4_expect_ec)

    def G_lastCreatedAuction(self, ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decoder=None):
        """
        Wrapper for D4User.lastCreatedAuction getter
        :rtype: address
        """
        return self.C_.call_getter('lastCreatedAuction', {}, key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decoder=ts4_decoder)

    def R_lastCreatedAuction(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.lastCreatedAuction raw getter
        :rtype: address
        """
        return self.C_.call_getter_raw('lastCreatedAuction', {}, expect_ec=ts4_expect_ec)

    def M_lastCreatedAuction(self, ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False):
        """
        Wrapper for D4User.lastCreatedAuction method call
        """
        _r_ = self.C_.call_method('lastCreatedAuction', {}, private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

    def S_lastCreatedAuction(self, ts4_expect_ec=0):
        """
        Wrapper for D4User.lastCreatedAuction signed method call
        """
        _r_ = self.C_.call_method_signed('lastCreatedAuction', {}, expect_ec=ts4_expect_ec)
        if WrapperGlobal.auto_dispatch_messages:
            ts4.dispatch_messages()
        return _r_

