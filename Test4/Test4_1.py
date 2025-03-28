import sqlite3


sqlite_filename = 'test4_1.sqlite'
conn = sqlite3.connect(sqlite_filename)
c = conn.cursor()
# Run the CREATE TABLE statement.
create_table_stmt = "CREATE TABLE IF NOT EXISTS invoices (id INTEGER, date TEXT, customer TEXT, balance REAL)"
c.execute(create_table_stmt)

# Ask the user for invoice number (ID), date, customer name, and balance.
# Then use a SQL INSERT to add the new invoice to the `invoices` table
invoice_num = int(input("Enter invoice number: "))
date = input("Enter date of invoice: ")
cust_name = input("Enter customer name: ")
balance = float(input("Enter invoice balance: "))

c.execute('''
    INSERT INTO invoices (id, date, customer, balance)
    VALUES (?, ?, ?, ?)
''', (invoice_num, date, cust_name, balance))

conn.commit()

c.execute('SELECT id, date, customer, balance FROM invoices ORDER BY id')
total_balance = 0
for row in c:
    print(row)
    total_balance += row[3]
print("Total invoice balance: ", total_balance)
conn.close()