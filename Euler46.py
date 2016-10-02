#!/usr/bin/env pypy

from Lib import era, besieve

def e46(L=10**4):
	primes = era(L)
	factors = besieve(L)

	for x in xrange(3, L, 2):
		if x in primes:
			continue
		
		for p in primes:
			if p >= x:
				return x
			pot = factors[x-p]
			if pot.get(2, 0) & 1 and all(pot[k]%2==0 for k in pot if k != 2):
				break

print e46()
