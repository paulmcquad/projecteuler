import math
import operator
#http://problematicsets.com/project-euler-110-find-an-efficient-algorithm-to-analyse-the-number-of-solutions-of-the-equation-1x-1y-1n/
#looking for least n where solutions exceed 4 million

# For a given number x squared, find the prime factorization of that number
# i.e. 10 squared is 100
# prime factorization is 2, 2, 5, 5
# or 2 squared times 5 squared
# combined factorizations for a to the b times c to the d
# is (b+1)*(d+1)
# in this case, it is 3*3, or 9
# (1,100), (2,50), (4,25), (5,20), (10, 10), (20,5) .....
# unique combinations is divided by 2 + 1, or 5 unique combinations


# let's investigate solutions with 14 distinct prime factors

f = [2,3,5,7,11,13,17,19,23,29,31,37,41.43,47]

# build a generator (thanks to Sans SS)

def genEx(limit):
    output = [1] * 14
    while output[13] < limit:
        i = 13
        while i > 0 and (output[i] == output[i-1]):
            output[i] = 1
            i -= 1
        output[i] += 2
        yield output

a = genEx(13)

import operator

def bigEnough(exps, threshold):
    expandedFactors = reduce(operator.mul, exps)
    if expandedFactors >= threshold:
        return True
    else:
        return False

def factorExpansion(f, exps):
    output = 1
    for i in range(len(f)):
        output *= math.pow(f[i], exps[i]-1)
    return output
        

answer = float("inf")
solution = []

for i in a:
    if bigEnough(i, 8000000):
        temp = factorExpansion(f, i)
        if temp < answer:
            answer = temp
            solution = i[:]
            print answer
            print solution
            print ""

# for the exponents in our solution list, subtract 1

temp = [x-1 for x in solution]

# the square root means we take each exponent and divide by 2

temp2 = [x/2 for x in temp]

print temp
print temp2

answer = 1
for i in range(14):
    answer *= int(math.pow(f[i], temp2[i]))

print answer
print type(answer)
