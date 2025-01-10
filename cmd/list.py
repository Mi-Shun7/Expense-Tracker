import pandas as pd 

def listExpense():
    # List all expenses
    try:
        with open('expenses.csv', 'r') as file:
            # expenses = file.readlines()
            expenses = pd.read_csv(file)
            if len(expenses) == 0:
                return "No expenses found."
            else:
                return expenses
    except FileNotFoundError:
        return "No expenses found."

