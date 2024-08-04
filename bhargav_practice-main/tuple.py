# characteristics ==>

# it stored index value
# slicing supports
# iterable
# immutable
# allows any data type
# allows duplicates

empty_tuple = ()
single_element_tuple = (1,)
multi_element_tuple = (1, 2, 3)
mixed_tuple = (1, "apple", 3.14, True)

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

a = tuple((1, 2, 3, 4, 5))
b = tuple([1, 2, 3, 4, 5])
c = (6, 7, 8)
print(type(a), type(b), type(c))
d = ()
e = ("a",)
print(type(d), type(e))

tp = (1, 2, 2, 3, 3, True, 2 + 2j, "Python", [1, 2, 3], 2.33, (3, 4, 5))
print(tp[-3])
print(tp[2])
print(tp[1:5])
print(tp[1:])
print(tp[:10])
print(len(tp))
li_1 = []
for t in tp:
    li_1.append(t * 33)
print(li_1)
li = list(tp)
li[5] = 33
print(tp)
print(li)
tp = tuple(li)
print(tp)

tp1 = (1, 2, 3, 3, 2, True, 2 + 2j, 0, 2, "Python", [1, 2, 3], 2.33, (3, 4, 5))

print(tp1.index(False))
print(tp1.index(True))
print(tp1.index(2, ))
print(tp1.index(2, 2))
print(tp1.index(2, 2, 9))
print(tp1.index(2, 2, 6))

print(tp.count(2))
print(tp.count(99))
