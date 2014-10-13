L, s = 1000000, 0

for n in xrange(2, L):
    x0, x1 = 0, n
    while x0 != x1 and x1:
        x0, x1 = x1, pow(n, x0, 10**9)
    s += x1

print "Project Euler 455 Solution =", s
