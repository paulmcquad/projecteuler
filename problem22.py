# This function takes a name / password and returns its text value 
def name_score ( name ): 
    score =  0 
    #Lecture one by one letter from the word 
    for i in name : 
        #The ord function takes a character parameter and returns its ascii code ascii 
		#The of A being 65, we subtract 64 to ascii code 
        # a letter to get its position in the alphabet 
        score += ord ( i )  -  64 
    return score

file = open ( "022_names.txt" ,  "r" ) 
#Lecture names the file and generate a list of names 
names = list ( eval ( file . read ())) 
file . close ()

names.sort()

result =  0

for i, name in enumerate(names):
    result += name_score(name)*(i+1)

print ( result )