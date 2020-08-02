
from sys import argv
import random

def remove(string):
	return " ".join(string.split())



print ("School Admission System")
print("*"* 20)
database = argv[1]
print(database)
ptr = open(database, '+a')
print(ptr.read())
name = input("enter your name>")
age = int(input ("enter your age 4-16 years >"))
if (age > 16 or age < 4):
	print("cannot give the admission")
	exit(0)
gender = input ("enter the gender M/W/T")
final=remove(gender)
final =final.lower()
if (final != "m"):
	print("cannot give the admission")
	exit(0)
classes = input ("enter the class>")
payroll = input ("willing to pay 30 k ? True:False")
payroll = remove(payroll)
payroll = payroll.lower()
print(payroll)
if (payroll == "true"):
	rollnumber = str(random.randint(1,100))
	print(f"name of student {name} took admission in class {classes} and rollnumber is {rollnumber}")
	ptr.write("\n")
	ptr.write(name)
	ptr.write(" ")
	ptr.write(classes)
	ptr.write(" ")
	ptr.write(rollnumber)








