#Project Euler Problem 125
#http://blog.dreamshire.com/project-euler-125-solution/
from projecteuler import is_palindromic

L = 10**8
sqrt_limit = int(L ** 0.5)    
pal = set()

for i in range(1, sqrt_limit-1):
    sos = i*i
    for j in xrange(i+1, sqrt_limit):
        sos += j*j
        if sos >= L: break
        if is_palindromic(sos): pal.add(sos)

print "Answer to PE125 =", sum(pal), len(pal)
