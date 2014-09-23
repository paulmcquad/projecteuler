#http://blog.singhanuvrat.com/problems/project-euler-greatest-exponent-value
'''
Created on Oct 23, 2012

@author: anuvrat
'''
from projecteuler import open_data_file
import numpy

max_digits = max_line = line_idx = 0
for line in ( line.rstrip( '\n' ) for line in open_data_file( 'pb99baseexp.txt' ) ):
    base, exponent = map( int, line.split( ',' ) )
    digits = exponent * numpy.log10( base )
    if digits > max_digits :
        max_digits = digits
        max_line = line_idx
    line_idx += 1

print max_line + 1

