#Project Euler Problem 197
#http://blog.dreamshire.com/project-euler-197-solution/
def u(n):
    f = lambda x: int(2 ** (30.403243784 - x*x)) * 1e-9
    return -1 if n==0 else f(u(n-1))

i = 0
while abs(u(i) - u(i+2)) > 1e-10:
    i += 51

print "Project Euler 197 Solution =", u(i) + u(i+1)
