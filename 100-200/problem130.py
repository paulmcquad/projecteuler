#Project Euler Problem 130
#http://blog.dreamshire.com/project-euler-130-solution/

from projecteuler import is_prime

dnp = set()    # set of deceptive non-primes
L = 25
n = 91    # start with first valid n given in the problem description

while len(dnp) < L:
    if not is_prime(n) and pow(10, n-1, 9*n) == 1:
        dnp.add(n)
    n += 2

print "Project Euler 130 Solution =", sum(dnp)
