import random


for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Josh']

leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        temp_list = []
        for i in range(2):
           temp_list.append(random.randint(1, 6))
        final_tuple = tuple(temp_list)
        return final_tuple 

    def roll_tutorial(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    

dice = Dice()
print(dice.roll())
print(dice.roll_tutorial())

