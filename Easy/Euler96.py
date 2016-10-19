#!/usr/bin/env pypy

from copy import deepcopy

def printm(arr):
	for row in arr:
		for e in row:
			if isinstance(e, int):
				print '%9s' % ('(%d)' % e),
			else:
				print '%9s' % ''.join(map(str, e)),
		print

def init(board):
	for r in xrange(9):
		for c in xrange(9):
			if board[r][c] == 0:
				s = set(xrange(1,10))
				for x in xrange(9):
					if isinstance(board[r][x], int):
						s.discard(board[r][x])
					if isinstance(board[x][c], int):
						s.discard(board[x][c])

				for dr in xrange(3):
					for dc in xrange(3):
						if isinstance(board[r - r%3 + dr][c - c%3 + dc], int):
							s.discard(board[r - r%3 + dr][c - c%3 + dc])
				
				board[r][c] = s

	return board

def rm(board, n, r, c):
	board[r][c] = n
	for x in xrange(9):
		if isinstance(board[r][x], set):
			board[r][x].discard(n)
			if not board[r][x]:
				return False
		if isinstance(board[x][c], set):
			board[x][c].discard(n)
			if not board[x][c]:
				return False

	for dr in xrange(3):
		for dc in xrange(3):
			if isinstance(board[r - r%3 + dr][c - c%3 + dc], set):
				board[r - r%3 + dr][c - c%3 + dc].discard(n)
				if not board[r - r%3 + dr][c - c%3 + dc]:
					return False

	return eval(board, r, c)

def eval(board, r, c):
	for x in xrange(9):
		if isinstance(board[r][x], set) and len(board[r][x]) == 1:
			if not rm(board, board[r][x].pop(), r, x):
				return False
		if isinstance(board[x][c], set) and len(board[x][c]) == 1:
			if not rm(board, board[x][c].pop(), x, c):
				return False

	for dr in xrange(3):
		for dc in xrange(3):
			if isinstance(board[r - r%3 + dr][c - c%3 + dc], set) and len(board[r - r%3 + dr][c - c%3 + dc]) == 1:
				if not rm(board, board[r - r%3 + dr][c - c%3 + dc].pop(), r - r%3 + dr, c - c%3 + dc):
					return False

	return True

def sudoku(board, r=0, c=0):
	#~ printm(board)
	#~ print r, c
	#~ raw_input()
	nr, nc = r, c+1
	if nc >= 9:
		nr, nc = r+1, 0
		if nr >= 9:
			if all(all(isinstance(e, int) for e in row) for row in board):
				return board
			else:
				return None

	if isinstance(board[r][c], set):
		for e in board[r][c]:
			pot = deepcopy(board)
			if not rm(pot, e, r, c):
				continue
			eval(pot, r, c)
			pot = sudoku(pot, nr, nc)
			if pot:
				return pot
	else:
		return sudoku(board, nr, nc)

def e96(fyl='p096_sudoku.txt', verbose=False):
	ret = 0
	arr = []
	i = 0
	for line in open(fyl):
		if i == 0:
			if verbose:
				print line.strip()
			i += 1
			continue
		elif i == 9:
			arr.append([int(c) for c in line.strip()])
			soln = sudoku(init(arr))
			
			if verbose:
				for row in soln:
					print row
				print
			
			ret += int(''.join(map(str, soln[0][:3])))
			i = 0
			arr = []
		else:
			i += 1
			arr.append([int(c) for c in line.strip()])
	
	return ret
	

print e96()
