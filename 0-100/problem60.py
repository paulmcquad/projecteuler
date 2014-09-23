#http://projecteuler.diandian.com/post/2013-04-25/40050564523
from Helper import isPrime
     
#check if two primes still prime after combination
def isPrimeOnCombination(a, b):
    return (isPrime(int(str(a)+str(b))) == True and \
    isPrime(int(str(b)+str(a))) == True)
     
# find primes under 100000
primes = []
for i in range(2, 10000):
    if isPrime(i):
        primes.append(i)
primes.remove(2)
primes.remove(5)
print 'found primes under 10000'    
     
# Pre calculate the list of numbers for each prime
# which remains prime after combination. And the number
# in list must 1. be higher than give one, 2. is prime
# 3. remain prime after combination
primesCanCombine = {}
for i in primes:
    primesCanCombine[i] = []
    for j in primes[primes.index(i)+1:]:
        if isPrimeOnCombination(i, j):
            primesCanCombine[i].append(j)
print 'finished the available combined list for each prime'
     
sums = 10**7
for i in primes:
    for j in primesCanCombine[i]:
            # k is in both primesCanCombines of i and j
            for k in set(primesCanCombine[i]) & set(primesCanCombine[j]):
                    for l in set(primesCanCombine[i]) & set(primesCanCombine[j])\
                    & set(primesCanCombine[k]):
                            for m in set(primesCanCombine[i]) & set(primesCanCombine[j])\
                            & set(primesCanCombine[k]) & set(primesCanCombine[l]) :
                                    sums_new = i + j + k + l + m
                                    if sums_new < sums:
                                        sums = sums_new
print "min sum is ", sums
