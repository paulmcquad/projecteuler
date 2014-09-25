#Project Euler Problem 124
#http://blog.dreamshire.com/project-euler-124-solution/
L, k = 100000+1, 10000

E = [[1,_] for _ in range(L)]

for i in range(2, L):
    if E[i][0] == 1:
        for j in range(i, L, i):
           E[j][0] *= i

print "kth element in sorted list of radicals", sorted(E)[k][1]
