import copy

# copy.copy()

li = [1, 2, 3, 4]
li1 = copy.copy(li)

li1[2] = 'Bhargav'

print("li:", li)
print("li1:", li1)

# deepcopy()

di = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
di1 = copy.deepcopy(di)

di1['b'][0] = 'Bhargav'
di1['c']['d'] = 'Kirne'

print("di:", di)
print("di1:", di1)

# list copy

l = [1, 2, 3, 4, 5]
l2 = l.copy()
l3 = l
l[2] = "Bhargav", 2.5
print(l)
print(l2)
print(l3)

# tuple copy

# t = (1, 2, 3, 4, 5)
# t2 = l.copy()
# t3 = l
# t[2] = "Bhargav"
# print(t)
# print(t2)
# print(t3)

# set copy

s = {1, 2, 3, 4, 5}
s1 = {6, 7, 8, 9, 10}
s2 = s1.copy()
print(s)
print(s1)
print(s2)

# dict copy

d = {1: 1, 2: 4, 3: 49, 4: 16, }
d2 = {5: 25, 6: 36, 7: 42}
d1 = d2.copy()
d = d2
d.update({8: 64})
print(d)
print(d2)
print(d1)
dd = d.copy()
print(dd)
d.update({"Bhargav": "python"})
print(d)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
li3 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def add_list(*a):
    lst = []
    for l in a:
        lst.extend(l)
    return lst


data1 = add_list(li, li2, li, li3, li, li, li2, li, li3, li, li2, li)
print("total list:", data1)