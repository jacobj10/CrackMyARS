class KeyTooLargeException(Exception):
    pass


def isqrt(x):
    """
    Newton's method for finding integer square roots
    
    :param x: The number to take the square root of
    :return: The integer square root approximation (or exact value if n is a perfect square)
    """
    x = x
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + x // x) // 2
    return x


def continued_frac_gen(x, y):
    """
    Generate the canonical continued fraction representation of a rational number x/y
    
    :param x: The rational number's numerator
    :param y: The rational number's denominator
    :return: The next in the sequence of continued fraction coefficients
    """
    a = x // y
    yield a
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        yield a


def convergent_gen(x, y):
    """
    Generator for convergents of a rational number x/y. In the case of Wiener's Attack, the convergents are values of
    k/d, where k is defined here: https://en.wikipedia.org/wiki/Wiener%27s_attack
    
    :param x: The rational number's numerator
    :param y: The rational number's denominator
    :return: The next in the sequence of tuples representing of the form (numerator,denominator) converging on x/y
    """
    cont_frac = continued_frac_gen(x, y)
    a_0, a = next(cont_frac), next(cont_frac)
    num_last,denom_last, num, denom = a_0, 1, a_0*a + 1, a
    yield num_last, denom_last
    yield num, denom
    while num < x:
        a = next(cont_frac)
        num_next, denom_next = num * a + num_last, denom * a + denom_last
        yield num_next, denom_next
        num_last, denom_last, num, denom = num, denom, num_next, denom_next


def wiener(e, n):
    """
    Wiener's attack on RSA encryption. Works given d < (n^(1/4))/3.
    
    :param e: The public key
    :param n: The modulus
    :return: A tuple representing of the form (private key d, p, q) where p and q are the prime factorization of n
    """
    g = convergent_gen(e, n)
    k, d = next(g)
    cap = isqrt(isqrt(n)) // 3
    while d <= cap:
        if k != 0:
            phi = (e * d - 1) // k
            a, b, c = 1, -(n - phi + 1), n
            discrm = b ** 2 - 4 * a * c
            discrm_sqrt = isqrt(discrm)
            if discrm_sqrt**2 != discrm:
                k, d = next(g)
                continue
            p, q = (-b + discrm_sqrt) // (2 * a), (-b - discrm_sqrt) // (2 * a)
            return int(d), int(p), int(q)
        k, d = next(g)
    raise KeyTooLargeException("The value of the public key d is larger than (n^(1/4))/3, thus Wiener's Attack will "
                               "not work.")
