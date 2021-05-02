import psycopg2
list_id = []
def connect_database():

    global connection
    DB_NAME = "db_books"
    DB_USER = "postgres"
    DB_PASSWORD = "1234"

    try:
        connection = psycopg2.connect( dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD )
        print( "Database connected successful" )
    except:
        print( "Could not connect to the database" )

    cur = connection.cursor()

    cur.execute( "CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY, author VARCHAR, title VARCHAR, "
                 "status VARCHAR)" )
    cur.execute( "CREATE TABLE IF NOT EXISTS books_issued(issued_code INT PRIMARY KEY, book_id INT REFERENCES "
                 "books(book_id))" )

    connection.commit()
    cur.close()
    return


def add_book(id, author, title, status):

    cur = connection.cursor()
    #cur.execute("SELECT * FROM books WHERE id = %s",(id))

    try:
        cur.execute( "INSERT INTO books(book_id, author, title, status) VALUES (%s,%s,%s,%s)", (id, author, title, status) )
    except:
        print("the id is already present")
    connection.commit()
    cur.close()

    return


def delete_book(id):
    cursor = connection.cursor()
    cursor.execute( "DELETE FROM books WHERE book_id = %s", (id,))

    connection.commit()
    cursor.close()

    return


def issue_book(id, book_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books_issued(issued_code, book_id) VALUES (%s,%s)",(id, book_id,))
    cursor.execute("UPDATE books SET status = 'issued' WHERE book_id= %s", (book_id,))

    connection.commit()
    cursor.close()
    return

def print_available_books():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books  WHERE status = 'Available'")

    data = cursor.fetchall()


    cursor.close()
    print("Available books:")
    for row in data:
        print(row)

    return

def print_issued_books():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books  WHERE status = 'issued'")

    data = cursor.fetchall()


    cursor.close()
    print("Issued books:")
    for row in data:

        print(row)

    return
def return_book(id):
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET status = 'Available' WHERE book_id= %s", (id,))

    connection.commit()
    cursor.close()

    return


def close_connection():

    connection.close()
    return
