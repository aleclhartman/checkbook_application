from os import path


def record_credit():
    amount = input("\n Please enter the amount of the credit: $")
    amount = amount.replace(',', "")
    while (amount.isalpha() == True
            or float(amount) < 0
            or abs(float(amount)) == 0.0):
        print(f"\n {amount} is not a valid input. Please enter a positive number with a maximum of two decimal places.")
        amount = input("\n Please enter the amount of the credit: $")

    filename = "transactions.txt"

    if path.exists(filename) == True:
        with open(filename, "a") as f:
                f.write(amount + "\n")
    else:
        with open(filename, "w") as f:
            f.write(amount + "\n")

record_credit()