from attacks.crt import CRTAttack
from attacks.wiener_attack import WienerAttack
from attacks.basic_factor import BasicFactorAttack
from attacks.attack import Attack

from Crypto.PublicKey import RSA

import argparse
import binascii
decrypt_attack_params = {'c':0, 'd':0, 'n':0, 'e':0}
def decrypt(decrypt_attack_params):
    c = decrypt_attack_params['c']
    d = decrypt_attack_params['d']
    d = int(d)
    n = decrypt_attack_params['n']
    e = decrypt_attack_params['e']
    key = RSA.construct((n, e, d))
    out = key.decrypt(c)
    if type(out) == int:
        out = bytes.fromhex(hex(out)[2:]).decode('utf-8')
    return out

class DecryptAttack(Attack):
    def __init__(self):
        self.params = decrypt_attack_params
        self.func = decrypt
        self.out = "M"

ATTACKS = [BasicFactorAttack, WienerAttack, CRTAttack, DecryptAttack]

class InvalidKeyError(Exception):
    pass

class Key(object):
    def __init__(self, p=None, q=None, d=None, n=None, c=None, e=None, m=None):
        self.p = p
        self.q = q
        self.d = d
        self.n = n
        self.c = c
        self.e = e
        self.m = m

    def decide(self):
        args = {}
        for var in self.__dict__.keys():
            if self.__dict__[var]:
                args[var] = self.__dict__[var]
        for attack in ATTACKS:
            temp_attack = attack()
            if temp_attack.should_work(args):
                input_args = {}
                for param in temp_attack.params:
                    input_args[param] = args[param]
                out = temp_attack.func(input_args)
                if out != -1:
                    return self.display(out, temp_attack)

    def display(self, out, attack):
        if attack.out == "D":
            out = int(out)
            if self.c and self.n:
                return (decrypt({'c':self.c, 'd':out, 'n':self.n, 'e':self.e}))
            else:
                return ("Private Key: " + str(out))
        elif attack.out == "M":
            return (out)

    def add_pem(self, pem):
        key = open(pem).read()
        key = RSA.importKey(key)
        if key.can_encrypt():
            self.e = key.e
            self.n = key.n
        if key.has_private():
            self.d = d

    def c_from_file(self, f):
        self.c = open(f, 'rb').read().strip()
"""
if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--pem", action="store")
    params = parse.add_argument_group("Decimal Params")
    params.add_argument("-p", action="store")
    params.add_argument("-q", action="store")
    params.add_argument("-d", action="store")
    params.add_argument("-n", action="store")
    params.add_argument("-e", action="store")
    params.add_argument("-c", action="store")
    parse.add_argument("--to-dec", action="store")
    x = vars(parse.parse_args())
    if x['pem']:
        print("pem")
    print(x)
"""
