print("*********sets play ground*********")
print("enter the numbers 1. array list 2 sets numbers")
m = input("array max lenght >")
n = input ("number of elemets in sets")
m = int(m)
n = int(n)
print( f"enter the elements in array {m}")
arrayvalues = []
for i in range(0,m):
	ele = int(input("enter element"))
	arrayvalues.append(ele)


set1 = []
set2 = []

for i in range(0,n):
	ele = int(input("enter the element in set1 >"))
	set1.append(ele)



for i in range(0,n):
	ele = int(input("enter the element in set2 >"))
	set2.append(ele)



s = set(arrayvalues)
t = set(set1)
y = set(set2)

print(s)
print(t)
print(y)

z = s.intersection(t)
x = s.intersection(y)
print(z)
print(x)
print("happiness is >")
print(len(z)-len(x))