#!/usr/bin/env pypy
from Lib import isprime
from itertools import count, combinations

def e51(L=8):
	for x in count(5, 6):
		s = str(x)
		for q in xrange(2, len(s)):
			for p in combinations(range(len(s)), q):
				c = 0
				for d in ('987654321' if 0 in p else '9876543210'):
					pot = ''.join(d if i in p else s[i] for i in xrange(len(s)))
					if not isprime(int(pot)):
						c += 1
					if c > 3:
						break
				else:
					if 0 in p and c == 9-L or 0 not in p and c == 10-L:
						return pot

print e51()
