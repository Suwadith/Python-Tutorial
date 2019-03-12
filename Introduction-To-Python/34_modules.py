import converters
from converters import lbs_to_kg
import utils

print(converters.kg_to_lbs(56))
print(lbs_to_kg(56))

numbers = [10, 20, 5, 50, 7, 60, 55, 56]

print(utils.find_max(numbers))
print(max(numbers)) #inbuilt function 