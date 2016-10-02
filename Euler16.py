#!/usr/bin/env pypy

print sum(int(c) for c in str(1<<1000))
