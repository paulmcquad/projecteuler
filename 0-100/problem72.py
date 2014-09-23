#https://raw.githubusercontent.com/AaronJiang/ProjectEuler/master/py/problem072.py
"""

Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in 
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 
3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper 
fractions for d <= 1,000,000?
"""

# Euler totient function phi(n):
# counts the number of positive integers less than or equal 
# to n that are relatively prime to n

# phi(p) = p -1, for prime number p
# phi(n) = n * (1-1/p1) * (1- 1/p2) *...*(1-1/pk)
#			p1,p2,..pk are prime factors of n

# this problem equals to: find the sum of phi(2), phi(3), ...phi(1000000)

from Helper import isPrime
limit = 1000001
totients = range(limit) # [0,1,2,..,1000000]

for i in range(2, limit): # for (i=2; i<limit; i++)
	if isPrime(i):
		totients[i] = i - 1;
		for j in range(2*i, limit, i):
			totients[j] *= (1.0 -  1.0 / i)

print sum(totients) - 1

