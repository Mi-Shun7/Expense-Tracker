from .utils import read_expense

def categorySummary(category):
    categoryExpense = sum(expense['amount'] for expense in read_expense() if expense['description'] == category)
    print(f"Total expenses for {category}: ${categoryExpense}")

def monthlySummary(month):
    monthlyExpense = sum(expense['amount'] for expense in read_expense() if expense['date'].split('-')[1] == month)
    print(f"Total expenses for {month}: ${monthlyExpense}")

def yearlySummary(year):
    yearlyExpense = sum(expense['amount'] for expense in read_expense() if expense['date'].split('-')[0] == year)
    print(f"Total expenses for {year}: ${yearlyExpense}")

def allTimeSummary():
    summaryExpense = sum(expense['amount'] for expense in read_expense())
    print(f"Total expenses: ${summaryExpense}")


def summary():
    fieldname = input("Enter fieldname to summarize by (year/month/category/all): ").strip().lower()
    
    match fieldname:
        case 'month':
            month = input("Enter month (MM): ").strip()
            monthlySummary(month)
        case 'category':
            category = input("Enter category: ").strip()
            categorySummary(category)
        case 'year':
            year = input("Enter year: ").strip()
            yearlySummary(year)
        case 'all':
            allTimeSummary()
        case _:
            print("Invalid selection. Please enter 'year', month', 'category', or 'all'.")
