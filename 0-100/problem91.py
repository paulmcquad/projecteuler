#http://blog.dreamshire.com/project-euler-91-solution/
from projecteuler import gcd

n = 50
t = 0
for x in range(1, n+1):
    for y in range(1, n):
        m = gcd(x, y)
        t += min(x*m/y, m*(n-y)/x)

print 'Project Euler 91 Solution =', t*2 + n*n*3
