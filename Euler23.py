#!/usr/bin/env pypy
from math import sqrt
from Lib import memoize

L = 28123

@memoize
def isabundant(n):
	if n <= 1:
		return False

	ret = 1

	if n == int(sqrt(n))**2:
		ret -= int(sqrt(n))

	for x in xrange(2, 1+int(sqrt(n))):
		if n%x==0:
			ret += x + n/x
		if ret > n:
			return True
	
	return ret > n


abundant = [x for x in xrange(L) if isabundant(x)]

ret = 0

for x in xrange(28123):
	for y in abundant:
		if y < x and isabundant(x-y):
			break
	else:
		ret += x

print ret
