import sqlite3

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
                description TEXT
            )
        ''')

    def show_categories(self):
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        categories = [row[0] for row in self.cursor.fetchall()]
        print('Categories:')
        for category in categories:
            print(category)


