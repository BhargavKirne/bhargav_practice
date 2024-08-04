names = ["bhargav", "nithin", "python"]
for name in names:
    print(name)

str = "Hello, world!"
for s in str:
    print(s)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

dict = {"name": "bhargav", "age": 30, "city": "hyderabad"}
for key in dict:
    print(key, dict[key])

squares = [x**2 for x in range(10)]
print(squares)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

