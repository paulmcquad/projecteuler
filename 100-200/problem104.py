#http://blog.dreamshire.com/project-euler-104-solution/
from projecteuler import is_pandigital

def top_digits(n):
     t = n * 0.20898764024997873 + (-0.3494850021680094)
     t = int((pow(10, t - int(t) + 8)))
     return t

fk, f0, f1 = 2, 1, 1
while not is_pandigital(f1) or not is_pandigital(top_digits(fk)):
    f0, f1 = f1, (f1+f0) % 10**9
    fk += 1
print "Project Euler 104 Solution =", fk
