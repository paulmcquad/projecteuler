#http://users.softlab.ntua.gr/~ttsiod/euler31.html

#!/usr/bin/env python

# the 8 coins correspond to 8 columns
coins = [1, 2, 5, 10, 20, 50, 100, 200]

TARGET=200

matrix = {}
for y in xrange(0, TARGET+1):
    # There is only one way to form a target sum N
    # via 1-cent coins: use N 1-cents!
    matrix[y, 0] = 1  # equivalent to matrix[(y,0)]=1

for y in xrange(0, TARGET+1):
    print y, ":", 1,
    for x in xrange(1, len(coins)):
        matrix[y, x] = 0
        # Is the target big enough to accomodate coins[x]?
        if y>=coins[x]:
            # If yes, then the number of ways to form
            # the target sum are obtained via:
            #
            # (a) the number of ways to form this target
            #     using ONLY coins less than column x
            #     i.e. matrix[y][x-1]
            matrix[y, x] += matrix[y, x-1]
            # plus
            # (b) the number of ways to form this target
            #     when USING the coin of column x
            #     which means for a remainder of y-coins[x]
            #     i.e. matrix[y-coins[x]][x]
            matrix[y, x] += matrix[y-coins[x], x]
        else:
            # if the target is not big enough to allow
            # usage of the coin in column x,
            # then just copy the number of ways from the
            # column to the left (i.e. with smaller coins)
            matrix[y, x] = matrix[y, x-1]
        print matrix[y, x],
    print


