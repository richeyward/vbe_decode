#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

RED = "\033[91m"
CLEAR = "\033[0m"

filename = sys.argv[1]

os.system("clear")

decoded = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

charmap="1231232332321323132311233213233211323231311231321323112331123132"
d = [[],[],[],[]]
f = open("map.txt").readlines()
for l in f:
    if l.startswith("#") or l.strip() == "":
        pass
    else:
        d0,d1,d2,d3 = l.partition("#")[0].strip().split(" ")
        d[0].append(d0)
        d[1].append(d1)
        d[2].append(d2)
        d[3].append(d3)

def decode(contents):
    contents = contents[12:-12].replace("@","")
    contents = contents.replace("#&", "\r\n")
    chars = list(contents)
    #print chars
    out = ""
    char_count = 0
    while len(chars) > 0:
        chartype = int(charmap[char_count % len(charmap)])
        char_count += 1
        c = chars[0]
        h = c.encode("hex")
        if h in d[chartype]:
            out += d[0][d[chartype].index(h)].decode("hex")
        else:
            out += RED + c + CLEAR            
        chars.pop(0)
    #Insert newlines
    print out
    print

if os.path.exists(filename):
    fic = open(filename)
    contents = fic.read()
    fic.close()
    tag_init="AAA=="
    tag_end="==^#~@"
    
    code_start = contents.find(tag_init)
    contents = contents[code_start + len(tag_init) - 12:]
    code_end = contents.find(tag_end) - len(tag_end) + 12
    contents = contents[:code_end]
    decode(contents)
