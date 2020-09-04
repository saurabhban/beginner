

strings = input("enter the value in the strings")
strings = strings.strip()
print(strings)

for i in range (0,len(strings)):
	strings[i]= int(strings[i])

print("bubble sorting the strings of int")

even=[]
odd=[]

for i in range (0,len(strings)):

	for j in range(0,len(strings)-i-1):

		if strings[j+1] > strings[j]:

			strings[j],strings[j+1] = strings[j+1],strings[j]



print("sorted strings:",strings)

