#!/usr/bin/env pypy

from Lib import isprime

def isrighttruncatable(s):
	return not s or isprime(int(s)) and isrighttruncatable(s[1:])

ret = 0
count = 0

row = ['2', '3', '5', '7']

while count < 11:
	nex = set()
	for e in row:
		for d in '1379':
			pot = e + d

			if isrighttruncatable(pot):
				ret += int(pot)
				count += 1

			if isprime(int(pot)):
				nex.add(pot)

	row = nex

print ret
