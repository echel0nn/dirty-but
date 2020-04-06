"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

Yes it is not normal.


================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import socket
from time import sleep


def netcat(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    content = None
    while True:
        data = s.recv(4096)
        print(repr(data))
        if "Clarity" in repr(data):
            content = "50\n"
            s.sendall(content.encode())
        if "Iron Branch" in repr(data):
            content = "50\n"
            s.sendall(content.encode())
        if "Wind Lace" in repr(data):
            content = "250\n"
            s.sendall(content.encode())
        if "Magic Wand" in repr(data):
            content = "465\n"
            s.sendall(content.encode())
        if "Basilius" in repr(data):
            content = "500\n"
            s.sendall(content.encode())
        if "Glimmer" in repr(data):
            content = "1850\n"
            s.sendall(content.encode())
        if "Crystalys" in repr(data):
            content = "2120\n"
            s.sendall(content.encode())
        if "Defiance" in repr(data):
            content = "1725\n"
            s.sendall(content.encode())
        if "Madness" in repr(data):
            content = "1900\n"
            s.sendall(content.encode())
        if "Energy Boost" in repr(data):
            content = "900\n"
            s.sendall(content.encode())
        if "Faerie Fire" in repr(data):
            content = "75\n"
            s.sendall(content.encode())
        if "Gauntlets" in repr(data):
            content = "150\n"
            s.sendall(content.encode())
        if "Stout Shield" in repr(data):
            content = "200\n"
            s.sendall(content.encode())
        if "Magic Stick" in repr(data):
            content = "200\n"
            s.sendall(content.encode())
        if "Null Talisman" in repr(data):
            content = "470\n"
            s.sendall(content.encode())
        if "Iron Talon" in repr(data):
            content = "500\n"
            s.sendall(content.encode())
        if "Force Staff" in repr(data):
            content = "2225\n"
            s.sendall(content.encode())
        if "Mordiggian" in repr(data):
            content = "2370\n"
            s.sendall(content.encode())
        if "Vanguard" in repr(data):
            content = "2150\n"
            s.sendall(content.encode())
        if "Dominator" in repr(data):
            content = "1800\n"
            s.sendall(content.encode())
        if "Point Booster" in repr(data):
            content = "1850\n"
            s.sendall(content.encode())
        if "Mango" in repr(data):
            content = "110\n"
            s.sendall(content.encode())
        if "Slippers" in repr(data):
            content = "150\n"
            s.sendall(content.encode())
        if "Quelling" in repr(data):
            content = "200\n"
            s.sendall(content.encode())
        if "Sage's Mask" in repr(data):
            content = "325\n"
            s.sendall(content.encode())
        if "Wraith Band" in repr(data):
            content = "485\n"
            s.sendall(content.encode())
        if "Headress" in repr(data):
            content = "575\n"
            s.sendall(content.encode())
        if "Discord" in repr(data):
            content = "2240\n"
            s.sendall(content.encode())
        if "Shadow Blade" in repr(data):
            content = "2700\n"
            s.sendall(content.encode())
        if "Blade Mail" in repr(data):
            content = "2200\n"
            s.sendall(content.encode())
        if "Dragon Lance" in repr(data):
            content = "1900\n"
            s.sendall(content.encode())
        if "Vitality Booster" in repr(data):
            content = "1100\n"
            s.sendall(content.encode())
        if "Tango" in repr(data):
            content = "125\n"
            s.sendall(content.encode())
        if "Mantle" in repr(data):
            content = "150\n"
            s.sendall(content.encode())
        if "Infused" in repr(data):
            content = "225\n"
            s.sendall(content.encode())
        if "Ring Of Regen" in repr(data):
            content = "325\n"
            s.sendall(content.encode())
        if "Poor Man's Shield" in repr(data):
            content = "500\n"
            s.sendall(content.encode())
        if "Buckler" in repr(data):
            content = "800\n"
            s.sendall(content.encode())
        if "Aether Lens" in repr(data):
            content = "2350\n"
            s.sendall(content.encode())
        if "Skull Basher" in repr(data):
            content = "2700\n"
            s.sendall(content.encode())
        if "Soul Booster" in repr(data):
            content = "3200\n"
            s.sendall(content.encode())
        if "Sange" in repr(data):
            content = "2050\n"
            s.sendall(content.encode())
        if "Platemail" in repr(data):
            content = "1400\n"
            s.sendall(content.encode())
        if "Healing Salve" in repr(data):
            content = "110\n"
            s.sendall(content.encode())
        if "Circlet" in repr(data):
            content = "165\n"
            s.sendall(content.encode())
        if "Blight Stone" in repr(data):
            content = "1850\n"
            s.sendall(content.encode())
        if "Boots Of Speed" in repr(data):
            content = "400\n"
            s.sendall(content.encode())
        if "Bracer" in repr(data):
            content = "505\n"
            s.sendall(content.encode())
        if "Urn Of Shadows" in repr(data):
            content = "875\n"
            s.sendall(content.encode())
        if "Necronomicon" in repr(data):
            content = "2650\n"
            s.sendall(content.encode())
        if "Battle Fury" in repr(data):
            content = "4500\n"
            s.sendall(content.encode())
        if "Crimson Guard" in repr(data):
            content = "3550\n"
            s.sendall(content.encode())
        if "Yasha" in repr(data):
            content = "2050\n"
            s.sendall(content.encode())
        if "Talisman Of Evasion" in repr(data):
            content = "1450\n"
            s.sendall(content.encode())
        if "Smoke Of Deceit" in repr(data):
            content = "50\n"
            s.sendall(content.encode())
        if "Belt Of Strength" in repr(data):
            content = "450\n"
            s.sendall(content.encode())
        if "Orb Of Venom" in repr(data):
            content = "275\n"
            s.sendall(content.encode())
        if "Gloves Of Haste" in repr(data):
            content = "500\n"
            s.sendall(content.encode())
        if "Soul Ring" in repr(data):
            content = "800\n"
            s.sendall(content.encode())
        if "Tranquil" in repr(data):
            content = "900\n"
            s.sendall(content.encode())
        if "Dagon" in repr(data):
            content = "2720\n"
            s.sendall(content.encode())
        if "Ethereal Blade" in repr(data):
            content = "4700\n"
            s.sendall(content.encode())
        if "Black King Bar" in repr(data):
            content = "3975\n"
            s.sendall(content.encode())
        if "Echo Sabre" in repr(data):
            content = "2650\n"
            s.sendall(content.encode())
        if "Hyperstone" in repr(data):
            content = "2000\n"
            s.sendall(content.encode())
        if "Town Portal" in repr(data):
            content = "50\n"
            s.sendall(content.encode())
        if "Elvenskin" in repr(data):
            content = "450\n"
            s.sendall(content.encode())
        if "Blades Of Attack" in repr(data):
            content = "420\n"
            s.sendall(content.encode())
        if "Cloak" in repr(data):
            content = "550\n"
            s.sendall(content.encode())
        if "Phase Boots" in repr(data):
            content = "1240\n"
            s.sendall(content.encode())
        if "Aquila" in repr(data):
            content = "985\n"
            s.sendall(content.encode())
        if "Scepter Of Divinity" in repr(data):
            content = "2750\n"
            s.sendall(content.encode())
        if "Silver Edge" in repr(data):
            content = "5100\n"
            s.sendall(content.encode())
        if "Lotus Orb" in repr(data):
            content = "4000\n"
            s.sendall(content.encode())
        if "Maelstrom" in repr(data):
            content = "2800\n"
            s.sendall(content.encode())
        if "Ultimate Orb" in repr(data):
            content = "2100\n"
            s.sendall(content.encode())
        if "Dust Of Appearance" in repr(data):
            content = "180\n"
            s.sendall(content.encode())
        if "Robe Of The Magi" in repr(data):
            content = "450\n"
            s.sendall(content.encode())
        if "Chainmail" in repr(data):
            content = "550\n"
            s.sendall(content.encode())
        if "Ring of Health" in repr(data):
            content = "850\n"
            s.sendall(content.encode())
        if "Power Treads" in repr(data):
            content = "1350\n"
            s.sendall(content.encode())
        if "Medallion Of Courage" in repr(data):
            content = "1175\n"
            s.sendall(content.encode())
        if "Solar Crest" in repr(data):
            content = "2625\n"
            s.sendall(content.encode())
        if "Radiance" in repr(data):
            content = "5150\n"
            s.sendall(content.encode())
        if "Shiva's Guard" in repr(data):
            content = "4700\n"
            s.sendall(content.encode())
        if "Diffusal Blade" in repr(data):
            content = "3150\n"
            s.sendall(content.encode())
        if "Demon Edge" in repr(data):
            content = "2400\n"
            s.sendall(content.encode())
        if "Animal Courier" in repr(data):
            content = "100\n"
            s.sendall(content.encode())
        if "Ogre Club" in repr(data):
            content = "1000\n"
            s.sendall(content.encode())
        if "Quarterstaff" in repr(data):
            content = "875\n"
            s.sendall(content.encode())
        if "Void Stone" in repr(data):
            content = "850\n"
            s.sendall(content.encode())
        if "Oblivion Staff" in repr(data):
            content = "1650\n"
            s.sendall(content.encode())
        if "Arcane Boots" in repr(data):
            content = "1300\n"
            s.sendall(content.encode())
        if "Rod Of Atos" in repr(data):
            content = "3100\n"
            s.sendall(content.encode())
        if "Monkey King Bar" in repr(data):
            content = "5400\n"
            s.sendall(content.encode())
        if "Bloodstone" in repr(data):
            content = "4900\n"
            s.sendall(content.encode())
        if "Desolator" in repr(data):
            content = "3500\n"
            s.sendall(content.encode())
        if "Mystic Staff" in repr(data):
            content = "2700\n"
            s.sendall(content.encode())
        if "Flying Courier" in repr(data):
            content = "150\n"
            s.sendall(content.encode())
        if "Blade Of Alacrity" in repr(data):
            content = "1000\n"
            s.sendall(content.encode())
        if "Helm Of Iron Will" in repr(data):
            content = "900\n"
            s.sendall(content.encode())
        if "True Sight" in repr(data):
            content = "900\n"
            s.sendall(content.encode())
        if "Perseverance" in repr(data):
            content = "1700\n"
            s.sendall(content.encode())
        if "Drum Of Endurance" in repr(data):
            content = "1780\n"
            s.sendall(content.encode())
        if "Orchid" in repr(data):
            content = "4075\n"
            s.sendall(content.encode())
        if "Daedalus" in repr(data):
            content = "5520\n"
            s.sendall(content.encode())
        if "Manta Style" in repr(data):
            content = "4950\n"
            s.sendall(content.encode())
        if "Halberd" in repr(data):
            content = "3500\n"
            s.sendall(content.encode())
        if "Reaver" in repr(data):
            content = "3000\n"
            s.sendall(content.encode())

    s.shutdown(socket.SHUT_WR)
    s.close()



netcat("139.59.61.220",6666)
