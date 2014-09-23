#http://stackoverflow.com/questions/3360842/project-euler-problem-in-python-problem-53
from math import factorial

def ncr(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

i = 0
for x in range(1,101):
    for y in range(0,x):
        if(ncr(x,y) > 1000000):
            i+=1
print i
