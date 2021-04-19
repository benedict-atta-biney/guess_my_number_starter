"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""


# use code below  to generate a random integer between 1 and 99 for example


# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
import random

Computer_PickNumber = random.randint(1, 99)
print(Computer_PickNumber)
user_first_name = input("What is your first name?")

print("Hello   " + user_first_name + " I have a number in mind. Guess it?")
is_number_correct = False
while not is_number_correct:
    User_GuessNumber = int(input("Enter a guess :  "))
    if User_GuessNumber == Computer_PickNumber:
        print("Congrats! The number was  : " + str(Computer_PickNumber) )
        is_number_correct = True

    elif User_GuessNumber < Computer_PickNumber:
        print("Your number is too low. Try again")

    else:

        print("Your number is too high. Try again")
        User_GuessNumber = int(input("Enter new guess :  "))



