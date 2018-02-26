import gmpy
import time

from CrackMyARS.attacks.attack import Attack

brute_force_attack_params = {'e': 0, 'n': 0, 'c': 0}
def brute_force(brute_force_attack_params):
    e = brute_force_attack_params['e']
    n = brute_force_attack_params['n']
    c = brute_force_attack_params['c']

    start_time = time.time()
    current_time = time.time()
    while current_time - start_time < 30:
        current_time = time.time()
        m = gmpy.root(c, e)[0]
        if pow(m, e, n) == c:
            hd = hex(int(m))[2:]
            asc = bytes.fromhex(hd).decode('utf-8')
            return asc
        c += n
    return -1


class BruteForceAttack(Attack):
    def __init__(self):
        self.params = brute_force_attack_params
        self.func = brute_force
        self.out = "M"
        self.name = "Brute Force Attack" 
