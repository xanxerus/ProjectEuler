#!/usr/bin/env pypy

from Lib import factorial

fac = [1] + range(1, 10)

for i in xrange(1, 10):
	fac[i] *= fac[i-1]

ret = 0
for x in xrange(3, 10**5):
	if x == sum(fac[int(c)] for c in str(x)):
		ret += x

print ret
