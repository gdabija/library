import tables_manipulation as db
from design_backround import *


db.connect_database()
#db.add_book(102, 'Steven Pinker', 'Blank State', 'Available')
# db.add_book(103, 'Steven Pinker', 'Blank State', 'Available')
# db.add_book(104, 'Steven Pinker', 'Blank State', 'Available')
#db.delete_book(102)
#db.issue_book(10,101)
db.print_available_books()
db.print_issued_books()
db.close_connection()

