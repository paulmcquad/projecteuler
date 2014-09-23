#https://github.com/AaronJiang/ProjectEuler/tree/master/py
"""
Let p(n) represent the number of different calculatedNum in which 
n coins can be separated into piles. For example, five coins 
can separated into piles in exactly seven different calculatedNum, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# Partition theory
# http://en.wikipedia.org/wiki/Partition_%28number_theory%29
def p(n):
	if n <= 1: return 1
	if n in calculatedNum: return calculatedNum[n]
	
	result = 0
	k = 1
	while (n-k*(3*k-1)/2) >= 0:
		result += ( (-1)**(k-1) * p((n-k*(3*k-1)/2)) )
		if k > 0:
			k *= -1 
		else:
			k = (-1)*k + 1
	# only save the last 6 digits
	calculatedNum[n] = int(result % 1000000) 
	return calculatedNum[n]

def main():
	n = 5
	while True:
		if p(n) % 1000000 == 0:
			print n
			break
		n += 1

if __name__ == '__main__':
	# store calculated p(n)
	global calculatedNum
	calculatedNum = {}
	main()		



