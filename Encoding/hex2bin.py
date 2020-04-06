"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017


It will try to unhexlify the given hex inputs
with 6 / 4 / 2 pairs, then creates a new file.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import binascii

#with open("hex") as f, open("binary",'wb') as fout:
#    for line in f:
#        fout.write(
#                binascii.unhexlify(''.join(line.split()))


f = open("hex")
fout = open("test","wb+")
icerik = f.read()
icerik = icerik.replace("\n","")
icerik = icerik.split(" ")
sts = ""
temp = ""
temp2 = ""
temp3 = ""
for h in icerik:
    if len(h) == 4:
        temp = h[0] + h[1]
        temp2 = h[2] + h[3]
        temp = str(temp)
        temp2 = str(temp2)
        fout.write(binascii.unhexlify(temp))
        fout.write(binascii.unhexlify(temp2))
        sts = sts + temp + temp2
    elif len(h) == 6:
        temp = h[0] + h[1]
        temp2 = h[2] + h[3]
        temp3 = h[4] + h[5]
        temp = str(temp)
        temp2 = str(temp2)
        temp3 = str(temp3)
        fout.write(binascii.unhexlify(temp))
        fout.write(binascii.unhexlify(temp2))
        fout.write(binascii.unhexlify(temp3))
        sts = sts + temp + temp2 + temp3
    elif len(h) == 2:
        sts = sts + h
        fout.write(binascii.unhexlify(h))
print(sts)
print(len(icerik))

