#!/usr/bin/pypy -i

from fractions import Fraction as F, gcd
from itertools import count
from time import time

def awesometotient(n):
	arr = [0, 1] + range(-2, -n-1, -1)

	for x in xrange(2, n+1):
		if arr[x] < 0:
			arr[x] = x-1
			for y in xrange(x<<1, n+1, x):
				if arr[y] < 0:
					arr[y] = y*F(x-1, x)
				else:
					arr[y] *= F(x-1, x)
		else:
			arr[x] = arr[x].numerator

	return arr

def woow(n=10**18):
	s = 1
	ret = 1
	tarr = awesometotient(min(n, 10**7))

	for d in count(3):
		if s >= n:
			break

		t = tarr[d]>>1
		if s+t*d < n:
			s += t*d
			ret += t
		else:
			for u in xrange(1, (d>>1)+1):
				if gcd(d, u) == 1:
					s += d
					ret += 1
					if s >= n:
						break

	return ret<<1

#~ for i in (1, 3, 9, 11, 100, 50000, 10**18):
	#~ t = time()
	#~ print i, woow(i), time()-t
print woow()-1, 'give or take 1'
