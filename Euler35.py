#!/usr/bin/env pypy

from Lib import era, allcomb

primes = set(era(10**6))

ret = 1 #count 2

for e in allcomb('13579', 6):
	if all(int(s) in primes for s in ((e[x:] + e[:x] for x in xrange(len(e))))):
		ret += 1

print ret
