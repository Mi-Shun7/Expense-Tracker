# import sys
import argparse
from cmd.add import addExpense
from cmd.list import listExpense
from cmd.summary import summary
from cmd.delete import deleteExpense

# Create the top-level parser
parser = argparse.ArgumentParser(description = "Expense Tracker CLI for everyday expenses")
subparsers = parser.add_subparsers(dest='commands', help='Available commands')

# Create the parser for the "add" command
add_parser = subparsers.add_parser('add', help='Add an expense')
add_parser.add_argument('--category', required=True, help='Category of the expense')
add_parser.add_argument('--amount', required=True, type=float, help='Amount of the expense')

# Create the parser for the "list" command
list = subparsers.add_parser('list', help='List all expenses')

# Create the parser for the "summary" command
summary_parser = subparsers.add_parser('summary', help='Summary of all expenses')
# summary_parser.add_argument('--month', choices=range(1,13), type=int, help='Display the summary for a specific month(1-12)')
# summary_parser.add_argument('--category', help='Display the summary for a specific category')

# Create the parser for the "delete" command
delete_parser = subparsers.add_parser('delete', help='Delete an expense')
delete_parser.add_argument('--month', required=True, help='Delete expense for a specific month')
delete_parser.add_argument('--category', help='Delete expense for a specific category')
delete_parser.add_argument('--id', help='Delete expense by ID')
# Parse the arguments
args = parser.parse_args()

#  Process the selected operation 
if args.commands == 'add':
    result = addExpense(args.category, args.amount)
    
   
elif args.commands == 'list':
    result = listExpense()

elif args.commands == 'summary':
    result = summary()
   
elif args.commands == 'delete':
    result = deleteExpense(args.id)
 
print(result)