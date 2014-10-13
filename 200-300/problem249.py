#http://blog.dreamshire.com/project-euler-249-solution/
#Project Euler Problem 249

from projecteuler import prime_sieve, is_prime

primes = prime_sieve(5000)
t = [1] + [0] * sum(primes)

sp = 0
for p in primes:
    sp += p
    for j in range(sp, p-1, -1):
        t[j] = (t[j] + t[j-p])

print "Project Euler 249 Solution =", (sum(t[p] for p in range(sp) if is_prime(p)) % 10**16)
