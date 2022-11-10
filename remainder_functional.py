#Problem statement : Give a string input, print alternate characters starting from index 0

# Example string : Python

#Output : P
#         t
#         o

# Step1: Get the input string and save to a variable
# Step2: Print the character at first index
# Step3: Skip the next one
# Step4: print the next character
# And it goes on.

# Steps for machine

# Step1: Get the input and store in a variable
# Step2: print the character at first index
# Step3: Skip the next one
# Step4: Repeat 2 and 3 until all characters are completed.

str_in = input("Enter a string value: ")
print(f"You entered string value <{str_in}>")
print(f"Printing alternate characters of the string <{str_in}>")
i = 1
for ch in str_in:
    #print(f"Iteration no: {1}")

    if i % 2 ==0:
        i = i + 1
        continue
        print(ch)
        i = i + 1