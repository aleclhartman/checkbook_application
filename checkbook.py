# welcoming user
print("")
print("~~~ Welcome to your terminal checkbook! ~~~")
print("")

# prompting user for input
print("\n Please enter the number corresponding with your desired action from the following menu options: \n \n 1) View current balance \n 2) Record a debit (withdraw) \n 3) Record a credit (deposit) \n 4) Exit")
user_choice = input("\n Your choice ")

while (user_choice.isdigit() == False
            or int(user_choice) not in range(1, 5)):
    print(f"\n {user_choice} is not a valid input. Please enter a number between 1 and 4.")
    print("\n Please enter the number corresponding with your desired action from menu options below: \n \n 1) View current balance \n 2) Record a debit (withdraw) \n 3) Record a credit (deposit) \n 4) Exit")
    user_choice = input("\n Your choice ")

user_choice = int(user_choice)

while (user_choice in range(1, 5)):    
    if user_choice == 1:

        print("\n Your current balance is ")
        
        break

    if user_choice == 2:
        print("\n Record a debit (withdraw) \n")
        break

    if user_choice == 3:
        print("\n Record a credit (deposit) \n")
        break
        
    if user_choice == 4:
        print("\n Goodbye! \n")
        exit()