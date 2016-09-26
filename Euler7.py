#!/usr/bin/env pypy
from Lib import era
from math import log

primes = era(120000)
print primes[10000], len(primes)
