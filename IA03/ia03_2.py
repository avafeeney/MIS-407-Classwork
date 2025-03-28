# Student: Ava Feeney
# Class: MIS407
# Semester: Fall 2023
# Assignment: ia03

import sqlite3

def query_database(county_name, store_name):

    conn = sqlite3.connect("booze-central-ia.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT STORE_NAME, PRODUCT_NAME, SUM(VOLUME)
    FROM booze
    WHERE COUNTY_NAME LIKE ? AND STORE_NAME LIKE ?
    GROUP BY STORE_NAME, PRODUCT_NAME
    ORDER BY STORE_NAME, PRODUCT_NAME
    """

    county_name = county_name.upper()
    store_name = "%" + store_name + "%"

    cursor.execute(query, (county_name, store_name))

    results = cursor.fetchall()
    if results:
        print(f"Volumes of product sales matching store {store_name} in county {county_name}:")
        for idx, (store_name, product_name, volume) in enumerate(results, start=1):
            print(f"   {idx}. {store_name} {product_name} {volume:.2f} liters")
    else:
        print(f"No matching sales found for store {store_name} in county {county_name}.")

    conn.close()

if __name__ == "__main__":
    county_name_input = input("Enter county name to match (in upper-case): ")
    store_name_input = input("Enter store name to match: ")

    query_database(county_name_input, store_name_input)
