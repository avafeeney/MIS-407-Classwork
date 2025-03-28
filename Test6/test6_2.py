import sqlite3

sqlite_filename = 'test6_2.sqlite'
conn = sqlite3.connect(sqlite_filename)
c = conn.cursor()
# Run the CREATE TABLE statement.
create_table_stmt = "CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, desc TEXT, amount REAL)"
c.execute(create_table_stmt)

date = input("Enter date of transaction: ")
desc = input("Enter description: ")
amount = float(input("Enter amount of transaction (negative for withdrawal): "))
# TODO: Add the missing code that inserts the new transaction date, desc, and amount
# (use NULL for the id so SQLite will automatically fill in the next ID number)
c.execute('''
    INSERT INTO transactions (id, date, desc, amount)
    VALUES (NULL, ?, ?, ?)
''', (date, desc, amount))

conn.commit()

c.execute('SELECT id, date, desc, amount FROM transactions ORDER BY id')
balance = 0
for row in c:
    print(row)
    # TODO: Add this transaction's amount to the balance
    balance += row[3]
print("Ending account balance: ", balance)
conn.close()