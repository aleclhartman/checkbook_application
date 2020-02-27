from os import path

# welcoming user
print("")
print("~~~ Welcome to your terminal checkbook! ~~~")
print("")

# prompting user for input
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
            def show_balance():
                filename = "transactions.txt"
                beginning_balance = ["$100.00"]

                if path.exists(filename) == True:
                    with open(filename) as f:
                        entries = f.readlines()
                        for entry in entries:
                            entry = entry.strip("$")
                            entry = entry.strip("\n")
                            entry = float(entry)
                            balance += entry
                        print(f"\n Your current balance is {balance}")
                else:
                    with open(filename, "w") as f:
                        for entry in beginning_balance:
                            f.write(entry + "\n")
                    with open(filename) as f:
                        entries = f.readlines()
                        for entry in beginning_balance:
                            print(f"\n Your current balance is {entry} \n")

            show_balance()
            
            menu()

        if user_choice == 2:
            print("\n Please enter the amount of the debit \n")
            menu()

        if user_choice == 3:
            print("\n Please enter the amount of the credit \n")
            menu()
            
        if user_choice == 4:
            print("\n Goodbye! \n")
            exit()

menu()


# THIS IS WHAT WAS IN YOUR CHECKBOOK.PY AT 6:53PM

# ACCOUNT FOR RANDOM CHARACTERS
# ACCOUNT FOR DEBTS LARGER THAN BALANCE

        if user_choice == 2:
            def record_debit():
                amount = input("\n Please enter the amount of the debit: $")
                while (
                        or str(int(round(float(amount)))).isnumeric() == False
                        or float(amount) < 0.0
                        or abs(float(amount)) == 0.0
                        or decimal.Decimal(amount).as_tuple().exponent < -2):
                    print(f"\n {amount} is not a valid input. Please enter a positive number with no commas and a maximum of two decimal places.")
                    amount = input("\n Please enter the amount of the debit: $")

                filename = "transactions.txt"

                if path.exists(filename) == True:
                    with open(filename, "a") as f:
                            f.write("-" + amount + "\n")
                else:
                    with open(filename, "w") as f:
                        f.write("-" + amount + "\n")

            record_debit()

            menu()

        if user_choice == 3:
            def record_credit():
                amount = input("\n Please enter the amount of the credit: $")
                while ("," in amount
                        or str(int(round(float(amount)))).isnumeric() == False
                        or float(amount) < 0.0
                        or abs(float(amount)) == 0.0
                        or decimal.Decimal(amount).as_tuple().exponent < -2):
                    print(f"\n {amount} is not a valid input. Please enter a positive number with no commas and a maximum of two decimal places.")
                    amount = input("\n Please enter the amount of the credit: $")

                filename = "transactions.txt"

                if path.exists(filename) == True:
                    with open(filename, "a") as f:
                            f.write(amount + "\n")
                else:
                    with open(filename, "w") as f:
                        f.write(amount + "\n")

            record_credit()

            menu()


# 10:40

for character in amount:
        if character.isalpha() == True:
            print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
            break