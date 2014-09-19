#Largest prime factor
#Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import prime

i = 1
while i < 600851475142:
      if 600851475143%i == 0:
         if prime.isprime(i):
            print i
      i+=1