#http://pastebin.com/g80iLQ2E

#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

digit = '.'
i = 1

#Create a string one million digits long by concatenating the counting numbers starting from 1.
while len(digit)<= 1000000:
    digit += str(i)
    i += 1

#multiply together the single digits at the positions specified above.
j = 1
count = 1
for k in range(7):
    count *= int(digit[j])
    j *= 10
print count
