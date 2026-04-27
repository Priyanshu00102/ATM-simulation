def get_amount(msg):
    try:
        return int(input(msg))
    except:
        print("Invalid input!")
        return 0

def show_message(msg):
    print("👉", msg)