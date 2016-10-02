#!/usr/bin/env pypy

from Lib import ordperm, isprime

def e41():
	for q in reversed(xrange(1, 10)):
		for e in ordperm(map(str, xrange(1, q+1))[::-1]):
			if e[-1] not in (2,4,5,6,8) and isprime(int(e)):
				return int(e)

print e41()

#brute force all the pandigitals
#1+2+3+4+5+6+7+8+9 % 3 == 0
#1+2+3+4+5+6+7+8 % 3 == 0
