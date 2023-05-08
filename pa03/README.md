Basic financial transaction app that uses sqlite database to keep track of a user's financial transactions.

Connor's Tracker.py log:
PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 tracker.py
Enter database filename: asdf
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
Enter your choice: hi there
Invalid choice!
Enter your choice: 7
Enter your choice: 1
Categories:
Enter your choice: 2
Enter new category name: food
Enter your choice: 2
Enter new category name: books
Enter your choice: 1
Categories:
books
food
Enter your choice: 5
Enter new transaction num: 2
Enter new transaction name: chipotle
Enter new transaction amount: 24
Enter new transaction category: food
Enter month: 05
Enter day: 02
Enter year: 2023
Enter new transaction description: burrito, chips, and drink
Enter your choice: 1
Categories:
books
food
Enter your choice: 10
Category: food, Total Amount: 24.0, Total Transactions: 1

Enter your choice: 0

pylint logs:
------------------------------------------------------------------
Your code has been rated at 8.72/10 (previous run: 9.25/10, -0.53)

PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 -m pylint tracker.py
************* Module tracker
tracker.py:65:0: W0105: String statement has no effect (pointless-string-statement)
tracker.py:82:0: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 9.76/10 (previous run: 8.72/10, +1.04)

PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 -m pylint tracker.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.76/10, +0.24)


PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 -m pylint transaction.py
************* Module transaction
transaction.py:32:0: C0301: Line too long (149/100) (line-too-long)
transaction.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:41:0: C0301: Line too long (217/100) (line-too-long)
transaction.py:51:0: C0301: Line too long (163/100) (line-too-long)
transaction.py:60:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:63:0: C0301: Line too long (158/100) (line-too-long)
transaction.py:71:0: C0301: Line too long (123/100) (line-too-long)
transaction.py:74:0: C0301: Line too long (152/100) (line-too-long)
transaction.py:81:0: C0301: Line too long (114/100) (line-too-long)
transaction.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:85:0: C0301: Line too long (161/100) (line-too-long)
transaction.py:92:0: C0301: Line too long (122/100) (line-too-long)
transaction.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:110:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:116:0: C0304: Final newline missing (missing-final-newline)
transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transaction.py:5:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:20:8: C0103: Attribute name "catIndex" doesn't conform to snake_case naming style (invalid-name)
transaction.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:29:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:47:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:48:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
transaction.py:111:4: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 6.93/10 (previous run: 7.97/10, -1.04)

PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 -m pylint transaction.py
************* Module transaction
transaction.py:32:0: C0301: Line too long (149/100) (line-too-long)
transaction.py:40:0: C0301: Line too long (217/100) (line-too-long)
transaction.py:50:0: C0301: Line too long (163/100) (line-too-long)
transaction.py:59:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:62:0: C0301: Line too long (158/100) (line-too-long)
transaction.py:70:0: C0301: Line too long (123/100) (line-too-long)
transaction.py:73:0: C0301: Line too long (152/100) (line-too-long)
transaction.py:80:0: C0301: Line too long (114/100) (line-too-long)
transaction.py:82:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:84:0: C0301: Line too long (161/100) (line-too-long)
transaction.py:91:0: C0301: Line too long (122/100) (line-too-long)
transaction.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:109:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:115:0: C0304: Final newline missing (missing-final-newline)
transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transaction.py:5:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:20:8: C0103: Attribute name "catIndex" doesn't conform to snake_case naming style (invalid-name)
transaction.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:29:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:46:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:47:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
transaction.py:110:4: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 7.07/10 (previous run: 6.93/10, +0.13)

PS C:\Users\zawac\OneDrive\Desktop\Classes\SE\cs103aSpr23TeamProject\pa03> python3 -m pylint transaction.py
************* Module transaction
transaction.py:32:0: C0301: Line too long (149/100) (line-too-long)
transaction.py:40:0: C0301: Line too long (217/100) (line-too-long)
transaction.py:50:0: C0301: Line too long (163/100) (line-too-long)
transaction.py:59:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:62:0: C0301: Line too long (158/100) (line-too-long)
transaction.py:70:0: C0301: Line too long (123/100) (line-too-long)
transaction.py:73:0: C0301: Line too long (152/100) (line-too-long)
transaction.py:80:0: C0301: Line too long (114/100) (line-too-long)
transaction.py:83:0: C0301: Line too long (161/100) (line-too-long)
transaction.py:73:0: C0301: Line too long (152/100) (line-too-long)
transaction.py:80:0: C0301: Line too long (114/100) (line-too-long)
transaction.py:83:0: C0301: Line too long (161/100) (line-too-long)
transaction.py:90:0: C0301: Line too long (122/100) (line-too-long)
transaction.py:114:0: C0304: Final newline missing (missing-final-newline)
transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transaction.py:5:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:20:8: C0103: Attribute name "catIndex" doesn't conform to snake_case naming style (invalid-name)
transaction.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:29:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:46:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:47:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
transaction.py:109:4: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 7.47/10 (previous run: 5.33/10, +2.13)

TO BE CONTINUED


Cole's Logs 

Transcript

PS C:\Users\coles\OneDrive\Documents\GitHub\cs103aSpr23TeamProject\pa03> & C:/Users/coles/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/coles/OneDrive/Documents/GitHub/cs103aSpr23TeamProject/pa03/tracker.py
Enter database filename: skks
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
Enter your choice: 10

Enter your choice: 5
Enter new transaction num: 10
Enter new transaction name: dkjdf
Enter new transaction amount: 3
Enter new transaction category: dogs
Enter month: 2
Enter day: 3
Enter year: 494
Enter new transaction description: dkjf
Enter your choice: 5
Enter new transaction num: 23
Enter new transaction name: fjkjfd
Enter new transaction amount: 33
Enter new transaction category: cats 
Enter month: 23
Enter day: 4
Enter year: 494
Enter new transaction description: kdfjf
Enter your choice: 5
Enter new transaction num: 234
Enter new transaction name: bee
Enter new transaction amount: 43
Enter new transaction category: dogs
Enter month: 2
Enter day: 494
Enter year: 494
Enter new transaction description: sdkjf
Enter your choice: 10
Category: cats, Total Amount: 33.0,                 Total Transactions: 1
Category: dogs, Total Amount: 46.0,                 Total Transactions: 2

Enter your choice: 9
Year: 494, Total Amount: 79.0,                 Total Transactions: 3

Enter your choice: 7
Date: 2/3/494, Total Amount: 3.0,                 Total Transactions: 1
Date: 2/494/494, Total Amount: 43.0,                 Total Transactions: 1
Date: 23/4/494, Total Amount: 33.0,                 Total Transactions: 1

PYLINT

PS C:\Users\coles\OneDrive\Documents\GitHub\cs103aSpr23TeamProject\pa03> python3 -m pylint transaction.py
************* Module transaction
transaction.py:44:0: C0301: Line too long (102/100) (line-too-long)
transaction.py:133:0: C0304: Final newline missing (missing-final-newline)
transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transaction.py:5:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:40:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:51:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:51:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
transaction.py:108:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:124:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:131:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:131:4: C0103: Method name "countTransactions" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 8.11/10 (previous run: 7.44/10, +0.67)

PS C:\Users\coles\OneDrive\Documents\GitHub\cs103aSpr23TeamProject\pa03> python3 -m pylint tracker.py        

------------------------------------
Your code has been rated at 10.00/10

PYTEST

PS C:\Users\coles\OneDrive\Documents\GitHub\cs103aSpr23TeamProject\pa03> & C:/Users/coles/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/coles/OneDrive/Documents/GitHub/cs103aSpr23TeamProject/pa03/test_transaction.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.016s

OK