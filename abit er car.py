command = ""
started= False
while command.lower() != "quit" :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started...")
            speed= input("How much speed do you need?" )
            print("The car is running at ",speed, "KMPH")
    elif command == "stop":
        if not started:
            print("car is already stop")
            print("car is not running")
        else:
            started= False
            print("car stopped")
            print("car is running at 0 KMPH")
    elif command == "help":
        print("""
        start - to start the car
        stop -  to stop the car
        quit -  to quit the game """)
    elif command == "quit":
        break
    else: print("sorry!! i don't understand, Type help to get help")