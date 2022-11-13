# Input
a= input("Enter a string: ")

# Show the string that was entered
print(f"You have entered: {a}")

# Slicing first character
b = a[1:]

# Slicing last characters from previous string
c = b[:-1]

# Print after removing fast and last character
print(f"Slice of '{a}' after removing first and last character '{c}'")

# Removing first 2 characters
d = a[2:]
print(f"Slice of '{a}' after removing first two character '{d}'")

# Removing last two characters
e = a[:-2]
print(f"Slice of '{a}' after removing last two character '{e}'")

# mid index
mid = len(a)//2
print(f"mid index is {mid}")

# First half of string
first_half = a[:len(a)//2]
print(f"First half slice of {a} is '{first_half}'")

# Second half of string
second_half = a[len(a)//2:]
print(f"Second half slice of {a} is '{second_half}'")