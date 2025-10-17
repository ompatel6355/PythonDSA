import random

my_list = ["Rock", "Paper", "Scissors"]


user_i = input("Select your choice from Rock, Paper, Scissors: ")
user_i = user_i.lower()
random_item = random.choice(my_list)
random_item = random_item.lower()
def Conditions(user_i, random_item):
    if user_i == random_item:
        return "tie"
    elif(
        (user_i == "rock" and random_item == "scissors") or
        (user_i == "scissors" and random_item == "paper") or
        (user_i == "paper" and random_item == "rock")
    ):
        return "you Win!!"
    else:
        return "You lose!"


print(f'Computer choose, {random_item}: ')
result = Conditions(user_i, random_item)
print(result)