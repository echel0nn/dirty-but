"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This is a example for decrypt RSA simple.

================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import gmpy

p = 0 # 1
q = 0 # 2
e = 65537 # exp
c = 0 # cipher text

f = (p-1) * (q-1)

d = gmpy.invert(e,f)

print "private key d value is : %d" % d
plain = hex(pow(c,d,n))[2:]
plain_text = plain.decode("hex")
print "The Plain text is %s "  % flag
