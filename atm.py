from utils import get_amount, show_message

def check_balance(balance):
    print("Your Balance:", balance)

def deposit(balance):
    amt = get_amount("Enter amount to deposit: ")
    balance += amt
    show_message("Amount deposited!")
    return balance

def withdraw(balance):
    amt = get_amount("Enter amount to withdraw: ")

    if amt <= balance:
        balance -= amt
        show_message("Collect your cash")
    else:
        show_message("Insufficient balance!")

    return balance