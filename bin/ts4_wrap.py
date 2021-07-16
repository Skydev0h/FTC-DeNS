import os, sys, json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + "/../")

pars_getter = 'key=ts4_key, expect_ec=ts4_expect_ec, decode=ts4_decode, decode_ints=ts4_decode_ints, decode_tuples=ts4_decode_tuples, dont_decode_fields=ts4_dont_decode_fields'
pars_getter_raw = 'expect_ec=ts4_expect_ec'
pars_method = 'private_key=ts4_private_key, expect_ec=ts4_expect_ec, is_debot=ts4_is_debot'
pars_method_signed = 'expect_ec=ts4_expect_ec'
pars_smart = 'ts4_expect_ec=ts4_expect_ec'

tails_getter = 'ts4_key=None, ts4_expect_ec=0, ts4_decode=False, ts4_decode_ints=True, ts4_decode_tuples=None, ts4_dont_decode_fields=[]'
tails_getter_raw = 'ts4_expect_ec=0'
tails_method = 'ts4_private_key=None, ts4_expect_ec=0, ts4_is_debot=False'
tails_method_signed = 'ts4_expect_ec=0'
tails_smart = 'ts4_expect_ec=0, ts4_sign=False'

print('import tonos_ts4.ts4 as ts4')
print('')
print('class WrapperGlobal:')
print('    auto_dispatch_messages: bool = True')
print('')

classes=[]
for fname in os.listdir("out"):
    if not fname.startswith("D4"): continue
    if not fname.endswith(".abi.json"): continue
    cname = fname[:-9]
    classes.append(cname)
    with open("./out/" + fname, 'r') as f1:
        abi = json.load(f1)
        fun = abi['functions']
    c_name = 'C_'
    print('# noinspection PyDefaultArgument,PyPep8Naming,PyShadowingBuiltins')
    print('class Wrap' + cname + ':')
    print('    def __init__(self, contract):')
    print('        self.' + c_name + ' = contract')
    print('        self.A_ = contract.address')
    print('')
    for fn in fun:
        inputs = []
        iregals = []
        otypes = []
        aid = False
        for inp in fn['inputs']:
            if inp['name'] == '_answer_id':
                aid = True
            else:
                inputs.append(inp['name'])
            iregals.append('\'' + inp['name'] + '\': ' + inp['name'])
        if aid:
            inputs.append('_answer_id=0')
        for oup in fn['outputs']:
            otypes.append(oup['type'])

        print('    def ' + fn['name'] + '(self, ' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + tails_smart + '):')
        print('        """')
        print('        Wrapper for ' + cname + '.' + fn['name'])
        print('        :rtype: ' + ', '.join(otypes))
        for inp in fn['inputs']:
            print('        :param ' + inp['name'] + ': ' + inp['type'])
        print('        """')
        if len(otypes) == 0:
            print('        if ts4_sign:')
            print('            return self.S_' + fn['name'] + '(' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + pars_smart + ')')
            print('        else:')
            print('            return self.M_' + fn['name'] + '(' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + pars_smart + ')')
        else:
            print('        return self.G_' + fn['name'] + '(' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + pars_smart + ')')
        print('')

        print('    def G_' + fn['name'] + '(self, ' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + tails_getter + '):')
        print('        """')
        print('        Wrapper for ' + cname + '.' + fn['name'] + ' getter')
        print('        :rtype: ' + ', '.join(otypes))
        for inp in fn['inputs']:
            print('        :param ' + inp['name'] + ': ' + inp['type'])
        print('        """')
        print('        return self.' + c_name + '.call_getter(\'' + fn['name'] + '\', {' + ', '.join(iregals) + '}, ' + pars_getter + ')')
        print('')

        print('    def R_' + fn['name'] + '(self, ' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + tails_getter_raw + '):')
        print('        """')
        print('        Wrapper for ' + cname + '.' + fn['name'] + ' raw getter')
        print('        :rtype: ' + ', '.join(otypes))
        for inp in fn['inputs']:
            print('        :param ' + inp['name'] + ': ' + inp['type'])
        print('        """')
        print('        return self.' + c_name + '.call_getter_raw(\'' + fn['name'] + '\', {' + ', '.join(iregals) + '}, ' + pars_getter_raw + ')')
        print('')

        print('    def M_' + fn['name'] + '(self, ' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + tails_method + '):')
        print('        """')
        print('        Wrapper for ' + cname + '.' + fn['name'] + ' method call')
        for inp in fn['inputs']:
            print('        :param ' + inp['name'] + ': ' + inp['type'])
        print('        """')
        print('        _r_ = self.' + c_name + '.call_method(\'' + fn['name'] + '\', {' + ', '.join(iregals) + '}, ' + pars_method + ')')
        print('        if WrapperGlobal.auto_dispatch_messages:')
        print('            ts4.dispatch_messages()')
        print('        return _r_')
        print('')

        print('    def S_' + fn['name'] + '(self, ' + ', '.join(inputs) + (', ' if len(inputs) > 0 else '') + tails_method_signed + '):')
        print('        """')
        print('        Wrapper for ' + cname + '.' + fn['name'] + ' signed method call')
        for inp in fn['inputs']:
            print('        :param ' + inp['name'] + ': ' + inp['type'])
        print('        """')
        print('        _r_ = self.' + c_name + '.call_method_signed(\'' + fn['name'] + '\', {' + ', '.join(iregals) + '}, ' + pars_method_signed + ')')
        print('        if WrapperGlobal.auto_dispatch_messages:')
        print('            ts4.dispatch_messages()')
        print('        return _r_')
        print('')

# print('def Wrap(contract: ts4.BaseContract):')
# print('    c = contract.name_')
# for cn in classes:
#     print('    if c == \'' + cn + '\':')
#     print('        return Wrap' + cn + '(contract)')
# print('    return None')
