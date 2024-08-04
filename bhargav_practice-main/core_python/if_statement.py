x = 10

if x > 5:
    print("x is greater than 5")

x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

x = 7

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")

x = 15

if x > 10:
    print("x is greater than 10")

    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")

x = 7
y = 3

if x > 5 and y < 6:
    print("x is greater than 5 and y is less than 5")

if x > 5 or y > 5:
    print("Either x or y is greater than 5")

if not x < 5:
    print("x is not less than 5")

x = 10
result = "x is even" if x % 2 == 0 else "x is odd"
print(result)

names = ["bhargav", "nithin", "python"]

if "bhargav" in names:
    print("bhargav is in the list")
else:
    print("bhargav is not in the list")


def check_number(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"


print(check_number(10))
print(check_number(0))
print(check_number(-5))
