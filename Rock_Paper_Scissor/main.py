import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("enter our move = Rock, Paper, Scissor = ")

comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock")
    else:
        print("Rock smashes Scissor")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper")
    else:
        print("Paper covers Rock")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper")
    else :
        print("Sock smashes Scissor")


 
