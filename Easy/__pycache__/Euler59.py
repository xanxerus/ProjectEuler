#!/usr/bin/env pypy
from collections import Counter

def e59():
	arr = map(int, open("p059_cipher.txt").readline().strip().split(","))
	
	first = arr[::3]
	second = arr[1::3]
	third = arr[2::3]
	
	e = ord('e')
	e1 = Counter(first).most_common()[0][0]
	e2 = Counter(second).most_common()[0][0]
	e3 = Counter(third).most_common()[0][0]
	key = chr(e1).lower() + chr(e2).lower() + chr(e3).lower()

	return sum(arr[i] ^ ord(key[i%3]) for i in xrange(len(arr)))

print e59()
