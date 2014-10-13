#http://blog.dreamshire.com/project-euler-203-solution/
#Project Euler Problem 203

primes_sq = [x*x for x in [2, 3, 5, 7]]
rows = 51

def sqf(x):
    for p in primes_sq:
        if x % p == 0: return False  
    return True

#generate rows of Pascal's triangle
pt = [[1]]
for i in range(rows-1):
    pt += [map(sum, zip([0]+pt[-1], pt[-1]+[0]))]

#flatten 2D array, pt, and create a set of distinct values
dpt = set(sum(pt, []))

print "Project Euler 203 Solution =", sum(x for x in dpt if sqf(x))
