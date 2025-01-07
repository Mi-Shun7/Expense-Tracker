# import sys
import argparse

# Create the top-level parser
parser = argparse.ArgumentParser(description = "Expense Tracker CLI for everyday expenses")
subparsers = parser.add_subparsers(dest='commands', help='Available commands')

# Create the parser for the "add" command
addExpense = subparsers.add_parser('add', help='Add an expense')
addExpense.add_argument('--category', required=True, help='Category of the expense')
addExpense.add_argument('--amount', required=True, type=float, help='Amount of the expense')
addExpense = parser.add_subparsers('add', help='Add an expense')

# Create the parser for the "list" command
list = parser.add_subparsers('list', help='List all expenses')

# Create the parser for the "summary" command
summaryExpense = parser.add_subparsers('summary', help='Summary of all expenses')
summaryExpense.add_argument('--month', choices=range(1,13), type=int, help='Display the summary for a specific month(1-12)')

# create the parser for the "export" command
export = parser.add_subparsers('export', help='Export expenses to a CSV file')
export.add_argument('--file', required=True, help='Export expenses to a CSV file')

# Create the parser for the "delete" command
deleteExpense = parser.add_subparsers('delete', help='Delete an expense')
deleteExpense.add_argument('--month', required=True, help='Delete expense for a specific month')
deleteExpense.add_argument('--category', help='Delete expense for a specific category')

# Parse the arguments
args = parser.parse_args()

#  Process the selected operation 
if args.commands == 'add':
    result = addExpense(args.description, args.amount)
    # print(result)

elif args.commands == 'list':
    result = list()
    # print(result)

elif args.commands == 'summary':
    result = summaryExpense()
    # print(result)

elif args.commands == 'delete':
    result = deleteExpense(args.description, args.amount)

print(result)
