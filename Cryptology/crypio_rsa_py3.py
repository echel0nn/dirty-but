"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This is a example for decrypt RSA with SQRT.

This is not a good approach new RSA.

================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import gmpy2
from Crypto.PublicKey import RSA
import binascii

#cipher text is not crypted at all....
# c = m^e (mod n) = m
# if e = 1 then c = m
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
e = 1

def sqrt(x):
    low = -1
    high = c+1
    while low + 1 < high:
        m = (low + high) // 2
        y = m*m
        if y < x:
            low = m
        else:
            high = m
    m = high
    return m


r = sqrt(n)
print(r)
p = r + 3
q = r - 3
#assert n == p * q
d = lambda p, q, e: int(gmpy2.invert(e, (p-1)*(q-1)))

key = RSA.construct((n, e, d(p,q,e)))

print(binascii.unhexlify(hex(key.decrypt(c))[2:]).decode())
