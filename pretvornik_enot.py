#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dobrodošli v pretvorniku razdalj" # začetek programa in vnos vrednosti
vrednost = float(raw_input("Vnesi število kilometrov:"))
print vrednost*0.62, "milj"
print "Želite vnesti novo vrednost za pretvorbo? Za nadaljevnje vpišite DA, sicer NE"
ponovnavrednost = raw_input("")

while True: # nadaljnje pretvorbe vrednosti, če zahtevano
    if ponovnavrednost == "NE":
        print "Goodbye"
        break
    elif ponovnavrednost == "DA":
        vrednost = float(raw_input("Vnesi število kilometrov:"))
        print vrednost*0.62, "milj"
        print "Želite vnesti novo vrednost za pretvorbo? Za nadaljevnje vpišite DA, sicer NE"
        ponovnavrednost = raw_input("")
