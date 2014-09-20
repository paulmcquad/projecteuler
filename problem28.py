from timeit import default_timer as timer
start = timer()

def spiral_diag_sum(n):
    if n < 1: return None
    elif n == 1: return 1
    elif n % 2 == 0: return None
    else:
        numbers = [1]
        while len(numbers) < (2*n - 1):
            increment = int(len(numbers) * 0.5 + 1.5)
            for p in range(4):
                numbers.append(numbers[-1] + increment)     
    return sum(numbers)

ans = spiral_diag_sum(1001)
elapsed_time = (timer() - start) * 1000 # s --> ms
print "Found %d in %r ms." % (ans, elapsed_time)
