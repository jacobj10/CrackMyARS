import gmpy

from factordb.factordb import FactorDB

def basic_factor(n, e):
    f_list = FactorDB(n).get_factor_list()
    if len(f_list) == 2:
        phi = (f_list[0] - 1) * (f_list[1] - 1)
        d = gmpy.invert(e, phi)
        return d
    return -1
