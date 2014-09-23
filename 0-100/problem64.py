#http://www.progsoc.uts.edu.au/wiki/Euler_Solution_64
from math import floor

def cf(D):
    m = [0,]
    d = [1,]
    a = [floor(D**0.5),]

    for n in xrange(0,10000):
        # a is one of the digits in the period. (Now how can we identify a pattern in a?)
        # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html
        # It looks like we can find the END of the sequence when a[n] = 2*a[0]. 
        if a[n] == 2*a[0]:
            return len(a[0:n])
        m.append(int( (d[n]*a[n]) - m[n] ))
        d.append(int( (D - (m[n+1])**2)/d[n] ))
        a.append(int( floor((a[0]+m[n+1])/d[n+1]) ))

count = 0
for x in range (2,10001):
    if not (x**0.5 == int(x**0.5)):
        period = cf(x)
        if period & 1:
            count += 1
print count

