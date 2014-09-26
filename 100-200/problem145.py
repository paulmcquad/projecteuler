#Project Euler Problem 145
#http://blog.dreamshire.com/project-euler-145-solution/

L = 9    #Limit is expressed as 10^L
C = 0

for n in xrange(2, L+1):
    if n % 2 == 0: C += 20 * pow(30, n//2 - 1)
    elif n % 4 == 3: C += 100 * pow(500, n//4)

print  "Reversible numbers below 10 ^", L, '=', C
