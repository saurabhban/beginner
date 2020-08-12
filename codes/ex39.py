print("welcome to the world of sorting")
print("*" * 30)
strings = input("enter the array to sort")
strings  = strings.strip()
strings = strings.split(" ")
for i in range (0,len(strings)):
	strings[i] = int(strings[i])


print(strings)


print("doing bubble sorting ......")

for i in range (0,len(strings)):

	for j in range(0,len(strings)-i-1):
		if strings[j]>strings[j+1]:
			strings[j],strings[j+1]= strings[j+1],strings[j]



print(strings)
