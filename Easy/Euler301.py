#!/usr/bin/env pypy

ret = 0
for x in xrange(1, 1+(1<<30)):
	if not (x ^ (x<<1) ^ (3*x)):
		ret += 1

print ret
