def appending(elements,numbers):
	i =0
	while (i<numbers):
		i=i+1
		print(f"adding {i} into list")
		elements.append(i)

		



numbers = int(input ("enter the numbers you would like to add "))
elements = []
print("calling function")
appending(elements,numbers)
print(f"value of elements {elements}")

