from random import randint
import re


def roll(input_roll):
    dice_type = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    dice_roll = re.split('[D+-]', input_roll)
    if dice_roll[0] == "":
        dice_roll[0] = "1"
    roll_multiplier = int(dice_roll[0])
    result = int(roll_multiplier) * randint(1, int(dice_roll[1]))
    if "-" in input_roll:
        modifier = dice_roll[2]
        result = (int(roll_multiplier) * randint(1, int(dice_roll[1])) - int(modifier))
    if "+" in input_roll:
        modifier = dice_roll[2]
        result = (int(roll_multiplier) * randint(1, int(dice_roll[1])) + int(modifier))
    return result


print(roll("2D10+10"))
print(roll("D6"))
print(roll("2D3"))
print(roll("D12-10"))
print(roll("3D12+10"))
