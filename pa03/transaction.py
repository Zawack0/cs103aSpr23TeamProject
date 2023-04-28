import sqlite3
#analagous to todolist.py
#no printing

class Transaction:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                item TEXT,
                amount REAL,
                category TEXT,
                date TEXT,
                description TEXT,
                day INTEGER,
                month INTEGER,
                year INTEGER)''')

    def show_categories(self):
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        categories = [row[0] for row in self.cursor.fetchall()]
        print('Categories:')
        for category in categories:
            print(category)

    def add_category(self,category):
        '''add a new category'''
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",(0,"placeholder",0,category,"none","placeholder",0,0,0))

    def mod_category(self,rowid,newcat):
        '''change an old category to new'''

    
    def add_transaction(self,item):
        ''' create a transaction and add it to the todo table '''
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",(item["item_num"],item['item'],item['amount'],item['category'],item['date'],item['description'],item['day'],item['month'],item['year']))

    def delete_transaction(self,delete_name):
        ''' delete a transaction item '''
        self.cursor.execute("DELETE FROM transactions WHERE item=(?)",(delete_name,))

    def summarize(self,method):
        '''summarize transaction as specified by method'''
        if method == 1:
            pass # TODO: implement summarize by date
        if method == 2:
           pass # TODO: implement summarize by month
        if method == 3:
           pass # TODO: implement summarize by year
        if method == 4:
            pass # TODO: implement summarize by category

    def get_menu(self):
        '''returns menu'''
        menu = '''0. quit
                1. show categories
                2. add category
                3. modify category
                4. show transactions
                5. add transaction
                6. delete transaction
                7. summarize transactions by date
                8. summarize transactions by month
                9. summarize transactions by year
                10. summarize transactions by category'''
        return menu

    


