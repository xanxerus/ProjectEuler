#!/usr/bin/env pypy

Q =23416728348467685
 
def dp_h(N):
  # H[x] is the least k such that you can guarantee a win with a pile of 
  # size x and a move of at move k stones

  # If you take k < H[x] stones, then there will always be a move that
  # the enemy can make to guarantee themselves a win

  H = [0, 1]
  S = 1
  for n in xrange(2, N+1):
    for x in xrange(1, n/3+1):
      if 2*x < H[n-x]:
        S += x
        H.append(x)
        break
    else:
      print 'lonesome', n
      H.append(n)
      S += n
    print 'h(%4s) = %4s (%s)' % (n, H[-1], S)
  return H

def e692(Q=23416728348467685):
  """
  Turns out H(n <= 3) = n and H(n > 3) = min{ x s.t. 2x < H(n-x) }
  H(f) = f for fibonacci number f, and in between is a repeat of H(1...f)
  Which gives a recurrence for G:
  G(f_x) = f_x - f_{x-2} + G(f_{x-1}) + G(f_{x-2})
  And since the goal number was a fibonacci number, this was really useful
  """

  f_2, f_1, f = 1, 2, 3
  g_1, g = 3, 6

  while f < Q:
    # progress the fibonacci numbers
    f_2, f_1, f = f_1, f, f_1 + f

    # progress g
    g_1, g = g, f - f_2 + g + g_1

  return g

print e692()

