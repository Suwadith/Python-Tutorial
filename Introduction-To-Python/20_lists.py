names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names)
print(names[0])
print(names[2])
print(names[-2])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[:3])
print(names)

names[0] == 'Jon'
print(names)


numbers = [1, 5, 8, 7, 4, 3]
largest = numbers[0]

for number in numbers:
    if number>largest:
        largest = number
print(largest)