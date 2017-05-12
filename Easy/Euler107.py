#!/usr/bin/env pypy
import heapq

edges = dict()

Q = 0 #twice the original weight
r = 0 #row
for line in open('p107_network.txt'):
	c = 0 #col
	for e in line.strip().split(','):
		if e != '-':
			Q += int(e)
			if r in edges:
				edges[r].append((int(e), c))
			else:
				edges[r] = [(int(e), c)]
		c += 1
	r += 1

#~ print edges

#prim!
used = {0}
frontier = edges[0][:] #heap
heapq.heapify(frontier)

ret = 0
while frontier:
	e = heapq.heappop(frontier)
	
	if e[1] not in used:
		ret += e[0]
		used.add(e[1])
		for pot in edges[e[1]]:
			heapq.heappush(frontier, pot)

print Q/2-ret
