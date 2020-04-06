"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

Random example usage of requests library.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import requests

r = requests.get('https://count.problem.ctf.nw.fit.ac.jp/')

rand_add = r.cookies['rand_add']
count = r.cookies['count']
kuki = {"rand_add":rand_add,"count":count}
while count != 96:
	r = requests.post('https://count.problem.ctf.nw.fit.ac.jp/',data={'username':rand_add},cookies=kuki)
	rand_add = r.cookies['rand_add']
	count = r.cookies['count']
	print("Count:",count)
	print("Adding:",rand_add)
	kuki = {"rand_add":rand_add,"count":count}
	r = requests.get('https://count.problem.ctf.nw.fit.ac.jp/',cookies=kuki)
	print("Cookies:",str(r.cookies))
print(r.text)

