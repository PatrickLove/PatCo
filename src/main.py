def isDivisibleSeven(n): # Based on Test  here: 2https://www.math.hmc.edu/funfacts/ffiles/10005.5.shtml
	s = str(n) # Get digits as char array (string)
	s = s[1:] if s[0]=='-' else s # Remove negative sign if present
	if(len(s)<=1): # Base case single digit check
		return s=='0' or s=='7'
	else: # Split and subtract recursively
		return isDivisibleSeven(int(s[:-1])-2*int(s[-1]))

def isValidNumber(n):
	# Check if multiple of 5 by looking at last digit
	isMultFive = str(n)[-1]=='5' or str(n)[-1]=='0'
	# Call seven divisibility algorithm
	isDivSeven = isDivisibleSeven(n)
	# Compute validity as per requirements
	return isDivSeven and not isMultFive

if __name__ == '__main__':
	print("Hello World")