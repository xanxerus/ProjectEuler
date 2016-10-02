#!/usr/bin/env pypy

arr = map(lambda s: sum(ord(c) - ord('A') + 1 for c in s), sorted(open('p022_names.txt').read()[1:-1].split('","')))
print sum( (x+1)*arr[x] for x in xrange(len(arr)) )
