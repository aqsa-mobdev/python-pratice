balance = 5000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient Balance!")

deposit(1000)
withdraw(2000)

print("Updated Balance:", balance)