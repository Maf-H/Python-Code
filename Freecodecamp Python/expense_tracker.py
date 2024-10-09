def add_expense(expenses, amount, category):
    """ 
    Add an expense to the list of expenses.

    Parameters:
    expenses (list): List of expenses. Each expense is a dictionary with keys 'amount' and 'category'.
    amount (float): Amount of the expense.
    category (str): Category of the expense.
    """
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    """
    Print each expense in the given list of expenses.
    
    Parameters:
    expenses (list): List of expenses. Each expense is a dictionary with keys 'amount' and 'category'.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calculate the total of all expenses in the given list.

    Parameters:
    expenses (list): List of expenses. Each expense is a dictionary with keys 'amount' and 'category'.

    Returns:
    float: The total of all expenses.
    """
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filter a list of expenses to only include those of a given category.

    Parameters:
    expenses (list): List of expenses. Each expense is a dictionary with keys 'amount' and 'category'.
    category (str): Category to filter by.

    Returns:
    iter: An iterator over the filtered list of expenses.
    """
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    """
    Main function for the Expense Tracker program.

    This program provides a simple expense tracker application. It provides the following features:
    - Add an expense: The user can add an expense with an amount and a category.
    - List all expenses: The program will print out all the expenses added by the user.
    - Show total expenses: The program will print out the total of all the expenses added by the user.
    - Filter expenses by category: The program will filter the expenses by category and print out the expenses for the given category.
    - Exit: The user can exit the program.

    The program will keep running until the user chooses to exit.
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()
