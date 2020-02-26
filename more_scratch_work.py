from os import path

def show_balance():
    filename = "transactions.txt"
    beginning_balance = ["$100.00"]

    if path.exists(filename) == True:
        with open(filename) as f:
            entries = f.readlines()
            for entry in entries:
                print(f"\n (Existing) Your current balance is {entry}")
    else:
        with open(filename, "w") as f:
            for entry in beginning_balance:
                f.write(entry + "\n")
        with open(filename) as f:
            entries = f.readlines()
            for entry in beginning_balance:
                print(f"\n (New) Your current balance is {entry} \n")

show_balance()

def record_debit():
    amount = input("Please enter the amount of the debit (withdraw): ")
    filename = "transactions.txt"

    if path.exists(filename) == True:
        with open(filename, "a") as f:
                for entry in entries:
                    f.write("$" + str(float(amount)) + "\n")
    else:
        with open(filename, "w") as f:
            f.write("$" + str(float(amount)) + "\n")

record_debit()

entries = [100, 20, 80, 220]
balance = sum([entry for entry in entries])
balance