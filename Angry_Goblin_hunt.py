import random

print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")
name = input ("type in your name")
level = input ("enter a difficulty level [5-50]")
print(f"{name}, do you think you can find the goblin hiding in the kitchen cupboards?")
print("|_|" * int(level))
goblin_position = random.randint(1,5)
for i in range (5):
    cupboard_number = input("Which cupboard do you think the goblin is in [type in number]:")
    print(cupboard_number)
    cupboard_number=int(cupboard_number)
    if cupboard_number == goblin_position:
        print("Well done! You have found the goblin. He was so scared he ran away.")
        break
    else:
        print("Sorry! The goblin is still lurking somewhere else.")



