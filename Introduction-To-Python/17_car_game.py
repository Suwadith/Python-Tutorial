command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''
        start - to start the car
        stop -to stop the car
        quit - to exit
        ''')
    elif command == "start":
        print("car started...")
    elif command == "stop":
        print("car stopped...")
    elif command == "quit":
        break
    else:
        print("I don't understand...")
        