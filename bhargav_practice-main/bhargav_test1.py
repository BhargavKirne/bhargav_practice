# string formats `f` sting and .formate method

a = 'seven'
b = "I'm Bhargav, my number is " + a
print(b)

a = 7
c = f"I'm Bhargav, my number is {a}"
print(c)

name = 'Bhargav'
print(f"I'm {name}, my number is 7")

# word under word

str1 = "Hi hello welcome to python classes, here we are learning about python string"
print(str1)

st = str1.split()
for s in st:
    print(s)

# list vs tuple with example
import sys

# Lists are mutable, Tuples are immutable
# The list is better for performing operations, such as insertion and deletion.
# A Tuple data type is appropriate for accessing the elements
# Lists use more memory, Tuple use less memory

l = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print(l)

l[2] = 222
print(l)

t = (0, 1, 2, 3, 4, 5, 6, 7)
print(t)

# t[4] = 555
# print(t)

print(sys.getsizeof(l))
print(sys.getsizeof(t))

# count of each item

li = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 6, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 7]
ss = set(li)

for i in ss:
    print(f"{i}: {li.count(i)}")

# common items, different items, subset

a = {1, 2, 3, 4, 5, 6, 7}
b = {4, 5, 6, 7, 8, 9, 0}
c = {2, 3}

d = a.intersection(b)
print(d)
e = a.union(b)
print(e - d)

if c.issubset(a):
    print("c is subset to a")
else:
    print("c is not subset to a")

if c.issubset(b):
    print("c is subset to b")
else:
    print("c is not subset to b")

if c.issubset(a) and c.issubset(b):
    print("c is subset to a,b")
else:
    print("c is not subset to a,b")

# generate even numbers till 100 by using range function and odd numbers

for i in range(100):
    if i % 2 == 0:
        print(f"{i} is even num")
    elif i % 2 != 0:
        print(f"{i} is odd number")
    else:
        print("unknown")

for i in range(100):
    if i % 2 == 0:
        print(f"{i} is even num")

for i in range(100):
    if i % 2 == 1:
        print(f"{i} odd number")

# add, change value, setdefault

di = {1: 1, 2: 4, 3: 6}
print(di)

di.update({4: 16})
print(di)

di[1] = 77
print(di)

di.setdefault(5, 25)
print(di)

# separate even number di to add number di

di = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196}
even_dict = {}
odd_dict = {}

for key, value in di.items():
    if key % 2 == 0:
        even_dict[key] = value
    else:
        odd_dict[key] = value
print(even_dict)
print(odd_dict)