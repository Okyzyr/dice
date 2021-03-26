from random import randint
import re

def check(dice):
    dice_type_allowed = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    result = False
    for i in dice_type_allowed:
        if i in dice:
            result = True
    return result


def roll(input_roll):
    if check(input_roll) == True:
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
    else:
        result = "Wrong dice"
        return result


print(roll("czsafda"))
print(roll("2D1+10"))
print(roll("2D10+10"))
print(roll("D6"))
print(roll("2D3"))
print(roll("D12-10"))
print(roll("3D12+10"))