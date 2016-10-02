#!/usr/bin/env pypy

from Lib import ordperm

primes = (2,3,5,7,11,13,17)
ret = 0

for e in ordperm('0123456789'):
	for i in xrange(len(primes)):
		if int(e[1+i:4+i]) % primes[i] != 0:
			break
	else:
		ret += int(e)

print ret

#kinda silly brute force
