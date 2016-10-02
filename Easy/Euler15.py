#!/usr/bin/env pypy

#It's Pascal's Matrix
def e15(L=20):
	L += 1
	arr = [[1]*L] + [[1] + [0]*(L-1)]*(L-1)
	for r in xrange(1, L):
		for c in xrange(1, L):
			arr[r][c] = arr[r-1][c] + arr[r][c-1]
	return arr[-1][-1]

print e15()
