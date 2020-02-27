import decimal
from os import path

# welcoming user
print("")
print("~~~ Welcome to your terminal checkbook! ~~~")

def get_balance():
    filename = "transactions.txt"
    balance = 0.00
    beginning_balance = ["0.00"]
    # if "transactions.txt" exists, read the lines and calculate balance
    if path.exists(filename) == True:
        with open(filename) as f:
            entries = f.readlines()
            for entry in entries:
                entry = entry.strip("\n")
                entry = float(entry)
                balance += entry
        # else, create "transactions.txt" with a starting balance of $100.00
    else:
        with open(filename, "w") as f:
            for value in beginning_balance:
                f.write(value + "\n")
            with open(filename) as f:
                value = f.readlines()
                for value in beginning_balance:
                    value = value.strip("\n")
                    value = float(value)
                    balance = value
    return balance

# prompting user for input
def menu():
    print("\n Please enter the number corresponding with your desired action from the following menu options: \n \n 1) View current balance \n 2) Record a debit (withdraw) \n 3) Record a credit (deposit) \n 4) Exit")
    user_choice = input("\n Your choice ")
    # if invalid input, run the code below
    while (user_choice.isdigit() == False
                or int(user_choice) not in range(1, 5)):

        print(f"\n {user_choice} is not a valid input. Please enter a number between 1 and 4.")

        user_choice = input("\n Your choice ")

    user_choice = int(user_choice)

    #working with valid user input
    while (user_choice in range(1, 5)):    

        # user entered 1 - showing balance
        if user_choice == 1:
            #defining show_balance()
            def show_balance():

                balance = '${:,.2f}'.format(get_balance())
                print(f"\n Your current balance is {balance}.")
                
            show_balance()

            menu()

        if user_choice == 2:
            def record_debit():
                balance = get_balance()
                if balance == 0:
                    print("\n You broke! Make a deposit before attempting to withdraw. Returning to menu...")
                    menu()
                amount = input("\n Please enter the amount of the debit: $")
                amount = amount.replace(",", "")
                try:
                    float(amount)
                except ValueError:
                    print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
                    record_debit()
                    return
                while (float(amount) < 0.0
                        or abs(float(amount)) == 0.0
                        or decimal.Decimal(amount).as_tuple().exponent < -2):
                    print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
                    record_debit()
                    return

                filename = "transactions.txt"

                if float(amount) > balance:
                    print(f"\n Insufficient funds! ${amount} is not a valid input. Please enter a positive number with a maximum of two decimal places no greater than ${balance}.")
                    record_debit()
                    return
                else:
                    with open(filename, "a") as f:
                            f.write("-" + amount + "\n")

            record_debit()

            menu()

        if user_choice == 3:
            def record_credit():
                amount = input("\n Please enter the amount of the credit: $")
                amount = amount.replace(",", "")
                try:
                    float(amount)
                except ValueError:
                    print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
                    record_credit()
                    return
                while (float(amount) < 0.0
                        or abs(float(amount)) == 0.0
                        or decimal.Decimal(amount).as_tuple().exponent < -2):
                    print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
                    record_credit()
                    return

                filename = "transactions.txt"

                if path.exists(filename) == True:
                    with open(filename, "a") as f:
                            f.write(amount + "\n")
                else:
                    with open(filename, "w") as f:
                        f.write(amount + "\n")

            record_credit()

            menu()
            
        if user_choice == 4:
            print("\n Thanks, have a great day! Goodbye 🙂 \n")
            exit()

menu()