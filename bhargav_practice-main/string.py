str1 = "Hello, world"
str2 = 'Python Programming'

data1 = str1 + str2
print(data1)

data2 = str1 * 3
print(data2)

# Indexing:

first_char = str1[0]
print(first_char)

last_char = str1[-1]
print(last_char)

# Slicing

data3 = str1[0:5]
print(data3)

data4 = str1[7:]
print(data4)

data5 = str1[:5]
print(data5)

data6 = str1[::2]
print(data6)

# String Methods:

data7 = str1.upper()
print(data7)

data8 = str1.lower()
print(data8)

data9 = str1.capitalize()
print(data9)

data10 = str1.title()
print(data10)

data11 = str1.replace("world", "Python")
print(data11)

data_index = str1.find("world")
print(data_index)

str3 = "bhargav, nithin, python"

# Split

str4 = str3.split(", ")
print(str4)

# Join

str5 = " & ".join(str4)
print(str5)

# string properties

str6 = "Bhargav123"

str7 = str1.isalpha()
print(str7)

str8 = str1.isdigit()
print(str8)

str9 = str1.isalnum()
print(str9)

str10 = str1.startswith("He")
print(str10)

str11 = str1.endswith("23")
print(str11)

# escape

long_string2 = 'welcome to nithin\'s classes'
print(long_string2)

# tab

long_string3 = "welcome to \tnithin\'s classes"
print(long_string3)

# tab value

long_string4 = "welcome to \tnithin\'s classes"
print(long_string4.expandtabs(8))

# new line

long_string5 = "welcome\n to \nnithin\'s \nclasses"
print(long_string5)
