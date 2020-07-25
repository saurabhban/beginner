from sys import argv

def printtwo (*args):
	value1,value2 = args
	print(f"this is function1 value passed are {value1} and {value2}")


def printone (num):
	print("this is the value passed",num)


def none():
	print("none printed")


def fileprint(data):
	print(data)

def findsearch(file1,search):
	with open(file1, 'r') as read_obj:
		for line in read_obj:
			line=line.lower()
			if search in line:
				print("true")
			else:
			    print("false")
	   
	   	

    
		 

printtwo("one","two")
printone(1)
none()

file1 = argv [1]
ptr = open(file1)
search = input("enter the string to search")
search=search.lower()
findsearch(file1,search)
