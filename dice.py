# dice.py
# Author: andrewtwelch
# bitbucket.org/andrewtwelch

import random

# Rolls a singular dice of a given size
def roll_singular(size):
    size = int(size)
    rolls_temp = []
    for x in range(0,size):
        rolls_temp.append(random.randint(1,size))
    selected_roll = random.randint(1,size) - 1
    return rolls_temp[selected_roll]

# Rolls 2 d10s to make up a d100 roll
def roll_percentile_singular():
    roll_tens = roll_singular(10) - 1
    roll_ones = roll_singular(10) - 1
    roll_result = (roll_tens * 10) + roll_ones
    return roll_result

# Gets the dice the user wants rolled and validates the input
def get_dice_rolls():
    DICE_TYPES = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100', 'd%']
    dice_rolls = []
    more_rolls = True
    while more_rolls or len(dice_rolls) == 0:
        if len(dice_rolls) > 0:
            print("\nDice to be rolled:")
            for dice in dice_rolls:
                print(dice, end=" ")
        print("\n")
        dice_input = input("Enter the dice to be rolled (enter to roll them): ")
        split_index = dice_input.find('d')
        if dice_input == "":
            more_rolls = False
            continue  
        elif split_index == -1:
            print("/nInvalid dice.")
            continue
        else:
            quantity = dice_input[:split_index]
            dice = dice_input[split_index:].lower()
            if DICE_TYPES.count(dice) == 0:
                print("/nInvalid dice.")
                continue
            else:
                if quantity == "":
                    quantity = 1
                else:
                    quantity = int(quantity)
                for x in range(0,quantity):
                    if dice == "d%":
                        dice = "d100"
                    dice_rolls.append(dice)
    return dice_rolls

# Rolls the requested dice and returns a list of lists containing the dice and result
def roll_dice(dice_rolls):
    rolled_dice = []
    for dice in dice_rolls:
        if dice == "d100":
            result = roll_percentile_singular()
        else:
            result = roll_singular(dice[1:])
        rolled_dice.append([dice, result])
    return rolled_dice

# Takes the results of roll_dice() and prints them neatly
def print_dice_rolls(rolled_dice):
    print("\nResults:\n")
    for result in rolled_dice:
        print(str(result[0]) + ": " + str(result[1]))

# Used to prompt for Y/N
def yes_or_no():
    message = "Continue?"
    result = ""
    accepted = ["Y", "N",]
    print("\n")
    while accepted.count(result) == 0:
        result = input(message + " [Y/N]: ").upper()
    return result

# Main function of program
def main():
    DICE_TYPES = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100', 'd%']
    print("Welcome to dice.py")
    print("Accepted dice entries are: ", end="")
    for x in DICE_TYPES:
        print(x, end=" ")
    active = True
    while active:
        dice_to_roll = get_dice_rolls()
        dice_results = roll_dice(dice_to_roll)
        print_dice_rolls(dice_results)
        keep_going = yes_or_no()
        if keep_going == "N":
            active = False
    print("\nThanks for rolling!")

# If not called by another python script, runs main()
if __name__ == "__main__":
    main()
