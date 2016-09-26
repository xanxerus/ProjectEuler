#!/usr/bin/env pypy
def e14(L = 10**6):
	m = 0
	i = 0
	arr = [0]*L

	for s in xrange(2, L):
		t = 0
		x = s
		while True:
			if x < s:
				t += arr[x]
				break

			t += 1
			x = 3*x+1 if x&1 else x>>1

		arr[s] = t
		if t > m:
			m = t
			i = s
	return i

print e14()
