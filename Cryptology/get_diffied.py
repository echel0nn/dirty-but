
"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This is a example for diffie-hellman.

================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import itertools

q=442101689710611
g=10

list_a = []
list_b = []
list_ab = []

def append_(g,q):
    for x in range(g*q):
        if g**x % q == 421049228295820:
            list_a.append(x)
        if g**x % q == 105262307073955:
            list_b.append(x)


def iter_(list_a,list_b):
    for i in itertools.product(list_a,list_b):
        if i[0] > 1000 or i[1] > 1000:
            continue
        exp = i[0] * i[1]
        if g**exp % q ==33:
            ab = str(i[0]) +"," + str(i[1])
            if ab not in list_ab:
                list_ab.append(ab)
    return list_ab

append_(g,q)
list_ab = iter_(list_a,list_b)
for aveb in list_ab:
    print(aveb)
