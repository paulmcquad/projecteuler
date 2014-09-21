#https://raw.githubusercontent.com/AaronJiang/ProjectEuler/master/py/problem071.py
"""

Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in 
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in 
ascending order of size, find the numerator of the fraction immediately 
to the left of 3/7.
"""
# from Helper import gcd

# upper = 3.0 / 7
# lower = 2.0 / 5
# target = (3.0/7, '3/7')
# result = ()

# for d in range(8, 1000001):
# 	# lower< n/d < 3/7
# 	fractions = [target]
# 	upper_n = int(d * upper) + 1
# 	lower_n = int(d * lower)
# 	for n in range(lower_n, upper_n):
# 		if gcd(d, n) == 1:
# 			fractions.append((float(n)/d, str(n)+'/'+str(d)))
# 	if len(fractions) > 1:
# 		fractions.sort()
# 		idx = fractions.index(target)
# 		if fractions[idx-1][0] > lower: 
# 			lower = fractions[idx-1][0]
# 			result = fractions[idx-1]

# print result

# only need to check n = (d*3/7)
from Helper import gcd
upper = 0
result = 0

for d in range(8, 1000001):
	n = int(d * 3.0/7)
	if gcd(d, n) == 1:
		temp = float(n) / d
		if temp > upper:
			upper = temp
			result = n
print result
