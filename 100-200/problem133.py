#Project Euler Problem 133
#http://blog.dreamshire.com/project-euler-133-solution/
from projecteuler import prime_sieve
L, q, s = 100000, pow(10, 20), 2+3

s += sum(p for p in prime_sieve(L)[2:] if pow(10, q, p) != 1)
 
print "Project Euler 133 Solution = ", s
