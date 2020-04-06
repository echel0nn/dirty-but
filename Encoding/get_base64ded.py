"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to decode base64 a file until cannot.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import base64


f = open("a.txt","r")
encoded = f.read()
i = 0
for x in range(1,999):
    try:
        i += 1
        encoded = base64.b64decode(encoded)
    except:
        break

print(encoded)
print(i)

