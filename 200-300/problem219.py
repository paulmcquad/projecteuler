#http://blog.dreamshire.com/project-euler-219-solution/
#Project Euler Problem 219

L = 10**9
S = [1, 0, 0, 0, L-1]

a = 0 
while S[-1] > 0:  
  S = [S[1]+S[0], S[2], S[3], S[0], S[4]-S[0]]
  a += 1
 
print "Cost =", sum((a+i)*S[i] for i in range(5))
