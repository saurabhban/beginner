

strings = input("enter the value in the strings")
strings = strings.strip()
strings = strings.split(" ")
for i in range (0,len(strings)):
	strings[i]= int(strings[i])

print("bubble sorting the strings of int")

even=[]
odd=[]

for i in range (0,len(strings)):

	for j in range(0,len(strings)-i-1):

		if strings[j] > strings[j+1]:

			strings[j],strings[j+1] = strings[j+1],strings[j]



print("sorted strings:",strings)

for i in range(0,len(strings)):
	
	if (strings[i] % 2 == 0):
		even.append(strings[i])

	else:
		odd.append(strings[i])



print("sorted strings are:",even)
print("odd strings are :",odd)

