
import random
print("this is school admission system with some modification")
print ("*" * 35)
name = input("enter the name of student")
age = input("enter the age")
classes = input ("which class student want to take the admission to ?")
check = bool(input ("ready to pay 30 k ? True/False"))
if (check):
	rollnumber =random.randint(1,60)
	print(f"student named {name} took admission in {classes} and his rollnumber {rollnumber}")
else :
	print("sorry we cannot provide admission")