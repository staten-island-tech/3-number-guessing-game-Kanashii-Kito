# count = 1

# while count <= 5:
#     print("This is loop number", count)
#     count = count + 1

# order = ""

# while order != "done":
#     order = input("What would you like to order? (type 'done' to finish): ")

# print("Thanks for your order!")

'''-----------------------------------------------------------------------------------------------------------------------------'''
'''Optional Challenge 2'''

# color = ""

# while color != "Stop.":
#     color = input("What is your favorite color? (Type |Stop.| when done.):  ")
# print ("Thank you for stating your favorite color along with everything about you.")

'''------------------------------------------------------------------------------------------------------------------------------'''

""" import random

ran = random.randint(1,10)
input = (f"Please input a number from {ran}") """

'''------------------------------------------------------------------------------------------------------------------------------------------------'''

import random

ran = random.randint(1, 10)

user_input = None

while user_input != ran:
    user_input = int(input("Please guess the random number selected from 1 to 10: "))
    if user_input < ran:
        print("Wrong number! Try again. Your number is less than the correct number.")
    elif user_input > ran:
        print ("Wrong number Try again. Your number is greater than the correct number.")

print("Thank you for guessing the correct number!")

'''------------------------------------------------------------------------------------------------------------------------------------------------'''

#     user_input = input(f"Please input a number from 1 to 10: ")
#     print ("If you got the message above again, that means you've guess the wrong number from 1 to 10 or what you've entered isn't a valid number.")
# if user_input is ran:
#     print ("Thank you for guessing the correct number.")