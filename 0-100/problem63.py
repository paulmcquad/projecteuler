#https://github.com/AaronJiang/ProjectEuler/tree/master/py
#43
"""

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, 
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def isEqualLenghtPower(x):
	flag = False
	for i in range(1, 10): # cannot reach 10
		if i ** len(str(x)) == x:
			flag = True
			break

	return flag == True

# Upper length limit
def getMaxLength():
	maxLength = 8
	while True:
		if len(str(9 ** maxLength)) < maxLength:
			break
		maxLength += 1
	return maxLength

# Numbers generate by 1-9's power
def getPowerNumbers():
	maxLength = getMaxLength()
	powers = []
	for i in range(1, maxLength):
		for j in range(1, 10):
			powers.append(j ** i)
	return set(powers)		

def main():		
	count = 0
	powers = getPowerNumbers()
	for i in powers:
		if isEqualLenghtPower(i):
			count += 1
	print count

if __name__ == '__main__':
	main()		

