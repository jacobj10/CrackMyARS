
def decrypt(c, d, n):
    out_int = pow(c, d, n)
    out_hex = hex(out_int)[2:]
    asc = bytes.fromhex(out_hex).decode('utf-8')
    return asc
