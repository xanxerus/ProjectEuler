#!/usr/bin/env pypy
from Lib import befactorize

print max(befactorize(600851475143, sieve=False).keys())
