
def add (a,b):
	print(f"this is what adding {a} + {b} looks like:")
	print(a+b)
	return a+b


def substract(a,b):
	print(f"this is what substracting {a}-{b} looks like:")
	print(a-b)
	return a-b 


def multiplication(a,b):
	print(f"this is what multiplying {a}*{b} looks like:")
	print(a*b)
	return a*b 

def divison(a,b):
	print(f"this is what division {a}/{b} looks like:")
	print(a/b)
	return a/b 

print("calculator at basic level (-|-)")
print("*"*20)
a = int(input("enter the value of a"))

b = int(input("enter the value of b"))
height= add (a,b)
age = substract(a,b)
weight =multiplication (a,b)
coolness = divison(a,b)
coolness = int(coolness)


print(f"height {height} : weight {weight} : age {age}: coolness {coolness}")
what =add (height,substract(age,multiplication(weight,divison(age,b))))
print("what ??? is it possible ? :",what)
