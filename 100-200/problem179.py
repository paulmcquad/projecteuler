#Project Euler Problem 179
#http://blog.dreamshire.com/project-euler-179-solution/

L = 10**7

n = [0]*(L)
for i in range(2, L//2):
    for j in range(i*2, L, i):
        n[j] += 1

c = 0
for i in range(3, L):
    if n[i] == n[i - 1]: c += 1

print "Project Euler 179 Solution =", c
