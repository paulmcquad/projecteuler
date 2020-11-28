
#Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
#It can be verified that 714285=5×142857.
#This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.
# Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have this property.



import sys
    
def main():
    sum = 0
    for k in range(1, 100):
        for d in range(1, 10):
            for y in range(1, 10):
                x, r = divmod((10**k - d)*y, 10*d - 1)
                if r != 0 or x < 10**(k-1):
                    continue
                sum += 10*x + y
    print(sum % 10**5)    
    
if __name__ == '__main__':
    sys.exit(main())
