#!/usr/bin/env pypy

L = 100
print sum(range(L)) ** 2 - sum(x**2 for x in range(L))
