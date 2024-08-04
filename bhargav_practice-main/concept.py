# premitive data types:
#
# intrger - 1, 2, 123, 555
# float - 1.1, 0.2, 0.003, 555.3
# Boolean - True, False
# complex - 3+2j, 5-1k
#
# string - "bhargav", 'bhargav', """bhargav""", '''bhargav'''
#
# collection datatypes:
# list - [1, 22, "the", True, 2.33]
# tuple - (1, 22, "the", True, 2.33)
# set = {1, 2, 3, 4}
# dict = {1:2, 3:10, 5:10}

a = 1
b = 2
c = 1
print(id(a), id(b), id(c))

# variable reference count == 0 garbage collector

s = "nithin"
d = "nithin"
ss = s.capitalize()
sss = ss.upper()
print(s, ss, sss)
print(id(s), id(ss), id(sss), id(d))

# mutable - Immutable

# iterable - Non-iterable
# not-iterables  --> int, float, bool
# iterables --> String, collection datatypes

s = "bhargav kirne"
print(s[7])
print(len(s))
for i in s:
    print(i * 2)

integ = 123324242
# for j in integ:
#     print(j * 2)

print(s[2:6])
# print(integ[1:6])
