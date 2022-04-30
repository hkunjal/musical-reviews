
print(" ")
print(" ")
print("~Hello! Welcome to Musical Reviews!~")
print(" ")
while True:
    print("There are so many options you can choose!")
    print("Would you like to: get reccomandations; choose a specific musical; or look at my reviews")
    userAction = input (">")

    if userAction == "get reccomandations":
        
        print ("You picked get reccomandations!")
        print ("Do you like fiction, non fiction, or realistic non fiction?")
        genre = input (">")

        if genre == "fiction":
            print ("Nice! I only have one fiction musical for you. Maybe you should try Wicked?")
            print ("Would you like to choose another option?")

