#!/usr/bin/env pypy
from Lib import besieve

def numfactors(be1, be2):
	ret = 1
	be2[2] -= 1
	for e in be1.values():
		ret *= e+1
	for e in be2.values():
		ret *= e+1
	return ret

def e12(G=500, L=15000):
	arr = besieve(L)

	for i in xrange(2, L-1, 2):
		if numfactors(arr[i-1], arr[i]) > G:
			return i*(i-1)>>1
		if numfactors(arr[i+1], arr[i]) > G:
			return i*(i+1)>>1

print e12()
