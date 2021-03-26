import re

def roll(rzut):
    dice_roll = re.split('[D+-]', rzut)
    roll_multiplier = 0
    modifier = 0
    if dice_roll[0] == "":
        dice_roll[0] = "1"
    roll_multiplier = int(dice_roll[0])
    dice_type = "D"+dice_roll[1]
    if "-" in rzut:
        modifier = "-"+dice_roll[2]
    if "+" in rzut:
        modifier = "+"+dice_roll[2]


    return f"Rodzaj kości: {dice_type}, ilośc rzutów: {roll_multiplier}, modyfikator: {modifier}",dice_roll


print(roll("2D10+10"))
print(roll("D6"))
print(roll("2D3"))
print(roll("D12-1"))
