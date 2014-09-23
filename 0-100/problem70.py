#https://raw.githubusercontent.com/AaronJiang/ProjectEuler/master/py/problem070.py
"""

Euler's Totient function, phi(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or equal
to n which are relatively prime to n. 

For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and 
relatively prime to nine, phi(9)=6. The number 1 is considered to be 
relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a 
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation 
of n and the ratio n/phi(n) produces a minimum.

I was totally stupid to this phi function problem, and the answers from 
this blog seems clearly enough 
http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/
and the codes comes from 
http://zacharydenton.com/project-euler-solutions/70/
"""

from math import sqrt
from operator import mul
from itertools import *

def primes(n): 
    if n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if sieve[i]:
            j = (m * m - 3) / 2
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [p for p in sieve if p]

def main():
    pairs = combinations(primes(2 * int(sqrt(1e7))), 2)
    minimum = (100, 0)
    for n, t in ((a * b, (a-1) * (b-1)) for a, b in pairs if a * b < 1e7):
        ratio = float(n) / t
        if ratio < minimum[0] and sorted(str(n)) == sorted(str(t)):
            minimum = (ratio, n)

    print minimum[1]

if __name__ == "__main__": main()
