#!/usr/bin/env pypy
from itertools import count
from Lib import isprime, era, memoize

primes = era(1000)
mn, ma, mb = 0, 0, 0
for a in xrange(-999, 1000):
	for b in primes:
		for n in count(0):
			if not isprime(n*n + a*n + b):
				break
		if n > mn:
			mn, ma, mb = n, a, b

print ma*mb
#brute force, duh
#for n=0, b must be prime
