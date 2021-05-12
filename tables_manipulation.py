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
    cur.execute( "SELECT * FROM books  WHERE book_id = %s", (id,) )

    data = cur.fetchall()
    if data:
        print( "The following book is already present" )
        connection.commit()
        cur.close()
        return False
    else:
        cur.execute( "INSERT INTO books(book_id, author, title, status) VALUES (%s,%s,%s,%s)",
                     (id, author, title, status) )

        connection.commit()
        cur.close()

    return True


def delete_book(id):
    cursor = connection.cursor()
    try:
        cursor.execute( "DELETE FROM books WHERE book_id = %s", (id,) )
    except:
        connection.commit()
        cursor.close()
        return False
    connection.commit()
    cursor.close()

    return True


def issue_book(code, book_id):
    cursor = connection.cursor()
    try:
        cursor.execute( "INSERT INTO books_issued(issued_code, book_id) VALUES (%s,%s)", (code, book_id,) )
        cursor.execute( "UPDATE books SET status = 'issued' WHERE book_id= %s", (book_id,) )
    except:
        connection.commit()
        cursor.close()
        return False

    connection.commit()
    cursor.close()
    return True


def print_books():
    cursor = connection.cursor()
    cursor.execute( "SELECT * FROM books" )

    data = cursor.fetchall()

    cursor.close()

    return data


def return_book(id):
    cursor = connection.cursor()
    try:
        cursor.execute( "UPDATE books SET status = 'Available' WHERE book_id= %s", (id,) )
        cursor.execute( "DELETE FROM books_issued WHERE book_id = %s", (id,) )
    except:
        connection.commit()
        cursor.close()
        return False
    connection.commit()
    cursor.close()

    return True


def close_connection():
    connection.close()
    return
