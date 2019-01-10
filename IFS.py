#Once there is two or more numbers that are equal, it will return true and false if none are equal
def EqualTwice(a, b, c):
	a, b, c = int(a), int(b), int(c) #This will make sure the inputs are integers
	Output = False
	if (a == b or a == c or b == c): 
		Output = True
	return Output

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

print(a, b, c)
print(EqualTwice(a, b, c))