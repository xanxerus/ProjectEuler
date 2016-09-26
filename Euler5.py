#!/usr/bin/env pypy
from Lib import era

def e5(n=20):
	ret = 1
	primes = era(n)
	for p in primes:
		r = p
		while r < n:
			r*=p
		ret *= r/p
	return ret

print e5()
