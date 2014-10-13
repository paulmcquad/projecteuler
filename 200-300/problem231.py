#http://blog.dreamshire.com/project-euler-231-solution/
#Project Euler Problem 231
from projecteuler import prime_sieve
n, r, s = 20000000, 15000000, 0

for p in prime_sieve(n):
    pj = p
    while pj <= n:
        s += p * (n//pj - r//pj - (n - r)//pj)
        pj *= p

print "Project Euler 231 Solution =", s
