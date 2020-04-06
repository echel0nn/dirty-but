"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will reverse your file.

================================================
	Y    U    B    I    T    S   E    C
================================================
"""

f = open("UNKnOWN","rb")

f2 = open("reversed2","wb")

icerik = f.read()

f2.write(bytes(reversed(icerik)))

