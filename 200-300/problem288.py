#http://code.jasonbhill.com/python/project-euler-problem-288/
import time
 
"""
Compute and return a list of elements in the sequence T_i
"""
def T(p,q):
    S = [290797]
    for i in range(q):
        S.append(S[i]**2 % 50515093)
    T = [(i % p) for i in S]
    return T
 
"""
How many factors of p does N! have modulo mod?
"""
def num_p_in_factorial(p,N,mod=None):
    quo = N//p
    num = quo
    while quo >= p:
        quo //= p; num += quo
        if mod is not None and num > mod: num = num % mod
    return num
 
def Nfac(p,q,n):
    # form the sequence S
    Tseq = T(p,q)
    iter = q
    num_factors = 0
    num_factors_cached = [None] * p
    while iter >= 0:
        t = Tseq[iter]
        if t == 0:
            iter -= 1
            continue
        elif iter >= n:
            if num_factors_cached[t] is None:
                num_factors_cached[t] = num_p_in_factorial(p,t*p**n)
            num_factors += num_factors_cached[t]
        else: num_factors += num_p_in_factorial(p,Tseq[iter]*p**iter)
        iter -= 1
    if num_factors >= p**n: num_factors = num_factors % p**n
    return num_factors
 
start = time.time()
#N = Nfac(3,10000,20)
N = Nfac(61,10**7,10)
 
elapsed = (time.time() - start)
print "found %s in %s seconds" % (N,elapsed)
