#Next Pandigital prime sets Problem 118
#http://euler.clarinetcat.com/Problems/118
#44680
from itertools import *

def isprime(n):
	if n == 2:
		return True
	elif n < 2 or n%2 == 0:
		return False
	else:
		for i in range(3, int(n**0.5 + 1), 2):
			if n%i == 0: return False
		return True

answers = set()

for p in combinations_with_replacement(range(0,10), 9):
	if sum(list(p)) == 9:
		answers.add(tuple(sorted(list(p))))

divisions = []
	
for group in answers:
	new_group = []
	for digit in group:
		if digit != 0:
			new_group.append(digit)
	divisions.append(new_group)
	
answers = set()
prev = 0

for p in permutations(range(1, 10)):
	if p[2] != prev:
		print p
		prev = p[2]
	for div in divisions:
		this = []
		this_p = list(p)
		for comma in div:
			this.append(int(''.join(map(str, this_p[:comma]))))
			del this_p[:comma]
		hum = True
		for number in this:
			if isprime(number) == False:
				hum = False
				break
		if hum == True:
			answers.add(tuple(sorted(this)))

print len(answers)
