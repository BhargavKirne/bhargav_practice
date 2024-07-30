# zip into FUNCTIONS

a = [1, 2, 3, 4, 5]
b = [7, 8, 9, 0, 4]
c = [4, 5, 6, 7, 8]
d = [2, 3, 4]


def zip_list(a, b, c):
    return list(zip(a, b, c))


def zip_tuple(b, c, a):
    return tuple(zip(b, c, a))


def zip_dict(b, c):
    return dict(zip(b, c))


def zip_list_with_d(a, b, c, d):
    return list(zip(a, b, c, d))


def zip_string():
    return list(zip("nithin", "nithin"))


z = zip_list(a, b, c)
zz = zip_tuple(b, c, a)
zzz = zip_dict(b, c)
zzzz = zip_list_with_d(a, b, c, d)
e = zip_string()

print(z)
print(zz)
print(zzz)
print(zzzz)
print(e)

# filter which divides with 3 or 5

n = range(1, 30)

data1 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, n))

print(data1)

#  all map func to lambda

num = [1, 2, 3, 4, 5]

sq_num = list(map(lambda x: x ** 2, num))

print(sq_num)

str = ["bhargav", "nithin", "python"]

upper_str = list(map(lambda s: s.upper(), str))

print(upper_str)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

sum_lst = list(map(lambda x, y: x + y, l1, l2))

print(sum_lst)
