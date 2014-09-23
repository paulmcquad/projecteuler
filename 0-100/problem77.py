#https://github.com/yarmash/projecteuler/master/077/problem77.py
#!/usr/bin/python

"""Problem 77: Prime summations"""

from projecteuler import prime_sieve_lazy
from itertools import count

def main():
    nways = 5000

    for num in count(10):
        ways = [0]*(num+1)
        ways[0] = 1

        for p in prime_sieve_lazy():
            if p > num:
                break

            for i in range(p, num+1):
                ways[i] += ways[i-p]

        if ways[num] > nways:
            return num


if __name__ == "__main__":
    print(main())
