#!/usr/bin/pypy
#Euler 63
from math import log10 as log
ret = 0
for x in xrange(1, 10):
	ret += int(log(10)/(log(10)-log(x)))

print ret
