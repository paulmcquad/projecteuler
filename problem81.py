#https://github.com/AaronJiang/ProjectEuler/tree/master/py
"""
http://projecteuler.net/problem=81
In the 5 by 5 matrix below, the minimal path sum 
from the top left to the bottom right, by only 
moving to the right and down, is indicated in 
bold red and is equal to 2427.

131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	
Find the minimal path sum, in matrix.txt (right 
	click and 'Save Link/Target As...'), a 31K text 
file containing a 80 by 80 matrix, from the top left 
to the bottom right by only moving right and down.
"""
from projecteuler import open_data_file

f = open_data_file("pb82matrix.txt")
matrix = []
for line in f:
	numbers = [int(n) for n in line.split(',')]
	matrix.append(numbers)
num = len(matrix) - 1

for i in range(num+1):
	for j in range(num+1):
		if (i == 0 and j == 0): continue
		if (j == 0): minx = matrix[i-1][j]
		elif (i == 0): minx = matrix[i][j-1]
		else: minx = min(matrix[i-1][j], matrix[i][j-1])
		matrix[i][j] += minx

print matrix[num][num]
