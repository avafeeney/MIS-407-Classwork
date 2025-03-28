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

county_name = input("Enter county name to match (all upper-case): ")
store_name = input("Enter store name to match: ")

stmt = select(booze.c.STORE_NAME, booze.c.PRODUCT_NAME, func.sum(booze.c.VOLUME))
stmt = stmt.where(and_(booze.c.COUNTY_NAME.like(county_name), booze.c.STORE_NAME.like(store_name)))
stmt = stmt.group_by(booze.c.STORE_NAME, booze.c.PRODUCT_NAME)
stmt = stmt.order_by(booze.c.STORE_NAME, booze.c.PRODUCT_NAME)

with eng.connect() as con:
    result = con.execute(stmt)

    if result.rowcount == 0:
        print(f"No matching records found for store '{store_name}' in county '{county_name}'.")
    else:
        print(f"Volumes of product sales matching store '{store_name}' in county '{county_name}'")
        counter = 1

        for row in result:
            print(f"  {counter}. {row.STORE_NAME} {row.PRODUCT_NAME} {row[2]:.2f} liter")
            counter += 1

eng.dispose()
