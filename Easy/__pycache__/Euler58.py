#!/usr/bin/env pypy
from itertools import count
from Lib import isprime

def e58():
	c = 0
	for layer in count(2):
		p = (layer-1 << 1)**2 + 1
		q = p - (layer-1 << 1)
		r = p + (layer-1 << 1)
		
		if isprime(p):
			c += 1
		if isprime(q):
			c += 1
		if isprime(r):
			c += 1

		d = 1 + (layer-1 << 2)

		if c*10 < d:
			return (layer-1<<1)+1

print e58()

