#!/usr/bin/env pypy

ret = 0
for a in xrange(100, 1000):
	for b in xrange(a, 1000):
		m = a*b
		if str(m) == str(m)[::-1] and m > ret:
			ret = m

print ret
