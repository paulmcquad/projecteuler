#http://problematicsets.com/project-euler-66-investigating-a-diophantine-equation/comment-page-1/
#
#Project Euler 66

import math

# x2 - Ny2 = 1
# no solutions when D is square

#brahmagupta created chakravala method
# identity
# (a2 - Nb2)(c2 - Nd2) = (ac+Nbd)2 - N(ad+bc)2
# first compose triplets
# (x,y,k) with trivial triple (m, 1, m2-N)
# to get triplet( (am + Nb, a+bm, k(m2-N) )
# then scale down by k


def reduceTriplet(triplet, n):
    a = triplet[0]
    b = triplet[1]
    k = triplet[2]
    mStart = 1
    while True:
        if (a + b*mStart) % k == 0:
            break
        mStart += 1
##    print mStart
    m = mStart
    step1 = int(math.fabs(k))
    least = int(math.fabs(m*m - n))
    while True:
        mNew = m + step1
        if int(math.fabs(mNew * mNew - n )) > least:
            break
        else:
            m =  mNew
            least = int(math.fabs(m*m - n))
##    print m
    newA = (a*m + n*b)/ int(math.fabs(k))
    newB = (a + b*m) / int(math.fabs(k))
    newK = (m*m-n) / k
##    print newA, newB, newK
    return (newA, newB, newK)
    

def chakra(n):   #takes integer, n can't be a perfect square
    root = int(math.sqrt(n))
    if root * root == n:
        raise ValueError
    # find an arbitary triplet (a, b, k), where b is 1
    r1 = root
    r2 = root + 1
    diff1 = r1 * r1 - n
    diff2 = r2 * r2 - n
    if math.fabs(diff1) < math.fabs(diff2):
        a = r1
    else:
        a = r2
    b = 1
    k = a*a - n
    triplet = (a, b, k)
##    print triplet
    # now compose this first triplet with (m, 1, m2-N)
    # select m so that (a+bm)/k is an integer, and that minimizes (m2-N)/k
    if triplet[2] == 1:
        return triplet
    result = reduceTriplet(triplet, n)
    while result[2] != 1:
        result = reduceTriplet(result, n)
    return result

largest = 0
answer = 0
for i in range(2, 1001):
    root = int(math.sqrt(i))
    if root * root != i:
        temp = chakra(i)
        if temp[0] > largest:
            largest = temp[0]
            answer = i
            print largest, i

print "The answer is ", answer 
