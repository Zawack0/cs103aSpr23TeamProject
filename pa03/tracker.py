'''
tracker.py interacts with user, offering a menu of possible
actions that users can choose to keep track of a database of financial
transactions. Makes calls to transaction class to update database
'''
from transaction import Transaction
#analagous to todo2.py
#no sql calls



def print_menu():
    '''
    print_menu is a fairly self explanatory method that provides user with the options
    directly to console. Note that as per instructed, modify category was not implemented.
    '''
    print('0. quit')
    print('1. show categories')
    print('2. add category')
    print('3. modify category')
    print('4. show transactions')
    print('5. add transaction')
    print('6. delete transaction')
    print('7. summarize transactions by date')
    print('8. summarize transactions by month')
    print('9. summarize transactions by year')
    print('10. summarize transactions by category')
    print('11. print this menu')


def get_menu_choice():
    '''
    get_menu_choice provides user with menu, then returns a valid
    user input (0-11). Will continue to prompt for input until input
    is valid.
    '''
    choice = input('Enter your choice: ')
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 11:
        print('Invalid choice!')
        choice = input('Enter your choice: ')
    return int(choice)


def get_text_arg(argname):
    '''
    prompts user for console input based on argname.
    returns input provided as a string.
    '''
    choice = input("Enter " + argname + ": ")
    return str(choice)


def get_num_arg(argname):
    '''
    prompts user for console input based on argname.
    continues to prompt user for input until the choice is
    valid (a number), then returns input as an integer.
    '''
    choice = input("Enter " + argname + ": ")
    while not choice.isdigit():
        print("Invalid choice!")
        choice = input("Enter " + argname + ": ")
    return int(choice)


def get_date_arg():
    '''
    prompts user for console input for a date in m/d/y format.
    Does so by calling get num arg for day, month, and year.
    returns date as string.
    '''
    month = str(get_num_arg("month"))
    day = str(get_num_arg("day"))
    year = str(get_num_arg("year"))
    seperator = "/"
    return month+seperator+day+seperator+year


def main():
    '''
    the loop that describes app behavior. when called,
    the app will prompt the user for a choice, and additional
    arguments if needed, make necessary calls to transaction.py,
    and prints any necessary output.
    '''
    filename = input('Enter database filename: ')
    transaction = Transaction(filename)
    print_menu()
    choice = get_menu_choice()
    while choice != 0:
        if choice == 1:
            transaction.show_categories()
        elif choice == 2:
            category = get_text_arg("new category name")
            transaction.add_category(category)
        elif choice == 3:
            pass # implement modify category
        elif choice == 4:
            transaction.summarize(1)
        elif choice == 5:
            item_num = get_num_arg("new transaction num")
            name = get_text_arg("new transaction name")
            amount = get_num_arg("new transaction amount")
            category = get_text_arg("new transaction category")
            date = get_date_arg()
            helper = date.split('/')
            day = int(helper[0])
            month = int(helper[1])
            year = int(helper[2])
            desc = get_text_arg("new transaction description")
            new_transaction = {'item_num':item_num,'item':name,
                               'amount':amount, 'category':category,
                               'date':date, 'description':desc, 'day':day,
                               'month':month, 'year':year}
            transaction.add_transaction(new_transaction)
            # implement add transaction
        elif choice == 6:
            delete_name = get_text_arg("name of transaction to be deleted")
            transaction.delete_transaction(delete_name)
        elif choice == 7:
            transaction.summarize(1)
        elif choice == 8:
            transaction.summarize(2)
            # implement summarize transactions by month
        elif choice == 9:
            transaction.summarize(3)
            # implement summarize transactions by year
        elif choice == 10:
            print(transaction.summarize(4))
        elif choice == 11:
            print_menu()
        choice = get_menu_choice()
    transaction.close()

if __name__ == '__main__':
    main()
