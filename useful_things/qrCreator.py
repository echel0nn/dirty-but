"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to encode your input to QR code.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

f1 = open("tokens","r")

ic = f1.read()
ic = ic.split("\n")
asd = 0
import qrcode
for i in ic:

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(i)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(str(asd)+".png","PNG")
    asd += 1
