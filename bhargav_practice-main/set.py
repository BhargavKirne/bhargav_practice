# set - {}, set()
# Char:
# it will not store index
# it will not support slicing
# allows diff data types
# mutable
# not allow duplicates

empty_set = set()

# Creating a Set with Elements:

s = {1, 2, 3, 4}

# Creating a Set from a List:

my_list = [1, 2, 2, 3, 4, 4, 5]
s1 = set(my_list)
print(s1)

# Basic Operations
# Adding Elements:

s2 = {1, 2, 3}
s2.add(4)
print(s2)

# Removing Elements:

s3 = {1, 2, 3, 4}
s3.remove(3)
print(s3)

s3.discard(2)
print(s3)

popped_element = s3.pop()
print(popped_element)
print(s3)

# Clearing All Elements:

s4 = {1, 2, 3}
s4.clear()
print(s4)

# Checking Membership:

s5 = {1, 2, 3}
print(2 in s5)
print(4 in s5)

# Set Operations
# Union:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

# Intersection:

set11 = {1, 2, 3}
set22 = {2, 3, 4}
intersection_set = set11 & set22
print(intersection_set)

# Difference:

set111 = {1, 2, 3}
set222 = {2, 3, 4}
difference_set = set111 - set222
print(difference_set)

# Symmetric Difference:

set1111 = {1, 2, 3}
set2222 = {2, 3, 4}
sym_diff_set = set1111 ^ set2222
print(sym_diff_set)

# Set Methods
# Adding Multiple Elements:

my_set1 = {1, 2}
my_set1.update([2, 3, 4])
print(my_set1)

# Copying a Set:

original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)

# Examples of Using Sets
# Removing Duplicates from a List:

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(my_list))
print(unique_elements)

# Finding Common Elements in Two Lists:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)

# Finding Elements in One List but Not in Another:

list11 = [1, 2, 3, 4]
list22 = [3, 4, 5, 6]
difference_elements = list(set(list11) - set(list22))
print(difference_elements)

# Finding Unique Characters in a String:

my_string = "hello world"
unique_chars = set(my_string)
print(unique_chars)
