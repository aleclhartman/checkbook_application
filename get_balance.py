from os import path

def get_balance():
    filename = "transactions.txt"
    balance = 0
    if path.exists(filename) == True:
        with open(filename) as f:
            entries = f.readlines()
            for entry in entries:
                entry = entry.strip("\n")
                entry = float(entry)
                balance += entry
    print(balance)

get_balance()