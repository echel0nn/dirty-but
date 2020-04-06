"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

Example for changing RGB values to hex values.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

from PIL import Image

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

f = Image.open("uu.jpg")
f2 = open("hexes.txt","w")
pixels = list(f.getdata())
sts = ""
hexes = ""
blacks = None
for pixel in pixels:
    if "(0, 0, 0)" in repr(pixel):
	 for r, g, b in pixels:
	     sts = rgb2hex(r, g, b)
	     print(sts)
print(len(pixels))
