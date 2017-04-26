from attacks.crt import CRTAttack
from attacks.wiener_attack import WienerAttack
from attacks.basic_factor import BasicFactorAttack
from attacks.attack import Attack

decrypt_attack_params = {'c':0, 'd':0, 'n':0}
def decrypt(c, d, n):
    out_int = pow(c, d, n)
    out_hex = hex(out_int)[2:]
    asc = bytes.fromhex(out_hex).decode('utf-8')
    return asc

class DecryptAttack(Attack):
    def __init__(self):
        self.params = decrypt_attack_params
        self.func = decrypt

ATTACKS = [BasicFactorAttack, WienerAttack, CRTAttack, DecryptAttack]

class InvalidKeyError(Exception):
    pass

class Key(object):
    def __init__(self, p=None, q=None, d=None, n=None, c=None, e=None):
        self.p = p
        self.q = q
        self.d = d
        self.n = n
        self.c = c
        self.e = e

    def decide(self):
        args = {}
        for var in self.__dict__.keys():
            if self.__dict__[var]:
                args[var] = self.__dict__[var]
        for attack in ATTACKS:
            temp_attack = attack()
            print(temp_attack.should_work(args))

Key(c=5, e=5, n=5).decide()
