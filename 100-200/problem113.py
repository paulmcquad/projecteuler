#http://blog.dreamshire.com/project-euler-113-solution/
from projecteuler import binomial

n = 100
print "Project Euler 113 Solution =", binomial(n+10, 10) + binomial(n+9, 9) - 10*n - 2
