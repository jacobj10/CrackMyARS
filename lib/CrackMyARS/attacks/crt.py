import gmpy

from CrackMyARS.attacks.attack import Attack

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def prod_minus_index(arr, i):
    """
    Product of a list excluding the index i
    """
    total = 1
    counter = 0
    while counter < len(arr):
        if counter != i:
            total *= arr[counter]
        counter += 1
    return total

crt_attack_params = {'e': 0, 'c': [], 'n': []}
def crt(crt_attack_params):
    e = crt_attack_params['e']
    c = crt_attack_params['c']
    n = crt_attack_params['n']
    if not isinstance(c, list) or not isinstance(n, list):
        return -1
    if len(c) != e or len(n) != e:
        return -1
    m = 0
    for k in range(e):
        prod = prod_minus_index(n, k)
        m += c[k] * prod * gmpy.invert(prod, n[k])
    i = gmpy.mpz(m % (prod_minus_index(n, len(n))))
    hd = hex(i.root(e)[0])[2:]
    asc = bytes.fromhex(hd).decode('utf-8')
    return asc

class CRTAttack(Attack):
    def __init__(self):
        self.params = crt_attack_params
        self.func = crt
        self.out = 'M'
        self.name = "Chinese Remainder Theorem"
