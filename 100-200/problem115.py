#Project Euler Problem 115
#http://blog.dreamshire.com/project-euler-115-solution/
L, m, ways = 1000000, 50, [1]

while ways[-1] < L:
    ways += [sum(ways[:-m]) + ways[-1]]

print "Fixed block size:", m, "units"
print len(ways)-2, "minimum units to fill", L, "combinations."
