#http://wiki.san-ss.com.ar/project-euler-problem-158
factorial = {0:1}
for i in range(1, 27):
    factorial[i] = factorial[i-1] * i
 
dp = {
    (0, 0, 0) : 0,
    (0, 0, 1) : 1
}
def get_num(*args):
    if args in dp:
        return dp[args]
 
    length, num_greater, count = args
    if count > 1:
        return 0
    result = sum(get_num(length-1, i, count + ((i < num_greater) and 1 or 0)) for i in range(length))
    dp[args] = result
    return result
 
p = lambda n: sum(get_num(n-1, i, 0) for i in range(n)) * (factorial[26] // (factorial[n] * factorial[26 - n]))
 
if __name__ == '__main__':
    max_pn, max_n = max((p(n), n) for n in range(2, 27))
    print("The result is:", max_pn, "found at n:", max_n)
