import random

lucky_number = random.randint(1,10)

fortune_number = random.randint(1,3)

if fortune_number == 1:
    print(f"Your Lucky Number is {lucky_number}. Today is your lucky day!")

if fortune_number == 2:
    print(f"Your Lucky Number is {lucky_number}. You might want to be cautious today.")

if fortune_number == 3:
    print(f"Your Lucky Number is {lucky_number}. An unexpected event may bring you joy today.")

