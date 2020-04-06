"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to unhexlify the given inputs.
The format must be "{1-f}{1-f] ... " so on.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""
f = open("text","r")
f2 = open("dec","wb")



from os import
ic = f.read()
ic = ic.split(" ")
print(ic)
for hx in ic:
    if len(hx) > 2:
        temp = hx[0] + hx[1]
        f2.write(bytearray.fromhex(temp))
    else:
        f2.write(bytearray.fromhex(hx))


