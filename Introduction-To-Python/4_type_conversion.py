year_of_birth = input('Birth year: ')
print(type(year_of_birth))
age = 2019 - int(year_of_birth)
print(type(age))
print(age)

weight_in_pounds = input('Please input your weight in pounds')
weight_in_kilos = int(weight_in_pounds) * 0.45
print(str(weight_in_kilos) + " kg")
print(format(weight_in_kilos) + " kg")