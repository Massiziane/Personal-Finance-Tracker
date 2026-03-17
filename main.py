import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            # Attempt to read the CSV file
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file does not exist, create it with the appropriate headers
            dataframe = pd.DataFrame(columns=["date", "amount", "category", "description"])
            dataframe.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    # Add a new entry to the CSV file
    def add_entry(cls, date, amount, category, description):
        # Create a dictionary representing the new entry
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # Append the new entry to the CSV file
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            # take the dictionary and write it to the CSV file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

# data collection function from the input helper functions
def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date (DD-MM-YYYY) or enter for today's date: ", 
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


# Test
add()