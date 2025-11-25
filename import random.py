import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

if fortune_number == 1:
    print("You will meet the love of your life")

if fortune_number == 2:
    print("You will fall in love today")

if fortune_number == 3:
    print("Your life will change for good today")


print(f"{fortune_number} Your lucky number is {lucky_number}.")