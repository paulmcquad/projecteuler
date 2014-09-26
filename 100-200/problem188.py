#Project Euler Problem 188
#http://blog.dreamshire.com/project-euler-188-solution/
def tetration(a, b, m):
    t0 = 1
    for i in xrange(b):
        t1 = pow(a, t0, m)
        if t0 == t1: break
        t0 = t1
    return t1
  
print "Project Euler 188 Solution = %08d" % tetration(1777, 1855, 10**8)
