print("enter the dark room with 2 doors do you want to go through door 1 or door 2 ")
options=input(">")
print(options)

if (options == "1"):
    print("welcome to first door , goooosh !!!!")
    print("*" * 30)
    print("what you want a do ?")
    print("1. eat a choco lava cake >")
    print("2 . eaten by polar beer >")
    inputs= input(">")
    if inputs == "1":
        print("you die ! cake was poisioned")
    elif inputs== "2":
        print("you are eaten by bear ! you die")

    else:
        print("you understand the trick ! you live :D")


elif (options == "2"):
    print("welcome to second door , goooosh !!!!")
    print("*" * 30)
    print("what you want a do ?")
    print("1. eat a pizaa >")
    print("2 . eat pasta >")
    inputs= input(">")
    if (inputs=='1'):
        print("you die ! pizaa was rotten")
    elif (inputs=='2'):
        print("pasta was 3 days old , all the best")
    else:
        print("you understand the trick ! you live :D")


else:
    print("you choose option not to play game ! you are saved")