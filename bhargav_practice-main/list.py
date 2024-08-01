# characteristics ==>

# it stored index value
# slicing supports
# iterable
# mutable
# allows any data type
# allows duplicates


empty_list = []

# List with Initial Values:

fruits = ["apple", "banana", "cherry"]

# List with Mixed Data Types:

mixed_list = [1, "apple", 3.14, True]

# Accessing List Elements
# Indexing:

first_fruit = fruits[0]

# Negative Indexing:

last_fruit = fruits[-1]

# Slicing:

first_two_fruits = fruits[0:2]
all_but_first = fruits[1:]

# Modifying Lists
# Changing an Element:

fruits[1] = "blueberry"
print(fruits)

# Adding Elements:
# Appending to the End:

fruits.append("date")
print(fruits)

# Inserting at a Specific Position:

fruits.insert(1, "banana")
print(fruits)

# Removing Elements:
# Using remove():

fruits.remove("banana")
print(fruits)

# Using pop():

last_fruit1 = fruits.pop()
print(last_fruit1)
print(fruits)

# Using del Statement:

del fruits[1]
print(fruits)

# Using clear() Method:

fruits.clear()
print(fruits)

# Sorting:

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.sort()
print(numbers)

# Reversing:

numbers.reverse()
print(numbers)

# Finding Index of an Element:

index_of_four = numbers.index(4)
print(index_of_four)

# Counting Occurrences of an Element:

count_of_ones = numbers.count(1)
print(count_of_ones)

# Copying a List:

numbers_copy = numbers.copy()
print(numbers_copy)

# List Comprehensions
# Basic List Comprehension:

squares = [x ** 2 for x in range(10)]
print(squares)

# List Comprehension with Condition:

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Looping Through Lists
# Using for Loop:

for fruit in fruits:
    print(fruit)

# Using while Loop:

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Nested Lists
# Creating and Accessing Nested Lists:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_row = nested_list[0]  # Output: [1, 2, 3]
first_element = nested_list[0][0]

# Examples of Using Lists
# Removing Duplicates from a List:

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

# Finding Common Elements in Two Lists:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = [element for element in list1 if element in list2]
print(common_elements)

# Flattening a Nested List:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
