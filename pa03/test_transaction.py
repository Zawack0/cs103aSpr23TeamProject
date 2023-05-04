from transaction import Transaction
import unittest

class transtests(unittest.TestCase):
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

    def test_add_category():
        t = Transaction('test.db')
        t.add_category('bees')
        

    def test_delete_transaction():
        return True

    def test_delete_category():
        return True

    def test_add_category():
        return True

    def test_mod_category():
        return True

    def test_mod_transaction():
        return True

if __name__ == '__main__':
    unittest.main()