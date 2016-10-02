#!/usr/bin/env pypy

from Lib import era, befactorize
from itertools import count

def e47(L=10**6):
	era(L)
	run = 0

	for x in count(2):
		f = befactorize(x)
		if len(f) == 4:
			run += 1
			if run == 4:
				return x-3
		else:
			run = 0

print e47()
