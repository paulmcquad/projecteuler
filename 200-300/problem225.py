#http://blog.dreamshire.com/project-euler-225-solution/
#Project Euler Problem 225
def prob225(n):
    c, i = 0, 27
    while c < n:
        t1, t2, t3 = 1, 1, 3
        while t3>0 and t1 * t2 * t3 != 1:
            t1, t2, t3 = t2, t3, (t1 + t2 + t3) % i
        if t3>0: c+=1
        i+=2
    return i-2
print 'Project Euler 225 Solution = ', prob225(124)
