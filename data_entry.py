from datetime import datetime

date_format = "%d-%m-%Y"
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    # check if the input is a valid date
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    # try to parse the date and return it in the correct format
    try: 
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return get_date(prompt, allow_default)


def get_amount():
    pass
def get_category():
    pass
def get_description():
    pass