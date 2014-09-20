#http://matthewhr.wordpress.com/2013/10/13/project-euler-fibonacci-numbers-and-problem-25/

#Import the math and time modules
import math, time
#The first two elements of the Fibonacci sequence are 0 and 1.
#We want to keep track of the index of the term with n.
F0 = 0; F1 = 1; n = 1
#The smallest 1000-digit number has logarithm in base 10 equal to 999 (i.e. 10**999).
#We want to see how long this algorithm will take.
start_time = time.time()
while math.log(F1,10) < 999:
    #Update the index
    n += 1
    #Compute the n^th Fibonacci number
    F2 = F0+F1
    F0 = F1
    F1 = F2
elapsed_time = time.time() - start_time
print n, elapsed_time
