# lamda
import time

cn = 0


def hello_dummy():
    data1 = lambda: f"cn :{cn}, ct:{50}"
    print(data1())


hello_dummy()


def recursive_function():
    global cn
    cn += 1
    ct = 100
    ct += 1
    time.sleep(1)
    print(cn)
    while cn <= 5:
        print("hello", cn, "ct:", ct)
        recursive_function()


data2 = lambda: recursive_function()

data2()

data3 = lambda: "welcome to python"

data4 = data3()
print(data4)

li = [1, 2, 3, 4, "nithin", "python"]
li2 = [4, 5, 6, 7]

# Lambda to combine two lists
second_return_func_lambda = lambda a, s: (a.copy(), a.copy().extend(s))[0]

# Using the lambda
data5 = second_return_func_lambda(li, li2)
data6 = second_return_func_lambda(li2, li2)
data7 = second_return_func_lambda(li2, li)

print(data5)
print(data6)
print(data7)

multiple_arg = lambda a, b: (print(type(a), type(b)), sum([a, b]))[1]

m_data = multiple_arg(1, 2)
m_data2 = multiple_arg(6, 7)
m_data3 = multiple_arg(3, 4)
m_data6 = multiple_arg(3, 4)
m_data4 = multiple_arg(m_data, m_data2)
m_data5 = multiple_arg(m_data4, m_data3)
print(m_data5)

star_arg = lambda *c: (print(c), print(type(c)), sum(c))[2]

data8 = star_arg(1, 3, 4, 5, 6)

print(data8)

double_str_arg = lambda **d: (print(d), print(type(d)), sum(d.values()))[2]

data9 = double_str_arg(a=2, b=3, c=3, d=33)

print(data9)


# comp practice

def hello_dummy():
    global cn
    ct = [50 for _ in range(1)]
    print(f"cn: {cn}, ct: {ct[0]}")


hello_dummy()


def hi_welcome_to_recursive():
    global cn
    cn += 1
    ct = 100
    ct += 1
    time.sleep(1)
    print(cn)

    messages = [f"hello {cn}, ct: {ct}" for _ in range(1)]
    print(messages[0])

    if cn <= 5:
        hi_welcome_to_recursive()


hello_dummy()
hi_welcome_to_recursive()
hello_dummy()


def simple_pass_keyword():
    _ = [None for _ in range(0)]


simple_pass_keyword()


def first_return_statement():
    return [a for a in ["welcome to python"]][0]


data11 = first_return_statement()
print(data11)

li = [1, 2, 3, 4, "nithin", "python"]
li2 = [4, 5, 6, 7]


def second_return_func(a, s):
    return [i for j in (a, s) for i in j]


data12 = second_return_func(li, li2)  # li + li2
data22 = second_return_func(li2, li2)  # li2 + li2
data33 = second_return_func(li2, li)  # li2 + li

print(data12)
print(data22)
print(data33)


def multiple_arg(a, b):
    print(type(a), type(b))
    return sum([x for x in [a, b]])


m_data44 = multiple_arg(1, 2)
m_data55 = multiple_arg(6, 7)
m_data66 = multiple_arg(3, 4)
m_data99 = multiple_arg(3, 4)
m_data77 = multiple_arg(m_data44, m_data55)
m_data88 = multiple_arg(m_data77, m_data66)
print(m_data88)


def star_arg(*c):
    print(c)
    print(type(c))
    return sum([x for x in c])


s_dt = star_arg(1, 3, 4, 5, 6)
print(s_dt)


def double_str_arg(**d):
    print(d)
    print(type(d))
    return sum([v for v in d.values()])


print(double_str_arg(a=2, b=3, c=3, d=33))
