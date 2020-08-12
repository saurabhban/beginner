elements =[]
list1 = ['mango','oranges','graphs','clouds']

def main():
	inputs =input("enter the value you want to enter")
	elements.append(inputs)
	print("value added to list")
	exit(0)



def printit():
	for lists in list1:
		print(lists)

	
	for name in elements:
  		print(name)
		
    



boolern = True

while True:

	strings =input("want to print the list or enter the value in list")

	if "enter" in strings:
		main()
		boolern = False
		

	elif "print" in strings:
		printit()
		boolern = False

	else:
		print("i donot know what you mean !")
    	
    


