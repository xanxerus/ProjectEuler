#!/usr/bin/env pypy

def e39(n):
	ret = 0
	for a in xrange(1, n):
		if a*a%(n-a) == 0 and n>2*a:
			ret += 1
	return ret >> 1

m, mp = 0, 0
for p in xrange(2, 1001):
	pot = e39(p)
	if pot > m:
		m, mp = pot, p

print mp

'''
a^2 + b^2 = c^2
a^2 = c^2 - b^2
a^2 = (c-b)(c+b) = xy

p = a+b+c = a+y
y > a
y | a^2

The number of triangles with a perimeter p
is equal to the number of a for which n-a | a^2 and n>2a,
divided by two (because a might not be the smaller side)s
'''
