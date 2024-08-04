# while loop

i = 1
while i <= 5:
    print(i)
    i += 1

# sum of numbers

i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("The sum is:", total)

# break statement

i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break

# while with else

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("while loop completed")

# while in while loop

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

# validate user input

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print("You entered a valid number:", number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
