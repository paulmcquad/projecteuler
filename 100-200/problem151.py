#http://wiki.san-ss.com.ar/project-euler-problem-151
from decimal import *
 
d = {
    (5,) : Decimal(0)
}
 
def solve(curr_size):
    if curr_size in d:
        return d[curr_size]
 
    result = Decimal(0)
 
    if len(curr_size) == 1:
        result += Decimal(1)
 
    p = Decimal(1) / Decimal(len(curr_size))
    for i in curr_size:
        tmp_curr = list(curr_size)
        tmp_curr.remove(i)
        while (i < 5):
            tmp_curr.append(i + 1)
            i += 1
        tmp_curr = tuple(sorted(tmp_curr))
        result += p * solve(tmp_curr)
 
    d[curr_size] = result
    return result
 
if __name__ == '__main__':
    result = solve((2,3,4,5))
    getcontext().prec = 6
    result = +result
    print("The result is:", result)
