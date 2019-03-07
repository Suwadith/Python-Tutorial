command = ""
car_is_started = False

while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop -to stop the car
quit - to exit
        ''')
    elif command == "start":
        if car_is_started:
            print("car is already started...")
        else:
            car_is_started = True
            print("car started...")
    elif command == "stop":
        if not car_is_started:
            print("car has already been stopped...")
        else:
            car_is_started = False 
            print("car stopped...")
    elif command == "quit":
        break
    else:
        print("I don't understand...")
        