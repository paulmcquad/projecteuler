#http://d.hatena.ne.jp/inamori/20120426/p1
from itertools import *
from math import sqrt
import time

def is_square(n):
    m = int(sqrt(n))
    return m * m == n

def div_pow(n, d):
    e = 0
    while n % d == 0:
        n /= d
        e += 1
    return e, n

def make_primes(N):
    a = [ True ] * (N + 1)
    for p in takewhile(lambda p: p * p <= N, (n for n in count(2) if a[n])):
        for n in xrange(p * p, N + 1, p):
            a[n] = False
    return [ n for n in xrange(2, N + 1) if a[n] ]

def gen_factorized():
    L = 10 ** 5
    primes = make_primes(L)
    f = [ (), () ]
    yield ()
    for offs in count(2, L):
        a = range(offs, offs + L)
        for p in takewhile(lambda p: p * p < offs + L, primes):
            for n in xrange((offs + p - 1) / p * p, offs + L, p):
                if a[n-offs] + offs != n:
                    a[n-offs] = p
        
        for n in xrange(offs, offs + L):
            p = a[n-offs]
            if n == p:
                fs = ((p, 1),)
            else:
                e, m = div_pow(n, p)
                fs = ((p, e),) + f[m]
            f.append(fs)
            yield fs

def value_f(fs):
    return reduce(lambda x, (p, e): x * p ** e, fs, 1)

def get_square(fs):
    return value_f((p, e / 2) for p, e in fs if e >= 2)

def progressives(N):
    for fs, r in izip(gen_factorized(),
                        takewhile(lambda r: r * r < N, count(1))):
        m = get_square(fs)
        a = r * r / m ** 3
        for n in takewhile(lambda n: n < N,
                            (r + a * k ** 3 for k in count(m + 1))):
            yield n

t0 = time.clock()
N = 10 ** 12
print sum(ifilter(is_square, progressives(N)))
print time.clock() - t0
