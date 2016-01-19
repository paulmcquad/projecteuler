#Largest palindrome product
#Problem 4
#
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
import Helper

if __name__ == "__main__":
   print('{} and {} => {}'.format(*max((i,j,i*j)
              for i in range(1000, 900, -1)
                  for j in range (1000, 900, -1)
                      if Helper.isPalindrome(i*j))))