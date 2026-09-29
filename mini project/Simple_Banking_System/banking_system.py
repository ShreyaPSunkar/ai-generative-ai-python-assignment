from bank_utils import deposit, withdraw, check_balance, display_account


print("===== SIMPLE BANKING SYSTEM =====")

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

while True:
    print("\n----- Banking Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", check_balance(balance))

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance, message = deposit(balance, amount)
        print(message)
        print("Current Balance: ₹", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        balance, message = withdraw(balance, amount)
        print(message)
        print("Current Balance: ₹", balance)

    elif choice == "4":
        display_account(name, account_number, balance)

    elif choice == "5":
        print("Thank you for using the Simple Banking System.")
        break

    else:
        print("Invalid choice. Please try again.")