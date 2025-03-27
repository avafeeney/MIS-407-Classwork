import csv

store_sales = {}

total_sales_ames = 0

with open('Iowa-Liquor-Sales-Ames-2020.csv') as csvfile:
    reader = csv.reader(csvfile)

    next(reader, None)

    for row in reader:
        store_name = row[3].upper()
        volume_sold_liters = float(row[19])

        store_sales[store_name] = store_sales.get(store_name, 0) + volume_sold_liters

        if row[8].upper() == 'AMES':
            total_sales_ames += volume_sold_liters


# Sort the store sales by volume in descending order
sorted_store_sales = sorted(store_sales.items(), key=lambda x: x[1], reverse=True)

# Print the total store sales ordered by volume
print("Total store alcohol sales by volume:")
for i, (store_name, sales_volume) in enumerate(sorted_store_sales, start=1):
    print(f"{i}. {store_name} {sales_volume:.2f} liters")

# Print the total sales in Ames, Iowa
print(f"Total sales in Ames: {total_sales_ames:.3f} liters")