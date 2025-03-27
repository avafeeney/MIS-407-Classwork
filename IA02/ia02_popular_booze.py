import csv

store_products = {}

with open('Iowa-Liquor-Sales-Ames-2020.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)


    header = next(reader, None)

    store_name_idx = header.index('Store Name')
    product_name_idx = header.index('Item Description')
    volume_sold_liters_idx = header.index('Volume Sold (Liters)')

    for row in reader:
        store_name = row[store_name_idx].strip().upper()
        product_name = row[product_name_idx].strip()
        volume_sold_liters = float(row[volume_sold_liters_idx])

        if store_name not in store_products:
            store_products[store_name] = {}
        if product_name not in store_products[store_name]:
            store_products[store_name][product_name] = 0
        store_products[store_name][product_name] += volume_sold_liters

print("Most popular product by volume in each store in Ames:")
for i, store_name in enumerate(sorted(store_products.keys()), start=1):
    product_volume_dict = store_products[store_name]
    most_popular_product = max(product_volume_dict, key=product_volume_dict.get)
    most_popular_volume = product_volume_dict[most_popular_product]
    print(f"{i}. {store_name} {most_popular_product} {most_popular_volume:.2f} liters")
