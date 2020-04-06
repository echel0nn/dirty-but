"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This is a example for attacking one time pad
if the text is english.


================================================
	Y    U    B    I    T    S   E    C
================================================
"""

from CryptoAttacks.Classic import one_time_pad


for i in range(0,100):
    print one_time_pad.break_repeated_key(open("flag.enc","rb").read(), lang='English', no_of_comparisons=100, key_size=i, max_key_size=100)
