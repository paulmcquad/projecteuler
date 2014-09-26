#Project Euler Problem 174
#http://blog.dreamshire.com/project-euler-174-solution/
L = 1000000
N = [0]*(L+1)

for h in range(1, L//4):
    nt = h*4 + 4
    sumx = nt
    while sumx <= L:
        N[sumx] += 1
        nt = nt + 8
        sumx += nt

print "Project Euler 174 Solution =", sum(1 <= n <= 10 for n in N)
