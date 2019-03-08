numbers = [5, 2, 1, 7, 4]

numbers.append(20)
print(numbers)

numbers.insert(0, 21)
print(numbers)

numbers.remove(21)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5, 2, 1, 7, 4, 8]

numbers.pop()
print(numbers)

print(numbers.index(2))

# print(numbers.index(50)) // This will throw an error if the value is not in the list

print(50 in numbers)

numbers.append(4)
print(numbers)
print(numbers.count(4))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)

fresh_numbers = [2, 4, 3, 5, 3, 9, 7, 8, 4, 9]

# for number in fresh_numbers:
#     if fresh_numbers.count(number) > 1:
#         fresh_numbers.remove(number)
# print(fresh_numbers)

# .remove() removes only the first occurrence of a given value

uniques = []

for number in fresh_numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)