from CrackMyARS.attacks.crt import CRTAttack
from CrackMyARS.attacks.wiener_attack import WienerAttack
from CrackMyARS.attacks.basic_factor import BasicFactorAttack
from CrackMyARS.attacks.decrypt import DecryptAttack

from Crypto.PublicKey import RSA

import logging

logger = logging.getLogger('results')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

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

        self.logger = logger
        self.logger.info('Creating Key')

    def decide(self):
        args = {}
        for var in self.__dict__.keys():
            if self.__dict__[var]:
                args[var] = self.__dict__[var]
        for attack in ATTACKS:
            temp_attack = attack()
            self.logger.info('Trying ' + temp_attack.name)
            if temp_attack.should_work(args):
                self.logger.info('  Parameters of attack match')
                input_args = {}
                for param in temp_attack.params:
                    input_args[param] = args[param]
                out = temp_attack.func(input_args)
                if out != -1:
                    self.logger.info('      Attack was a success! Displaying output')
                    return self.display(out, temp_attack)
                else:
                    self.logger.info('      Attack failed')
            else:
                self.logger.info('  Parameters of attack do not match')

    def display(self, out, attack):
        if attack.out == "D":
            out = int(out)
            if self.c and self.n:
                return (DecryptAttack().func({'c':self.c, 'd':out, 'n':self.n, 'e':self.e}))
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
        self.c = open(f, 'rb').read().rstrip(bytes('\n', 'utf-8'))

    def add_multiple_c_from_file(self, files):
        self.c = []
        for f in files:
            data = open(f, 'rb').read().rstrip(bytes('\n', 'utf-8'))
            data = int(data.hex(), 16)
            self.c.append(data)

    def add_multiple_n_from_file(self, files):
        self.n = []
        for f in files:
            key = open(f).read()
            key = RSA.importKey(key)
            self.e = key.e
            self.n.append(key.n)

