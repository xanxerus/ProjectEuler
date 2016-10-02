#!/usr/bin/env pypy

open('p042_words.txt')


arr = range(1, 20*ord('Z')) #liberal guess

for i in xrange(1, len(arr)): #trianglify, dp style
	arr[i] += arr[i-1]

arr = set(arr) #make lookupable

print len(filter(lambda s: sum(ord(c) - ord('A') + 1 for c in s) in arr, open('p042_words.txt').read()[1:-1].split('","')))
