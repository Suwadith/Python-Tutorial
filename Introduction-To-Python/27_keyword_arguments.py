def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user(last_name="Henry", first_name="Josh") #keyword arguments - We'll be able to change the order as we wish etc.... 
# cal_cost(total=50, shipping=5, discount=0.1) with numerical values it's better to use keyword arguments as they'll improve readability
greet_user("Josh", last_name="Henry") #words
#greet_user(first_name="Henry", "Josh") won't work coz python prefers positional argument first then any number of keyword/positional arguments
print("End")