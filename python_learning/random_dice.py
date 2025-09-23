import random

dice_roll = []

for i in range(1,11):
    dice_roll.append(random.randint(1,6))

print(dice_roll)