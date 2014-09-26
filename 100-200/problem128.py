#Project Euler Problem 128
#http://blog.dreamshire.com/project-euler-128-solution/

from projecteuler import is_prime

def tiles(L=2000):
    n, c = 1, 1
    while c <= L:
        r = 6 * n
        if is_prime(r-1):
            if is_prime(r+1) and is_prime(2*r+5): c += 1
            if is_prime(r+5) and is_prime(2*r-7): c += 1
        n += 1
    return n-1

n = tiles()
print 3*n*(n - 1) + 2 if is_prime(6*n+1) else 3*n*(n + 1) + 1
