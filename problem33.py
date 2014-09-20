#http://codereview.stackexchange.com/questions/48137/project-euler-problem-33-digit-canceling-fractions

from timeit import default_timer as timer

start = timer()
fractions_that_work = []

def a_common_element(list_a, list_b):
    count = 0
    common = 0
    for m in list_a:
        for n in list_b:
            if m == n:
                count += 1
                common = m
    if count == 1:
        return common
    return False

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100): # denom must be > num
        n_digits = sorted([int(x) for x in str(numerator)])
        d_digits = sorted([int(x) for x in str(denominator)])
        common = a_common_element(n_digits, d_digits)
        if common:
            n_digits.remove(common)
            d_digits.remove(common)
            n_rem = n_digits[0]
            d_rem = d_digits[0]
            if 0 not in n_digits and 0 not in d_digits:
                if float(numerator) / denominator == float(n_rem) / d_rem:
                    fractions_that_work.append([numerator, denominator])        
product_of_fractions = [1, 1]
for frac in fractions_that_work:
    product_of_fractions[0] *= frac[0]
    product_of_fractions[1] *= frac[1]

start = timer()
ans = product_of_fractions[1] / product_of_fractions[0]
elapsed_time = (timer() - start) * 1000 # s --> ms

print "Found %d in %r ms." % (ans, elapsed_time)
