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

