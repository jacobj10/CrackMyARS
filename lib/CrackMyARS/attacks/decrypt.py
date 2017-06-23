from Crypto.PublicKey import RSA

from CrackMyARS.attacks.attack import Attack

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
        try:
            out = bytes.fromhex(hex(out)[2:]).decode('utf-8')
        except ValueError:
            pass
    else:
        if 0 in out:
            padding_end = out.index(0)
            out = out[padding_end + 1:].decode('utf-8')
    return out

class DecryptAttack(Attack):
    def __init__(self):
        self.params = decrypt_attack_params
        self.func = decrypt
        self.out = "M"
        self.name = "Basic Decrypt"
