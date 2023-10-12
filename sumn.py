#sum of n digit number until a single number
#optimized
n=int(input("enter the number"))
if n%9==0:
	print(9)
else:
	print(n%9)
