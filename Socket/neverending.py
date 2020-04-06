#!/usr/bin/python3
"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by LVMBDV
@ 26 Kas 2017

================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import socket

printable = "".join(map(chr, range(0x20, 0x7F)))

def deduce_key(p, c):
    return printable.index(c) - printable.index(p)

def decrypt(c, k):
    return printable[(printable.index(c) - k) % len(printable)]

TEST_CHAR = "a"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("neverending.tuctf.com", 12345))
    buf = ""
    while True:
        if buf.endswith("Give me some text:"):
            s.send((TEST_CHAR + "\n").encode("ascii"))
            buf += s.recv(16).decode("ascii")
            c = buf[-1]
            k = deduce_key(TEST_CHAR, c)
            print("Found key:", k)
            buf = ""
        elif buf.endswith(" decrypted?\n:"):
            ct = buf[buf.find("What is ") + len ("What is "):buf.find(" decrypted")]
            print(ct)
            pt = "".join(map(lambda c: decrypt(c, k), ct)) + "\n"
            print("Decrypted:", pt.strip())
            s.send(pt.encode("ascii"))
            buf = ""
        c = s.recv(1).decode("ascii")
        if len(c) == 0:
            break
        else:
            buf += c
    print(buf.strip())
