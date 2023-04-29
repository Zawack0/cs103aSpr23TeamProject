from transaction import Transaction
#analagous to todo2.py
#no sql calls

def print_menu():
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
    choice = input('Enter your choice: ')
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 11:
        print('Invalid choice!')
        choice = input('Enter your choice: ')
    return int(choice)

def get_text_arg(argname):
    choice = input("Enter " + argname + ": ")
    return str(choice)

def get_num_arg(argname):
    choice = input("Enter " + argname + ": ")
    while not choice.isdigit():
        print("Invalid choice!")
        choice = input("Enter " + argname + ": ")
    return int(choice)

def get_date_arg():
    '''prompt user for mm/dd/yyyy formatted date'''
    month = str(get_num_arg("month"))
    day = str(get_num_arg("day"))
    year = str(get_num_arg("year"))
    seperator = "/"
    return(month+seperator+day+seperator+year)


def main():
    filename = input('Enter database filename: ')
    transaction = Transaction(filename)
    print_menu()
    choice = get_menu_choice()
    while choice != 0:
        if choice == 1:
            pass # TODO: implement show categories
        elif choice == 2:
            pass # TODO: implement add category
        elif choice == 3:
            pass # TODO: implement modify category
        elif choice == 4:
            pass # TODO: implement show transactions
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
            new_transaction = {'item_num':item_num,'item':name, 'amount':amount, 'category':category, 'date':date, 'description':desc, 'day':day, 'month':month, 'year':year}
            transaction.add_transaction(new_transaction)
            pass # TODO: implement add transaction
        elif choice == 6:
            delete_name = get_text_arg("name of transaction to be deleted")
            transaction.delete_transaction(delete_name)
        elif choice == 7:
            pass # TODO: implement summarize transactions by date
        elif choice == 8:
            pass # TODO: implement summarize transactions by month
        elif choice == 9:
            pass # TODO: implement summarize transactions by year
        elif choice == 10:
            pass # TODO: implement summarize transactions by category
        elif choice == 11:
            print_menu()
        choice = get_menu_choice()

if __name__ == '__main__':
    main()
