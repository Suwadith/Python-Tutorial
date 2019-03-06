temperature = 30

if temperature >= 30:
    print("It's a hot day")
elif temperature <= 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")


name = input("What's your name?")
char = len(name)

if char < 3:
    print('name must be at least 3 characters')
elif char > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good')
