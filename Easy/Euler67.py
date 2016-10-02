#!/usr/bin/env pypy

arr = [map(int, line.split()) for line in open('p067_triangle.txt')]

for r in xrange(1, len(arr)):
	for c in xrange(len(arr[r])):
		if c==0:
			arr[r][c] += arr[r-1][c]
		elif c == len(arr[r])-1:
			arr[r][c] += arr[r-1][c-1]
		else:
			arr[r][c] += max(arr[r-1][c], arr[r-1][c-1])

print max(arr[-1])

