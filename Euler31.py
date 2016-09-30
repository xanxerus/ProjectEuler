#!/usr/bin/env pypy

#dynamic programming

def e31(L = 200, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
	arr = [[1] + [0]*L for x in xrange(len(coins))]

	for r in xrange(len(coins)):
		for c in xrange(1, L+1):
			arr[r][c] = arr[r-1][c]
			if coins[r] <= c:
				arr[r][c] += arr[r][c-coins[r]]

	return arr[-1][-1]

print e31()
