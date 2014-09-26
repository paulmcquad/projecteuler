#Even Fibonacci numbers
#Problem 2
#
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
import fibo

sum = 0
a = fibo.fib2(4000000)
for i in a:
    if i%2 == 0:
       sum += i
print sum