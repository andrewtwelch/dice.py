# dice_test.py
# Test script for dice.py
# bitbucket.org/andrewtwelch

import dice

# List of dice to test (other than d100)
test_list = [4, 6, 8, 10, 12, 20]

# Gets number of times to roll each dice to test
test_iterations = int(input("How many tests for each dice type: "))

# For each dice in test_list, rolls it test_iterations times and ensures it's a valid roll
for dice_roll in test_list:
    for x in range(1,test_iterations):
        print("d" + str(dice_roll) + " roll " + str(x) + " of "
              + str(test_iterations) + ": ", end="")
        roll = dice.roll_singular(dice_roll)
        if roll < 1 or roll > dice_roll:
            print("FAILURE")
        else:
            print(str(roll))

for x in range(1,test_iterations):
    print("d100 roll " + str(x+1) + " of "
              + str(test_iterations) + ": ", end="")
    roll = dice.roll_percentile_singular()
    if roll < 0 or roll > 99:
        print("FAILURE")
    else:
        print(str(roll))
