#Project Euler Problem 173
#http://blog.dreamshire.com/project-euler-173-solution/
from math import sqrt

tiles = 1000000 // 4
L = int(sqrt(tiles))

print "Different square laminae:", sum(tiles//i - i for i in range(1, L+1))
