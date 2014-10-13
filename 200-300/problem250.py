#http://blog.dreamshire.com/project-euler-250-solution/
#Project Euler Problem 250

m = 250
freq, t = [0]*m, [0]*m

for i in range(1,250251):
    freq[pow(i, i, m)] += 1

t[0] = 1
for i in range(m):
    for j in range(freq[i]):
        t = [(t[k] + t[(k-i)]) % 10**16 for k in range(m)]

print "Answer to PE250 =", t[0]-1

print freq
