# Make a program that Ask the user is they would like to deposit
# or withdraw money from there bank account

Max = 1

balance = float(input('Enter how much money you have in your bank account: '))

while True:
    user = input("""Enter '1' if you would like to deposit or '2' \
                 if your would like to withdraw (or 'q' to quit): """)
    if user == '1':
        for money in range(Max):
            deposit = float(input('Enter the amount of money you would like to deposit: '))
            balance += deposit  # Easier way of putting balance = balance - deposit
            print(f'You now have ${balance} in your account.')
    elif user == '2':
        for money in range(Max):
            withdraw = float(input('Enter the amount you would like to withdraw: '))
            balance -= withdraw # balance = balance - withdraw
            print(f'You now have ${balance} in your account.')
    elif user == 'q':
        break
