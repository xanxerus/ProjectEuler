#!/usr/bin/env pypy

from operator import mul

#find d[n]
def d(goal):
	goal -= 1
	lan = 1
	digit = 1
	while goal >= lan*(10**lan - digit):
		goal -= lan*(10**lan- digit)
		digit = 10**lan
		lan += 1
	
	digit += goal/lan
	
	return int(str(digit)[goal%lan])

print reduce(mul, (d(10**x) for x in xrange(7)))

#it could be more efficient, but I'm too happy with the generalized d[n]
