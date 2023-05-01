from transaction import Transaction
import unittest

class transtests(unittest.TestCase):
    def test_add_transaction(self):
        t = Transaction('test.db')
        t.add_transaction(1, 100, 'groceries', '2022-04-16', 'shopping at Walmart')

    def test_add_category():
        '''TODO'''

    def test_delete_transaction():
        '''TODO'''

    def test_delete_category():
        '''TODO'''

    def test_add_category():
        '''TODO'''

    def test_mod_category():
        '''TODO'''

    def test_mod_transaction():
        '''TODO'''

if __name__ == '__main__':
    unittest.main()