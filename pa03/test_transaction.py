'''Cole wrote the framework for all of these tests'''

from transaction import Transaction
import unittest

class transtests(unittest.TestCase):
    '''Cole's work'''
    def test_add_transaction(self):
        t = Transaction('test.db')
        result = t.countTransactions()
        assert result == 0
        t.add_transaction({'item_num':50,'item':'groceries',
                               'amount':50, 'category':'shopping',
                               'date':'2022-04-16', 'description':'shopping at Walmart', 'day':16,
                               'month':4, 'year':2022})
        result = t.countTransactions()
        assert result == 1        
    '''Cole's work'''
    def test_add_category(self):
        t = Transaction('test.db')
        t.add_category('bees')
        assert t.show_categories == "Categories:\nbees\n"
        

    def test_delete_transaction(self):
        '''Todo'''

    def test_mod_category(self):
        '''Todo'''

    def test_mod_transaction(self):
        '''Todo'''

if __name__ == '__main__':
    unittest.main()