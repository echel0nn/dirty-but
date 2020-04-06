"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

STMCTF image reading from socket.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import socket
import base64
import pytesseract
from PIL import Image
from time import sleep


def netcat(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    content = None
    bd = s.recv(10000)
    print(repr(bd))
    data = s.recv(4096)
    print(repr(data))
    decode_me = base64.b64decode(bd)
    content = decode_me
    f1 = open("read_me.png","wb")
    f1.write(decode_me)
    f1.close()

    print(pytesseract.image_to_string(Image.open('read_me.png')))
    
    data = s.recv(4096)
    s.shutdown(socket.SHUT_WR)
    s.close()



netcat("192.168.120.5",6666)
