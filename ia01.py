# Student: Ava Feeney
# Class: MIS407
# Semester: Fall 2023
# Program: ia01

accounts = [
    {"name": "Checking", "balance": 1000.00},
    {"name": "Savings", "balance": 500.00},
    {"name": "Credit Card", "balance": -450.00}
]

def show_accounts():
    idx = 0
    print('Num  Account Name            Balance')
    for account in accounts:
        print(f'{idx:3d}. {account["name"]:20s} {account["balance"]:10.2f}')
        idx += 1

done = False
while not done:
    show_accounts()

    user_input = input("Enter account index (0 for Checking, 1 for Savings, 2 for Credit Card), or q to exit: ")

    if user_input.lower() == 'q':
        break

    try:
        account_idx = int(user_input)
        if 0 <= account_idx < len(accounts):
            print(f'Selected Account: {accounts[account_idx]["name"]}')
            transaction_amount = float(input("Enter transaction amount: "))

            accounts[account_idx]["balance"] += transaction_amount

        else:
            print("Invalid account index. Please enter a valid index.")

    except ValueError:
        print("Invalid input. Please enter a valid account index or 'q' to quit.")


