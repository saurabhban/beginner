def gold_room():
	print("This room is full of gold. How much do you take?")
	choice = input("> ")
	if choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)

	else:
		print("you greedy bastard")
		exit(0)



def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = True
	while True:
		choice = input(">")
		if "honey" in choice:
			dead("The bear looks at you then slaps your face off.")
		elif "taunt" in choice and bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			gold_room()
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
    		 print("I got no idea what that means.")



def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	choice = input("> ")
	print(choice)
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)





def start():
	print("you are in dark room ")
	print("there is a door on left and right what you want to take")
	print("Which one do you take?")

	choice = input("> ")
	if (choice == "left"):
		bear_room()

	elif (choice == "right"):
		cthulhu_room()

	else:
		print("You stumble around the room until you starve.")



start()