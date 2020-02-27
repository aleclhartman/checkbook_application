import decimal
from os import path

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


read balance
debit greater than balance = invalid
debit less than balance = invalid