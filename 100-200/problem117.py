#Project Euler Problem 117: Linear recurrence
#http://blog.dreamshire.com/project-euler-117-solution/
ways, n = [1, 2, 4, 8], 50

while len(ways) < n:
    ways += [sum(ways[-4:])]

print "Space size =", n, "units"
print "Number of ways to fill:", ways[-1]
