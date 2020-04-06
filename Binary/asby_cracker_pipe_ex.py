
"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017
This is a example for pipes.
Use with asby.exe. (PE32 executable)

================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import subprocess

def getp():
    p=subprocess.Popen(['asby.exe'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return p

def tryflag(p, possible_flag):
    command = possible_flag + '\r\n'
    p.stdin.write(command)
    for i in range(len(possible_flag)):
        response=p.stdout.readline()
        if 'WRONG!' in response:
            return False
    return True

p = getp()
assert(tryflag(p, 'flag{'))
assert(tryflag(p, 'flag{0'))

flag = 'flag{'

for x in range(32):
    for y in range(16):
        c = '%x' % y
        if tryflag(p, flag + c):
            print(flag)
            flag += c
            break

flag += '}'
print(flag)
