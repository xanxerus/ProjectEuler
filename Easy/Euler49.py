#!/usr/bin/env pypy

from Lib import ordcomb, era
from itertools import permutations

def e49():
	primes = set(era(10**5))
	for e in ordcomb(L=4):
		arr = sorted(filter(lambda n: n in primes, (int(''.join(s)) for s in permutations(e))))
		if len(arr) >= 3:
			for a in xrange(len(arr)):
				for b in xrange(a+1, len(arr)):
					for c in xrange(b+1, len(arr)):
						if arr[b] - arr[a] == arr[c] - arr[b] != 0 and arr[a] != 1487:
							return ''.join(map(str, (arr[a], arr[b], arr[c])))

print e49()
