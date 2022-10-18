#addition
def add_numbers(x,y):
    return x + y

def sub_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y


def division(x, y):
    return x / y

def remainder(x, y):
    return x % y


def quotient(x, y):
    return x // y

def exponential(x, y):
    return x ** y

#choose an option
print ("Choose an option from the following:")
print("1) Add (+)")
print("(2) Subtract (-)")
print("(3) Multiply (*)")
print("(4) Divide (/)")
print("(5) Find Remainder (%)")
print("(6) Find Quotient (//)")
print("(7) Find Square of a number (**)")
choice = input("Option Selected: ")


#Get input from user
x = int(input("Enter first number: "))
if int(x) < 0:
            print(" please enter a positive number")
            exit()
y = int(input("Enter second number: "))
if int(y) < 0:
            print(" please enter a positive number")
            exit()

 #Calculation logic
if choice == '1':
            print("Output is  :", add_numbers(x,y))

elif choice == '2':
           print("Output is  :", sub_numbers(x, y))

elif choice == '3':
            print("Output is  :", multiply_numbers(x, y))

elif choice == '4':
            print("Output is  :", division(x, y))

elif choice == '5':
            print("Output is  :", remainder(x, y))

elif choice == '6':
    print("Output is  :", quotient(x, y))

elif choice == '7':
            print("Output is  :", exponential(x, y))

else :
    exit()





