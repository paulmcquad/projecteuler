#http://blog.dreamshire.com/project-euler-242-solution/
#Project Euler Problem 242
from math import log

def f(n):
    if n == 0:
        return 0
    if n < 5:
        return 1
    k = int(log(n, 2))
    return 3**(k-2) + 2*f(n - 2**k)
    
print "Project Euler 242 Solution =", f(10**12)
