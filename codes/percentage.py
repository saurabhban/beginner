print("lets enter value in list")
N = input ("enter the number of values to be entered in list")
N =int(N)
list1 = []
for i in range (0,N):
	cmd = int(input())
	list1.append(cmd)


print(list1)


list1 = tuple(list1)


print("value is",hash(list1))







