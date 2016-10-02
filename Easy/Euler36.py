#!/usr/bin/env pypy

ret = 0
for x in xrange(1, 1000):
	a = int(str(x) + str(x)[:-1][::-1])
	b = int(str(x) + str(x)[::-1])
	
	if bin(a)[2:] == bin(a)[:1:-1]:
		ret += a
	if bin(b)[2:] == bin(b)[:1:-1]:
		ret += b

print ret
