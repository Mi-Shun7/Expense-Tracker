import os
import pandas as pd

EXPENSE_FILE = 'expenses.csv'

def read_expense():
    if not os.path.exists(EXPENSE_FILE):
        return []  # If the file doesn't exist, return an empty list.
    
    try:
        # Read CSV file and return it as a list of dictionaries
        df = pd.read_csv(EXPENSE_FILE)
        return df.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
    except Exception as e:
        print(f"Error reading expenses: {e}")
        return []

def write_expense(expense):
    fieldnames = ['id', 'date', 'category', 'amount']
    
    expenses = read_expense()
    if expenses:
        max_id = max(expense['id'] for expense in expenses)
        expense['id'] = max_id + 1
    else:
        expense['id'] = 1

    df = pd.DataFrame([expense], columns=fieldnames)
    
    # Check if the file exists and write the header only if it's new
    file_exists = os.path.isfile(EXPENSE_FILE)
    
    try:
        df.to_csv(EXPENSE_FILE, mode='a', index=False, header=not file_exists)
        return True
    except Exception as e:
        print(f"Error writing expense: {e}")
        return False


def get_months():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for expense in read_expense():
        month = expense['date'].split('-')[1]
        month = months[int(month) - 1]
        if month not in months:
            months.append(month)
    return months