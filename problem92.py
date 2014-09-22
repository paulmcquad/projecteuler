#http://blog.dreamshire.com/project-euler-92-solution/
from projecteuler import sos_digits

def unhappy(n):
    while n > 1 and n != 89 and n != 4:
        n = sos_digits(n)
    return n>1

L = 7    #  Limit is expressed as 10^L
Lc = 9**2 * L + 1    #  maximum sum of digits square for L digits (plus 1)
t = [0] * Lc
solutions = [0] * Lc
for i in range(10):
    solutions[i*i] = 1

for i in range(2, L+1):
    for j in range(Lc):
        t[j] = sum(solutions[j - k*k] for k in range(10) if k*k <= j)
    solutions = list(t)
   
print "Project Euler 92 Solution =", sum(solutions[i] for i in range(1, Lc) if unhappy(i))
