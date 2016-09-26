#!/usr/bin/env pypy

ret = 0
a, b = 1, 2

while b < 4e6:
	if not b&1:
		ret += b
	a, b = b, a+b

print ret
