"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017


Meh.

================================================
	Y    U    B    I    T    S   E    C
================================================
"""
import socket
import sys
import string

state_capitals={"Washington":"Olympia","Oregon":"Salem",\
                "California":"Sacramento","Ohio":"Columbus",\
                "Nebraska":"Lincoln","Colorado":"Denver",\
                "Michigan":"Lansing","Massachusetts":"Boston",\
                "Florida":"Tallahassee","Texas":"Austin",\
                "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                "Alaska":"Juneau","Utah":"Salt Lake City",\
                "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                "South Dakota":"Pierre","West Virginia":"Charleston",\
                "Virginia":"Richmond","New Jersey":"Trenton",\
                "Minnesota":"Saint Paul","Illinois":"Springfield",\
                "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                "Tennessee":"Nashville","Georgia":"Atlanta",\
                "Alabama":"Montgomery","Mississippi":"Jackson",\
                "North Carolina":"Raleigh","South Carolina":"Columbia",\
                "Maine":"Augusta","Vermont":"Montpelier",\
                "New Hampshire":"Concord","Connecticut":"Hartford",\
                "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                "Montana":"Helena","Kansas":"Topeka",\
                "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                "Maryland":"Annapolis","Missouri":"Jefferson City",\
                "Arizona":"Phoenix","Nevada":"Carson City",\
                "New York":"Albany","Wisconsin":"Madison",\
                "Delaware":"Dover","Idaho":"Boise",\
                "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

server = "34.253.165.46"
port = 11223
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] Connecting to: 34.253.165.46"
try:
    s.connect((server, port))
except Exception as e:
    print e
ban=s.recv(1024)
print ban
while 1:
    text=s.recv(1024)
    print text 
    if "Bugs" in text:
        quit()
    if "=" in text:
        a,b = text.split(" = ")
        if "+" in a:
            x,y = a.split("+")
            s.send(str(int(b)-int(y)))
        if "-" in a:
            x,y = a.split("-")
            s.send(str(int(b)+int(y)))
        if "*" in a:
            x,y = a.split("*")
            s.send(str(int(b)/int(y)))
        if "/" in a:
            x,y = a.split("*")
            s.send(str(int(b)*int(y)))
    state = text.split(".: ")[1]
    print state
    state = state.strip()
    print "[+] Searching..."
    if state in state_capitals.keys():
        print "[+] Success ! "+state_capitals.get(state)
        s.send(state_capitals.get(state))
