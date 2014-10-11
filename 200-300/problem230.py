#http://wiki.san-ss.com.ar/project-euler-problem-230
calc_offset = lambda x: (127+19*x)*(7**x)
 
def solve(n, a, b):
    len_str = len(a)
    ab = a + b
    i1 = 1
    i2 = 2
    while i2 * len_str < n:
        t = i2
        i2 += i1
        i1 = t
    while i2 > 2:
        t = i1
        i1 = i2 - i1
        i2 = t
        if n <= i1 * len_str:
            n += i2 * len_str
        n -= i1 * len_str
    return ab[n-1]
 
a = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
b = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
 
if __name__ == '__main__':
    result = []
    for i in range(18):
        result.insert(0, solve(calc_offset(i), a, b))
    print("The result is:", ''.join(result))

