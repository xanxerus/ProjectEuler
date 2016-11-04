#!/usr/bin/env pypy
from itertools import count

def e52(L=6):
	for n in count(1):
		q = sorted(str(n))
		if all(q == sorted(str(k*n)) for k in xrange(2, L+1)):
			return n #[k*n for k in xrange(1, L+1)]

print e52()
