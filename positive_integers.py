# Input 1st number
x = input("enter 1st number: ")

# Condition
if int(x) < 0:
    print (" please enter a positive number")
    exit()
else:
    print(f"first value is {x}")

# Get the second number
y = input("enter 2nd number: ")
# Condition
if int(y) < 0:
    print (" please enter a positive number")
    exit()
else:
    print("second value is " + y)
# add two numbers and store result
z = (int(x) + int(y))
print(f"Result is {z}")