
import random
print("this is school admission portal", end ='')
print("*" * 30)
print ("enter the name of the person >", end ='')
name = input ()
print ("enter the age of the person >", end= '')
age  = input ()
print ("enter the class he wants to take admission to >", end = '')
classes = input ()
print ("fees to be paid :30000")
rollnumber = random.randint(1,200)
print(f"student with name {name} took admission in class {classes} by paying fees 30k and rollnumber is {rollnumber}")
