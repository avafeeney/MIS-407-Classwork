import csv

# Columns:
YEAR_COLUMN = 0
COUNTY_COLUMN = 1
BUSHELS_COLUMN = 2

first_county = input("Enter first county: ").upper()
second_county = input("Enter second county: ").upper()

# Dictionary of bushels for the first and second county. Year of production
# will be the key for each dictionary.
first_county_bushels_by_year = {}
second_county_bushels_by_year = {}

total = 0
with open("CornProduction-2008-2022.csv", newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    # TODO: read the file's data
    # If the row's county == first_county, store the bushels into
    # first_county_bushels_by_year[year].
    for row in reader:
        year = int(row[YEAR_COLUMN])
        county = row[COUNTY_COLUMN]
        bushels = int(row[BUSHELS_COLUMN])
        if county == first_county:
            first_county_bushels_by_year[year] = bushels
        elif county == second_county:
            second_county_bushels_by_year[year] = bushels
    # If the row's county == second_county, store the bushels into
    # second_county_bushels_by_year[year].
    ...

# After the data is read into the dictionaries, determine which years appear
# in both the first county and second county's data by intersecting the years.
years_in_both_counties = set(first_county_bushels_by_year.keys()).intersection(set(second_county_bushels_by_year.keys()))
if len(years_in_both_counties) == 0:
    print(f"No stats found in common for {first_county} and {second_county}")
else:
    print(f"Year {first_county:^18s} {second_county:^18s} Difference")
    for year in sorted(years_in_both_counties):
        first_county_bushels = first_county_bushels_by_year[year]
        second_county_bushels = second_county_bushels_by_year[year]
        difference = first_county_bushels - second_county_bushels
        print(f"{year:4} {first_county_bushels:18d} {second_county_bushels:18d} {difference:10d}")
