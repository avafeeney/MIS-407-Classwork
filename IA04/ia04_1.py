# Student: Ava Feeney
# Class: MIS407
# Semester: Fall 2023
# Assignment: ia04

from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.sql import func, and_

eng = create_engine("sqlite:///booze-central-ia.sqlite")
meta = MetaData()
meta.create_all(eng)
meta.reflect(eng)
booze = Table("booze", meta, autoload_with=eng)

product = input("Enter product name to match: ")

stmt = select(booze.c.PRODUCT_NAME, booze.c.STORE_NAME, func.sum(booze.c.VOLUME))
stmt = stmt.where(booze.c.PRODUCT_NAME.like(product))
stmt = stmt.group_by(booze.c.PRODUCT_NAME, booze.c.STORE_NAME)
stmt = stmt.order_by(booze.c.PRODUCT_NAME, booze.c.STORE_NAME)

with eng.connect() as con:
    result = con.execute(stmt)

    if result.rowcount == 0:
        print("No matching records found.")
    else:
        print(f"Volumes of products matching {product}")
        counter = 1

        for row in result:
            print(f"  {counter}. {row.PRODUCT_NAME} {row.STORE_NAME} {row[2]:.2f} liters")
            counter += 1

eng.dispose()
