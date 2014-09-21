import sys
import math
import random
	 
def isprime(num):
    for j in range(2,int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True
