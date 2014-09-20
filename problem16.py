#http://pythonfiddle.com/euler-problem-fifth-teen-lattice-path/

sum = str(2**1000)

result = 0

for i in sum:
    result += int(i)

print(result)