def deposit(balance, amount):
    if amount <= 0:
        return balance, "Invalid deposit amount."

    balance = balance + amount
    return balance, "Amount deposited successfully."


def withdraw(balance, amount):
    if amount <= 0:
        return balance, "Invalid withdrawal amount."

    if amount > balance:
        return balance, "Insufficient balance."

    balance = balance - amount
    return balance, "Amount withdrawn successfully."


def check_balance(balance):
    return balance


def display_account(name, account_number, balance):
    print("\n--- Account Details ---")
    print("Account Holder:", name)
    print("Account Number:", account_number)
    print("Current Balance: ₹", balance)