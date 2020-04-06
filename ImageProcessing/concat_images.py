"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to concat your images in very
primal way. 
Do not forget to change the variables
for suitable for your task.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""
from PIL import Image



width = 200*2

height = 40


new_image = Image.new('RGBA',(width,height))


for i in range(1,201):
    temp_im = Image.open(str(i)+".png")
    new_image.paste(temp_im,((i*2),0))

new_image.save("new-image.png")
