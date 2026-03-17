import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = 'finance_data.csv'

    @classmethod
    # Initialize the CSV file
    def initialize_csv(cls):
        try:
            # Attempt to read the CSV file
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file does not exist, create it with the appropriate headers
            dataframe = pd.DataFrame(columns=["date", "amount", "category", "description"])
            dataframe.to_csv(cls.CSV_FILE, index=False)

CSV.initialize_csv()