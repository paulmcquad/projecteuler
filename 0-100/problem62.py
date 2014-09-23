#https://github.com/AaronJiang/ProjectEuler/tree/master/py
#127035954683
"""

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from Helper import isPerm
import sys

# Get all cube numbers with desired length
def getCubesWith(length):
	start = int( (10 ** (length-1)) ** (1.0 / 3) )
	end = int( (int(''.join(['9'] * length))) ** (1.0 / 3) )
	return [i ** 3  for i in range(start, end + 1)]

length = 8
print 'calculate numbers in length: ',

while True:
	print length,
	cubes = getCubesWith(length)
	for i in cubes:
		perms = [i]
		for j in cubes[cubes.index(i)+1:]:
			if isPerm(i, j): perms.append(j)

		if len(perms) == 5:
			print perms
			sys.exit(0)

		# remove checked perm numbers
		for k in perms:
			cubes.remove(k)

	length += 1			
