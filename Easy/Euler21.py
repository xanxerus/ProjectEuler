#!/usr/bin/env pypy
from math import sqrt

L = 10000

def d(n):
	if n <= 1:
		return 1

	ret = 1
	for x in xrange(2, 1+int(sqrt(n))):
		if n%x==0:
			ret += x + n/x
	
	if n == int(sqrt(n))**2:
		ret -= int(sqrt(n))
	
	return ret

ret = 0
for a in xrange(2, L+1):
	b = d(a)
	if b>a and d(b) == a:
		ret += a + b

print ret
#just brute force
