#http://blog.singhanuvrat.com/problems/project-euler-arranged-probability
'''
Created on Apr 5, 2013

@author: anuvrat
'''

def main():
    min_value = 1000000000000
    t = 21
    b = 15
    
    while t < min_value:
        b_temp = 3 * b + 2 * t - 2
        t_temp = 4 * b + 3 * t - 3
        
        b, t = b_temp, t_temp
    
    print(b)

main()
