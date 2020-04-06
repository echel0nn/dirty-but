"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to decode QR codes given files.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import qrtools
#from qrtools.qrtools import QR
qr = qrtools.QR()
for i in range(0,501):
    qr.decode(str(i)+".png")
    print (qr.data)


