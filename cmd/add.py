import datetime
from .utils import write_expense, read_expense

expense_id = len(read_expense()) + 1

def addExpense(category, amount):
    # Add the expense to the list
    if amount <= 0:
        raise ValueError("Amount cannot be zero or negative")
        # return 
    
    amount = round(float(amount), 3)
    try:
        if amount: 
            write_expense(
                {
                'id': expense_id,
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'description': category,
                'amount': amount,
                })
        
    except ValueError as e:
        print(e)
        return
    
    return f"Expense added successfully. ID: {expense_id}"
