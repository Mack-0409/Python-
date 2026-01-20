
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("enter our move = Rock, Paper, Scissor = ")

comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers rock")
    else:
        print("Rock smashes scissor")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("scissor cuts paper")
    else:
        print("paper covers rock")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("scissor cuts paper")
    else :
        print("rock smashes scissor")


 
