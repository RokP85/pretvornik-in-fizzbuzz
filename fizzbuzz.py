#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dobrodošli v fizzbuzz igri!"
seznam = int(raw_input("Vnesi celo število 1-100:"))

for int in range(1, seznam+1):
    if int % 3 == 0 and int % 5 == 0:
        print "fizzbuzz"
    elif int % 5 == 0:
        print "buzz"
    elif int % 3 == 0:
        print "fizz"
    else:
        print int
