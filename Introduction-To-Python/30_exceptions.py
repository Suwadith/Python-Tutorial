try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('INVALID VALUE')
except ZeroDivisionError:
    print("Age can't be 0")