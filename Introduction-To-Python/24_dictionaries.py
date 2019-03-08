# Used to store information in key, value pairs
# Keys have to be unique

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
# print(customer["dob"]) Throws error and also it's case sensitive 
# print(customer.get("dob")) Doesn't throw an error. Instead returns 'None'
print(customer.get("dob", "Jan 1 1980")) # You can manually set a default value instead returning 'None'
customer["name"] = "Jack Smith" # can be modified
print(customer["name"])

customer["dob"] = "Jan 1 1980"
print(customer["dob"])

print(customer)

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone: ")

output = ""

for digit in phone:
    output += numbers.get(digit, "!") + " " # "!" - incase if the input is not in the dictionary (E.g :- 5)
print(output)

