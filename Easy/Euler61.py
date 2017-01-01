#!/usr/bin/pypy
#Euler 61

from itertools import count

fun = [
lambda x: x*(x+1)>>1,
lambda x: x**2,
lambda x: x*(3*x-1)>>1,
lambda x: x*(2*x-1),
lambda x: x*(5*x-3)>>1,
lambda x: x*(3*x-2)
]
arr = [dict() for x in xrange(6)]

for y in xrange(6):
	for x in count(1):
		pot = fun[y](x)
		if 1000 <= pot <= 10000:
			if pot%100 in arr[y]:
				arr[y][pot%100].add(pot/100)
			else:
				arr[y][pot%100] = {pot/100}
		if pot > 9999:
			break

soln = None
def recur(sofar=None, types=None):
	global soln
	if types is None:
		types = set(xrange(6))

	if sofar and len(sofar)==7 and sofar[0] == sofar[6]:
		soln = sum(sofar[:-1]) + sum(sofar[:-1])*100

	if sofar is None:
		for t in types:
			for k in arr[t]:
				for v in arr[t][k]:
					recur([k, v], types - {t})
	elif len(sofar) < 7:
		for t in types:
			for v in arr[t].get(sofar[-1], []):
				recur(sofar + [v], types - {t})

recur()
print soln
