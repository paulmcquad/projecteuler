count = 0
n = 1
while count < 6:
    six_consequtive = True
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 6*a + 9*b + 20*c == n:
                    six_consequtive = False
    if six_consequtive:
        count += 1
    else:
        count = 0

    n += 1

print("Largest number of McNuggets that cannot be bought in exact quantity: %d." % (n - 5))
