"""
Score - Jerome Ribaldone

Task:
Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt as below:
Psuedocode:


"""

import random

def main():
    score_amount = 0
    score_amount = float(input("Enter Number Of Scores: "))
    while score_amount > 0:
        score = random.randint(0, 100)
        print(f"{score} is {determine_status(score)}")
        score_amount = score_amount - 1

def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()