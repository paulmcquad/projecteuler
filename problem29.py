
#http://www.s-anand.net/euler.html
'''
How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100
'''
terms = {}
count = 0
for a in xrange(2,101):
     for b in xrange(2,101):
        c = pow(a,b)
        if not terms.get(c, 0):
            terms[c] = 1
	    count += 1
print count