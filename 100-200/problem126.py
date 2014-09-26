#Project Euler Problem 126
#http://glisicv.wordpress.com/2013/01/07/cuboid-layers-p126/
from collections import defaultdict

def calculate_layer(x,y,z,L):   

    return 2*(2*(L-1)*(x+z)+2*(L-1)*(L+y-2)+x*y+x*z+y*z)

dict1 = defaultdict(int)

max_v = 20000

for L in range(1,100):

    for x in range(1,5000):

        if calculate_layer(x,x,x,L) > max_v:
            break

        for y in range(x,5000):

            if calculate_layer(x,y,y,L) > max_v:
                break

            for z in range(y,5000):

                if calculate_layer(x,y,z,L) > max_v:
                    break

                dict1[calculate_layer(x,y,z,L)] += 1

for x,y in dict1.iteritems():

    if y == 1000:

        print x
