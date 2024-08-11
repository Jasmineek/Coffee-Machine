menu = {
    "espresso" : {
        "ingredients" :{
            "water" : 50,
            "coffee" : 18,
        },
    "cost" : 25,    
    },
    "latte" : {
        "ingredients" :{
            "water" : 200,
            "coffee" : 24,
            "milk" : 150,
        },
    "cost" : 50,    
    },
    "cappuccino" : {
        "ingredients" :{
            "water" : 250,
            "coffee" : 24,
            "milk" : 100,
        },
    "cost" : 75,    
    },
}
resources = {
    "milk" : 2000,
    "water" : 2500,
    "coffee" : 250,
}
def ask_again():
    ask = input("Would you like to buy again? :").lower()
    if ask == 'yes':
        return True
    else:
        print("Switching OFF the machine, Thank you!")
        return False
def is_available(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item] :
            print("Sorry, we have no sufficient resources for your order.")
            is_on = ask_again()
        else:
            resources[item] = resources[item] - order_ingredients[item]
            return True     
def pay_for_coffee(amount):
    token1 = int(input("Enter the count of Rs 10: "))
    token2 = int(input("Enter the count of Rs 20: "))
    token3 = int(input("Enter the count of Rs 50: "))
    total = (token1*10) + (token2*20) + (token3*50)
    if total < amount :
        print("Sorry, this isn't enough money. Try again")
        is_on = ask_again()
    else:
        if total > amount:
            balance = total - amount
            print(f"Please collect your balance amount {balance}") 
def check_resources():
    print("Here is the list of ingredients left: ")
    for key, value in resources.items():
        print(f"{key} : {value}")               
#beginning
is_on = input("Enter 'ON' or 'OFF' the machine: ").lower()
if is_on == 'on':
    is_on = True    
    print("Hello, Nice to meet you!")
else:
    is_on = False
#Ask for the drink
while is_on:
    customer = input("What would you like to do? \nType '1' to Order a coffee or '2' to check the report of ingredients: \n")
    if customer == '2':
        check_resources()
        is_on = ask_again()
    elif customer == '1':
        choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
        if choice in menu:
            drink = menu[choice]
            if is_available(drink["ingredients"]):
                print(f"Please pay an amount of {drink["cost"]}")
                pay_for_coffee(drink["cost"])
                print(f"Here is your {choice},and Have a good day!")
                is_on = ask_again()
        else:
            print(f"Sorry, We don't have {choice} in our Menu.")
            is_on = ask_again()
