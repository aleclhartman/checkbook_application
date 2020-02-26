from os import path

def menu():
    print("Please enter the number corresponding with your desired action from the following menu options: \n \n 1) View current balance \n 2) Record a debit (withdraw) \n 3) Record a credit (deposit) \n 4) Exit")
    user_choice = input("\n Your choice ")

    while (user_choice.isdigit() == False
                or int(user_choice) not in range(1, 5)):

        print(f"\n {user_choice} is not a valid input. Please enter a number between 1 and 4.")

        print("\n Please enter the number corresponding with your desired action from menu options below: \n \n 1) View current balance \n 2) Record a debit (withdraw) \n 3) Record a credit (deposit) \n 4) Exit")
        
        user_choice = input("\n Your choice ")

    user_choice = int(user_choice)

    while (user_choice in range(1, 5)):    

        if user_choice == 1:
            filename = "transactions.txt"
            beginning_balance = ["$100.00"]

            if path.exists(filename) == True:
                with open(filename) as f:
                    entries = f.readlines()
                    for entry in entries:
                        print(f"\n Your current balance is {entry}")
            else:
                with open(filename, "w") as f:
                    for entry in beginning_balance:
                        f.write(entry + "\n")
                with open(filename) as f:
                    entries = f.readlines()
                    for entry in beginning_balance:
                        print(f"\n Your current balance is {entry}")
            menu()

        if user_choice == 2:
            print("\n Please enter the amount of the debit ")
            menu()

        if user_choice == 3:
            print("\n Please enter the amount of the credit ")
            menu()
            
        if user_choice == 4:
            print("\n Goodbye! \n")
            exit()

menu()

