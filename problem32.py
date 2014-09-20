#http://codereview.stackexchange.com/questions/47931/how-to-make-project-euler-32-in-python-faster

from timeit import default_timer as timer

start = timer()
products = set()
for a in range(12, 100):
    for b in range(102, 1000): # to get 9-digit: 2-digit * 3-digit
        product = a * b
        digits = list(str(a) + str(b) + str(product))
        digits = [int(x) for x in digits]
        if sorted(digits, key = int) == range(1, 10):
            products.add(product)

for a in range(1, 10):
    for b in range(1023, 10000): # other option is 1-digit * 4-digit
        product = a * b
        digits = list(str(a) + str(b) + str(product))
        digits = [int(x) for x in digits]
        if sorted(digits, key = int) == range(1, 10):
            products.add(product)

ans = sum(list(products))
elapsed_time = (timer() - start) * 1000 # s --> ms

print "Found %d in %r ms." % (ans, elapsed_time)
