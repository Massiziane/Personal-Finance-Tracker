import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

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

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # Convert the date column to datetime format for filtering
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        # Filter the DataFrame based on the date range
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the specified date range.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:"
                )
            print(
                filtered_df.to_string(
                    index=False, formatters={'date': lambda x: x.strftime(CSV.FORMAT)}
                    )
                )
            
            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expense = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df


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
CSV.get_transactions("01-08-2023", "17-03-2026")
add()