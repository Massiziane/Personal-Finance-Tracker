import pandas as pd
import csv
from datetime import datetime

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

#tests
CSV.initialize_csv()
CSV.add_entry("2023-08-01", 1000, "Salary", "Monthly salary")