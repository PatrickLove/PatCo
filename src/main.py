def isDivisibleSeven(n):
	s = str(n)
	s = s[1:] if s[0]=='-' else s
	if(len(s)<=1):
		return s=='0' or s=='7'
	else:
		return isDivisibleSeven(int(s[:-1])-2*int(s[-1]))

def isValidNumber(n):
	return str(n)[-1]!='5' and str(n)[-1]!='0' and isDivisibleSeven(n)

if __name__ == '__main__':
	print("Hello World")
	works = True;
	for i in range(10000):
		if (i%5!=0 and i%7==0) != isValidNumber(i):
			works = False
			print(i)
	print(works)