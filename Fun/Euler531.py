#!/usr/bin/env pypy
'''
x === a mod n
x === b mod m

x = a + sn
a + sn === b mod m
sn === (b-a)%m mod m
s === (b-a)%m * MMI(n, m)%m mod m
s = (b-a)%m * MMI(n, m)%m + tm
x = a + ( (b-a)%m * MMI(n, m)%m + tm) * n
x = a + n * ((b-a)%m * MMI(n, m)%m) + tnm
'''

from Lib import hm, merge, MMI
from fractions import gcd as gcdu, Fraction as F
from time import time
gcd = lambda *t: reduce(gcdu, t)

def totfac(L):
	tots = range(L+1)
	facs = [dict(), dict()] + [0]*(L-1)
	
	for x in xrange(2, L+1):
		if tots[x] == x:
			tots[x] = x-1
			facs[x] = {x:1}
			for y in xrange(x<<1, L+1, x):
				if isinstance(facs[y], int):
					facs[y] = (x, hm(y, x))
				tots[y] *= 1 - F(1, x)
		else:
			tots[x] = tots[x].numerator

			q = facs[x][0]**facs[x][1]
			facs[x] = {facs[x][0] : facs[x][1]}
			if q != x:
				facs[x] = merge(facs[x], facs[x/q])

	return tots, facs

def crt(*args):
	a, n = 0, 1
	for b, m in args:
		a += ((b-a)%m) * (MMI(n, m)%m) * n
		n *= m
	return a%n

def g(a, n, b, m):
	D = gcd(n, m)
	ret = None
	if a%D == b%D:
		if a%D or b%D:
			DA = gcd(a, b, n, m)
			if DA != 1:
				return DA*g(a/DA, n/DA, b/DA, m/DA)
			else:
				pairs = set()
				for k in facs[n]:
					p = k**facs[n][k]
					pairs.add((a%p, p))
				for k in facs[m]:
					p = k**facs[m][k]
					pairs.add((b%p, p))
				return crt(*pairs)
		elif D != 1:
			return D*g(a/D, n/D, b/D, m/D)
		else:
			return a + n * ((MMI(n, m)%m) * (b-a)%m)
	else:
		return 0

def e531(L=1000000, U=1005000):
	global tots, facs
	tots, facs = totfac(U)
	ret = 0
	for m in xrange(L, U):
		for n in xrange(L, m):
			ret += g(tots[n], n, tots[m], m)
	return ret

print e531()
