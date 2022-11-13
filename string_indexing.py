# Input
a = input("Enter a string: ")
print(f"You entered: {a}")
print("")


# Finding first character
first_character = a[0]
print(f"The first character of {a} is {first_character}")

# Finding last character
last_character = a[-1]
print(f"The last character of {a} is {last_character}")

# Length of string
print(f"The length of you string is {len(a)}")

# Middle index
print(f"Mid index is {(len(a)//2)}")

# Function for middle character
def middle_character(a):
  return a[(len(a)-1)//2:(len(a)+2)//2]
b= middle_character(a)
print(f"The middle character(s) of {a} is/are: {b}")