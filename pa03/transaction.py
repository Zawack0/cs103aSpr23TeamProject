import sqlite3
#analagous to todolist.py
#no printing

class Transaction:
    catIndex = -1
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

    '''Connor's work with Cole's bugfixes'''
    def add_category(self,category):
        '''add a new category'''
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",(catIndex,"placeholder",0,category,"none","placeholder",0,0,0))
        catIndex = catIndex - 1

    def mod_category(self,rowid,newcat):
        '''change an old category to new'''

    
    def add_transaction(self,item):
        ''' create a transaction and add it to the todo table '''
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",(item["item_num"],item['item'],item['amount'],item['category'],item['date'],item['description'],item['day'],item['month'],item['year']))

    def delete_transaction(self,delete_name):
        ''' delete a transaction item '''
        self.cursor.execute("DELETE FROM transactions WHERE item=(?)",(delete_name,))

    '''Cole's work'''
    def summarize(self,method):
        '''summarize transaction as specified by method'''
        if method == 1:
            pass # TODO: implement summarize by date
        if method == 2:
           pass # TODO: implement summarize by month
        if method == 3:
           pass # TODO: implement summarize by year
        if method == 4:
            self.cursor.execute("SELECT category, SUM(amount) as total_amount, COUNT(*) as total_transactions FROM transactions WHERE id > 0 GROUP BY category")
            results = self.cursor.fetchall()
            lines = ""
            for row in results:
                category = row[0]
                total_amount = row[1]
                total_transactions = row[2]
                lines += f"Category: {category}, Total Amount: {total_amount}, Total Transactions: {total_transactions}\n"
            return lines
            

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
    
    '''Cole's work'''
    def close(self):
        '''Closes the program and saves the data'''
        self.conn.commit()
        self.conn.close()
        self.cursor.close()