states = {
	
'Rajasthan1' : 'jaipur',
'Delhi' : 'Union capital hence city',
'Andra pradesh' : 'Vizag',
'Telangana' : 'Hyderabad',



}


print("lets play the game")
print("*"* 30)



d = {}

n = int(input("enter how many vlues you want to add in dict"))




for i in range (0,n):

	strings = input()
	strings = strings.split(" ")
	d[i]= strings



print(d)


print(d[1])




for i in states:
	if i == 'Rajasthan':
		print(f"Welcome to pink city {states[i]}")
		exit(0)
         
	else:
		print("not allowed , state is close")







