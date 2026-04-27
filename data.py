balance = 1000   # default balance

def get_balance():
    return balance

def update_balance(new_balance):
    global balance
    balance = new_balance