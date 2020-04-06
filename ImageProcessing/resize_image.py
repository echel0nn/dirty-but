
"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to resize your ducking image.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""
from PIL import Image

im = Image.open("copy.jpg")

pixels = im.getdata()

uzunluk = len(pixels)


pixels = list(im.getdata())
print(len(pixels))

im2 = Image.new("RGB",(92,304))
im2.putdata(pixels)
im2.save("fxed.png")
