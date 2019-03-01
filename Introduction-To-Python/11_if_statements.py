is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
print()

price = 1000000
is_good_credit = True

if is_good_credit:
    down_payment = price * (10/100)
else:
    down_payment = price * (20/100)
print("Down payment: $" + str(round(down_payment)))
#print(f"Down payment: ${down_payment}")
