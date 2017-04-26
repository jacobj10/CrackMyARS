import gmpy

from factordb.factordb import FactorDB
from attacks.attack import Attack

basic_factor_attack_params = {'e': 0, 'n': 0}
def basic_factor(basic_factor_attack_params):
    e = basic_factor_attack_params['e']
    n = basic_factor_attack_params['n']
    f_list = FactorDB(n).get_factor_list()
    if len(f_list) == 2:
        phi = (f_list[0] - 1) * (f_list[1] - 1)
        d = gmpy.invert(e, phi)
        return d
    return -1


class BasicFactorAttack(Attack):
    def __init__(self):
        self.params = basic_factor_attack_params
        self.func = basic_factor
        self.out = "D"
