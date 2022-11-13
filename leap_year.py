 input year
year = int(input("Which year do you want to check? "))

# define condition 1
def leap1(year):
 return (year % 4)
# assign condition 1
a= leap1(year)

# define condition 2 to a
def leap2(year):
 return(year % 100)

# assign condition 2 to b
b= leap2(year)

# define condition 3 to c
def leap3(year):
 return(year % 400)
# assign condition 3
c= leap3(year)

# If the conditions are true (leap year), if not (not a leap year)
if a ==0:
 print("its a leap year")
elif b ==0 and c ==0:
 print("its a leap year")
else:
 print("not a leap year")