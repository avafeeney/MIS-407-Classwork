# Student: Ava Feeney
# Class: MIS407
# Semester: Fall 2023
# Assignment: ia03

import sqlite3

def query_database(product_name):
    conn = sqlite3.connect("booze-central-ia.sqlite")
    cursor = conn.cursor()


    query = """
    SELECT STORE_NAME, PRODUCT_NAME, SUM(VOLUME)
    FROM booze
    WHERE PRODUCT_NAME LIKE ?
    GROUP BY PRODUCT_NAME, STORE_NAME
    ORDER BY PRODUCT_NAME, STORE_NAME
    """

    product_name = "%" + product_name + "%"

    cursor.execute(query, (product_name,))

    results = cursor.fetchall()
    if results:
        print(f"Volumes of products matching {product_name}:")
        for idx, (store_name, product_name, volume) in enumerate(results, start=1):
            print(f"  {idx}. {product_name} {store_name} {volume:.2f} liters")
    else:
        print(f"No products matching {product_name} found.")

    conn.close()

if __name__ == "__main__":

    product_name_input = input("Enter product name to match: ")

    query_database(product_name_input)