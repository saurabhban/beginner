list1 = "my name is saurabh and i am still a noodler in programming"

list1 = list1.split(" ")
#print(list1)


print("wait there are few more stuffs")
list2 = "saurabh has high temper problem as well"
list2 =list2.split(" ")

list4 =[]

#print (list2)


#def contatination():
#	list3 = list1 + list2
#	print(list3)


def func(num):

	for i in range(0,num):
		ack = list2.pop()
		list4.append(ack)

	print(list4)


# contatination()
num = int(input("enter how many number your would like to add to the list"))
func(num)



