#https://github.com/AaronJiang/ProjectEuler/tree/master/py
"""

A common security method used for online banking is to ask the user 
for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 
3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret 
passcode of unknown length.
"""
from Helper import swap

"""
I've made two restrictions after analysing the txt file
1. no duplicate digits in a single passcode, like '221' or '133' wont exist
2. no anti order between passcodes, if '123' exists, '132' wont exist, 
	if '321' exists, '231' wont exist for '3' and '2' anti orders in two passcodes, 
"""	

def readLogincode(filename):
	f = open(filename, 'r')
	logincode = f.read().split('\n')
	logincode = logincode[:-1]
	return logincode

# Prepare available digits for passcode from keylog.txt
def getAvailableDigits(logincode):
	availDigits = '';
	for code in logincode:
		for digit in code:
			if digit not in availDigits:
				availDigits += digit
	return availDigits

# sort passcode
def main():
	logincode = readLogincode('data/keylog.txt')
	passcode = getAvailableDigits(logincode)
	codelength = 3
	for code in logincode:
		for i in range(codelength-1):
			for j in range(i+1, codelength):
				passcode_i = passcode.index(code[i]) 
				passcode_j = passcode.index(code[j]) 
				if passcode_i > passcode_j:
					passcode = swap(passcode, passcode_i, passcode_j)
	print passcode

if __name__ == '__main__':
	main()
