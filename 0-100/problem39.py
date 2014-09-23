#http://pastebin.com/McU8rdFX

#If p is the perimeter of a right angle triangle with integral length sides,
#{a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p <= 1000, is the number of solutions maximised?

#Characteristics:
#a<=b<c
#c**2 = a**2 + b**2 (Pythagoras)
#smallest values a=3, b=4, c=5

#iterate over the maximum perimetr to get all the solutions and store in
#a dict where solution is the key and the perimeter is the value
maxP = 1000
solutions = {}
for a in range(3,maxP+1):
    for b in range(a,maxP+1):
        if a+b > maxP:
            break
        for c in range(b+1,maxP+1):
            if a+b+c > maxP:
                break
            if  c**2 == a**2 + b**2:
                solutions[(a,b,c)] = a+b+c
                
    
pList = solutions.values() #Generate a list of all values in solutions dict

print max(set(pList), key=pList.count) #Get the most frequent value in pList
