from random import randint
import re


def roll(rzut):
    dice_roll = re.split('[D+-]', rzut)
    if dice_roll[0] == "":
        dice_roll[0] = "1"
    roll_multiplier = int(dice_roll[0])
    result = int(roll_multiplier) * randint(1, int(dice_roll[1]))
    if "-" in rzut:
        modifier = "-"+dice_roll[2]
        result = int(roll_multiplier)*randint(1, int(dice_roll[1])-int(modifier))
    if "+" in rzut:
        modifier = "+"+dice_roll[2]
        result = int(roll_multiplier) * randint(1, int(dice_roll[1]) + int(modifier))
    return result


print(roll("2D10+10"))
print(roll("D6"))
print(roll("2D3"))
print(roll("D12-1"))
