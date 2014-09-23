#http://blog.dreamshire.com/project-euler-48-solution/
L = 1000    
d = 10    # last d digits of series
s = sum(pow(n, n, 10**d) for n in range(1, L+1))
 
print "Project Euler 48 Solution = %010d" % (s % 10**d)
