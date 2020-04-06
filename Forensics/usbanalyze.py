"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will try to decode pcap file for USB keyboards.

*unfinished yet*

================================================
	Y    U    B    I    T    S   E    C
================================================
"""


def klavye_convert(bits):
    dict_klavye = {"A":"04","B":"05","C":"06","D":"07",
                    "E":"08","F":"09","G":"0a","H":"0b",
                    "I":"0c","J":"0d","K":"0e","L":"0f",
                    "M":"10","N":"11","O":"12","P":"13",
                    "Q":"14","R":"15","S":"16","T":"17",
                    "U":"18","V":"19","W":"1a","X":"1b",
                    "Y":"1c","Z":"1d","1":"1e","2":"1f",
                    "3":"20","4":"21","5":"22","6":"23",
                    "7":"24","8":"25","9":"26","0":"27",
                    "\n":"28","ESC":"29","DELETE":"2a",
                    "\t":"2b"," ":"2c","-":"2d",
                    "=":"2e","[":"2f","]":"30",
                    "\\":"31",";":"33","'":"34",
                    ",":"36",".":"37","/":"38",
                    "CAPSLOCK":"39"}

    SHIFT_BASILDI = False
    ALT_BASILDI = False
    liste = {}
    kucuk = ""
    bits = str(bits)
    bit1 = str(bits[4])+str(bits[5])
    bits_first = str(bits[0])
    bits_second = str(bits[1])
    kucuk = bits_first+ bits_second
    if kucuk == "02":
        SHIFT_BASILDI = True
    if bit1 == "00" and bits[0] == 0 and bits[1] == 0:
        return None
    for key, value in dict_klavye.items():
        if bit1 == value:
            liste = {"shift":SHIFT_BASILDI,"key":key}
            return liste

f1 = open("text","r")

liste2 = {}
icerik = f1.read()
buyuk_harf = False
icerik = icerik.split("\n")
sts = ""
for _ in range(0,len(icerik)-1):
    try:
        liste2 = klavye_convert(icerik[_])
    except:
        continue
    if liste2 is not None:
        buyuk_harf = liste2['shift']
        a = liste2['key']
        if buyuk_harf:
            sts += a
        else:
            sts += a.lower()

print(sts)
