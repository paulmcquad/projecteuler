from math import *
from decimal import Decimal
from operator import itemgetter

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
#        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def fibonacci(n):
	if n<=2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def isPrime(n):
	for i in xrange(2, int(sqrt(n))+1):
		if n%i == 0:
			return False
	if n == 1 : return False		
	return True

def isPalindrome(n):
	return str(n)==str(n)[::-1]	

def reverseInt(n):
	return int(str(n)[::-1])

def gcd(a, b):
    """Return greatest common divisor."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b / gcd(a, b)
    
def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def isRelativePrime(a, b):
	return gcd(a, b) == 1
	
def factors(n):
	res = []
	limit = int(sqrt(n))+1
	for i in range(1, limit):
		if n%i == 0:
			res.append(i)
			res.append(n/i)
	return res		

def primeFactors(n):
	res = []
	limit = int(sqrt(n))+1
	for i in range(1, limit):
		if n%i == 0:
			if isPrime(i) : res.append(i)
			if isPrime(n/i) : res.append(n/i)
	return set(res)

def CollatzChain(n):
	chain = []
	while True:
		
		chain.append(n)
		if n == 1:
			break

		if (n%2 == 0):
			n = n/2
		else:
			n = 3*n + 1	
	return len(chain)		

def properFactors(n):
	factors = []
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			factors.append(i)
			if n/i != i and i !=1 :
				factors.append(n/i)
	return factors		
	
def charToValue(charest, charcase):
	if charcase == 'UPPERCASE':
		return ord(charest) - 64
	elif charcase == 'LOWCASE':
		return ord(charest) - 96		

def isTruncatablePrime(n):
	number = str(n)
	length = len(number)
	flag = True
	for i in range(length):
		if (not isPrime(int(number[i:]))) or\
		(not isPrime(int(number[:length-i]))):
			flag = False
			break 

	return flag

def isConcatenated(n):
	for i in range(1,10):
		if n.count(str(i)) != 1:
			return False
	return True		

def isPandigital(n, s=9): 
	n=str(n);
	return len(n)==s and not '1234567890'[:s].strip(n)

def isSquare(n):
	# n = Decimal(n).sqrt() # use decimal to avoid precision lost
	n = sqrt(n) # use decimal to avoid precision lost
	return int(n) == n

def isPentagonal(x):
	n = (1 + sqrt(1+24*x))/6
	return n == int(n)

def isTriangle(x):
	n = (-1 + sqrt(1+8*x))/2
	return n == int(n)

def isHexagonal(x):
	n = (1 + sqrt(1+8*x))/4
	return n == int(n)	

def isHeptagonal(x):
	n = (3 + sqrt(9+40*x))/10
	return n == int(n)	

def isOctagonal(x):
	n = (1 + sqrt(1+3*x))/3
	return n == int(n)	

def isPerm(a,b): 
	return sorted(str(a)) == sorted(str(b))	

def combinator(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))

def sortedDict(d):
	return sorted(d.iteritems(), key=itemgetter(1))

# swap the ith and jth value in a string
def swap(c, i, j):
	c = list(c)
	c[i], c[j] = c[j], c[i]
	return ''.join(c)
