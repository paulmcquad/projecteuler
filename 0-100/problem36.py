#http://protectedpenguin.com/2013/01/project-euler-problem-36-solution-double-base-palindromes-solution/

count = 0

for i in range(999999):
    if bin(i)[2:] == bin(i)[2:][::-1] and str(i) == str(i)[::-1]:
        count += i

print(count)


