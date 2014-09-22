#http://blog.dreamshire.com/project-euler-87/
from projecteuler import prime_sieve, sqrt
def PE87(L):
    P = set()
    p = prime_sieve(int(sqrt(L)))
    for a in p:
        for b in p: 
            qz =  a**4 + b**3
            if qz >= L: break
            for c in p:
                z = c**2 + qz
                if z >= L: break
                P.add(z)
    return len(P) 

print "Project Euler 87 Solution =", PE87(50000000)
