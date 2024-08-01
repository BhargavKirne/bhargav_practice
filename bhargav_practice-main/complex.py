a = 22 + 5j
print(type(a))
print(a.imag)
print(a.real)
print(a.conjugate())
b = 22 + 5j
print(id(a), id(b))

c = 3 + 4j
print(c.real)  # Output: 3.0
print(c.imag)  # Output: 4.0

# Basic Operations with Complex Numbers

# Addition:

c1 = 1 + 2j
c2 = 3 + 4j
data1 = c1 + c2
print(data1)

# Subtraction:

data2 = c1 - c2
print(data2)

# Multiplication:

data3 = c1 * c2
print(data3)

# Division:

data4 = c1 / c2
print(data4)

# Absolute Value:

data5 = abs(c1)
print(data5)
