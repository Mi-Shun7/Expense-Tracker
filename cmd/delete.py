from .utils import read_expense, write_expense
import pandas as pd

def deleteExpense(expense_id):
    # Convert expense_id to integer if it’s passed as a string
    expense_id = int(expense_id)
    
    # Read all expenses
    expenses = read_expense()
    
    # Find and remove the matching expense
    updated_expenses = [expense for expense in expenses if expense['id'] != expense_id]
    
    if len(updated_expenses) == len(expenses):  # No expense was removed
        return False
    
    # Overwrite the file with updated expenses
    df = pd.DataFrame(updated_expenses)
    try:
        df.to_csv('expenses.csv', index=False)  # Overwrite the file
        return True
    except Exception as e:
        print(f"Error writing updated expenses: {e}")
        return False
    

