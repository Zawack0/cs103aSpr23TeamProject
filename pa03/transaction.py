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
        self.cat_index = -1

    def show_categories(self):
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        categories = [row[0] for row in self.cursor.fetchall()]
        result = 'Categories:\n'
        for category in categories:
            result = result + category + "\n"
        return result

    #Connor's work with Cole's bugfixes
    def add_category(self,category):
        #add a new category
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",
                            (self.cat_index,"placeholder",0,category,"none","placeholder",0,0,0))
        self.cat_index = self.cat_index - 1

    def mod_category(self,rowid,newcat):
        '''change an old category to new'''

    def add_transaction(self,item):
        #create a transaction and add it to the todo table
        self.cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?)",
                            (item["item_num"],item['item'],item['amount'],item['category'],
                             item['date'],item['description'],item['day'],item['month'],item['year']))

    def delete_transaction(self,delete_name):
        #delete a transaction item
        self.cursor.execute("DELETE FROM transactions WHERE item=(?)",(delete_name,))

    #Cole's work
    def summarize(self,method):
        #summarize transaction as specified by method'''
        if method == 1:
            self.cursor.execute("SELECT date, SUM(amount) as total_amount, \
                                COUNT(*) as total_transactions FROM transactions \
                                WHERE id >= 0 GROUP BY date")
            results = self.cursor.fetchall()
            lines = ""
            for row in results:
                date = row[0]
                total_amount = row[1]
                total_transactions = row[2]
                lines += f"Date: {date}, Total Amount: {total_amount}, \
                Total Transactions: {total_transactions}\n"
            return lines
        if method == 2:
            self.cursor.execute("SELECT year, SUM(amount) as total_amount, \
                                COUNT(*) as total_transactions FROM transactions \
                                WHERE id > 0 GROUP BY year,month")
            results = self.cursor.fetchall()
            lines = ""
            for row in results:
                year = row[0]
                month = row[1]
                total_amount = row[2]
                total_transactions = row[3]
                lines += f"Date: {month}/{year} , Total Amount: {total_amount}, \
                Total Transactions: {total_transactions}\n"
            return lines
        if method == 3:
            self.cursor.execute("SELECT year, SUM(amount) as total_amount, \
                                COUNT(*) as total_transactions FROM transactions\
                                 WHERE id > 0 GROUP BY year")
            results = self.cursor.fetchall()
            lines = ""
            for row in results:
                year = row[0]
                total_amount = row[1]
                total_transactions = row[2]
                lines += f"Year: {year}, Total Amount: {total_amount}, \
                Total Transactions: {total_transactions}\n"
            return lines
        if method == 4:
            self.cursor.execute("SELECT category, SUM(amount) as total_amount, \
                                COUNT(*) as total_transactions FROM transactions \
                                WHERE id >= 0 GROUP BY category")
            results = self.cursor.fetchall()
            lines = ""
            for row in results:
                category = row[0]
                total_amount = row[1]
                total_transactions = row[2]
                lines += f"Category: {category}, Total Amount: {total_amount}, \
                Total Transactions: {total_transactions}\n"
            return lines


    def get_menu(self):
        #returns menu
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
                10. summarize transactions by category\n'''
        return menu

    #Cole's work
    def close(self):
        #Closes the program and saves the data
        self.conn.commit()
        self.conn.close()
        self.cursor.close()

    #Cole's work
    def countTransactions(self):
        self.cursor.execute("SELECT COUNT(*) FROM transactions WHERE id >= 0")
        return self.cursor.fetchone()[0]