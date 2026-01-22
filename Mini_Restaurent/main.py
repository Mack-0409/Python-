# Define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

# Greet
print("Welcome to PYTHON Restaurant")
print("pizza:40rs\nPasta:50rs\nBurger':60rs\nSalad':70rs\nCoffee':80rs")

order_total = 0

item_1 = input("Enter the name of item you want o order =  ")
if item_1 in menu:
    order_total = menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else :
        
     