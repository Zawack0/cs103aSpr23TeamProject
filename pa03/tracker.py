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
            pass # TODO: implement add transaction
        elif choice == 6:
            pass # TODO: implement delete transaction
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
