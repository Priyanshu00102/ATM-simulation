from atm import check_balance, deposit, withdraw
from data import get_balance, update_balance

balance = get_balance()

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        check_balance(balance)

    elif choice == 2:
        balance = deposit(balance)
        update_balance(balance)

    elif choice == 3:
        balance = withdraw(balance)
        update_balance(balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")