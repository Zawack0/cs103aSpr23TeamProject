from transaction import Transaction

def test_add_transaction():
    t = Transaction('test.db')
    t.add_transaction(1, 100, 'groceries', '2022-04-16', 'shopping at Walmart')
    assert t.get_transaction(1) == (1, 100, 'groceries', '2022-04-16', 'shopping at Walmart')

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
