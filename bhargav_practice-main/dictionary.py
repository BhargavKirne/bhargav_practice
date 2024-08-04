#  dict  ==> {1:1, 2:2}, dict()
# characteristics
# key:value pair
# key should be immutable
# value mutable/immutable
# fetching order one
# key will not allow duplicates/ keys should be unique
# it will not follow index

empty_dict = {}
# Dictionary with Initial Values:

person = {
    "name": "bhargav",
    "age": 30,
    "city": "hyderabad"
}
print(person)

# Using the dict() Constructor:

person = dict(name="bhargav", age=30, city="hyderabad")

# Accessing Values
# Accessing a Value by Key:

name = person["name"]

# Using the get() Method:

age = person.get("age")
country = person.get("country", "INDIA")

# Modifying Dictionaries
# Adding or Updating a Key-Value Pair:

person["email"] = "bhargav@example.com"
person["age"] = 31

# Removing a Key-Value Pair:

removed_value = person.pop("age")
del person["city"]

# Clearing a Dictionary:

person.clear()  #

# Dictionary Methods
# keys() Method:

keys = person.keys()
# values() Method:

values = person.values()
# items() Method:

items = person.items()

# update() Method:

additional_info = {"country": "INDIA", "profession": "Engineer"}
person.update(additional_info)

# Looping Through Dictionaries
# Looping Through Keys:

for key in person.keys():
    print(key)

# Looping Through Values:

for value in person.values():
    print(value)

# Looping Through Key-Value Pairs:

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Comprehensions
# Creating a Dictionary with Comprehension:

squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# Filtering Items in a Dictionary Comprehension:

filtered_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(filtered_squares)
