import csv
total_interest = 0.0
interest_rate = 0.5
total_interest_to_pay = 0

with open("accounts.csv", "r", newline='') as input_file:
    reader = csv.reader(input_file)
    for row in reader:

        account_type = row[8]

        if account_type == 'SAVINGS':
            account_number = row[0]
            balance = float(row[7])

            interest_to_pay = balance * interest_rate

            total_interest_to_pay += interest_to_pay

            print(f"Account Number: {account_number}, Balance: ${balance:.2f}, Interest: ${interest_to_pay:.2f}")

print(f"Total Interest to Pay: ${total_interest_to_pay:.2f}")