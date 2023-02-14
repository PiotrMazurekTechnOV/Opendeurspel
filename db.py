import mysql.connector


def connect_to_db():
    try:
        mydb = mysql.connector.connect( 
            host="sql7.freemysqlhosting.net",
            user= "sql7597227",
            password="7x9Ssuvhlq",
            database="sql7597227")

        cursor = mydb.cursor(buffered=True)
        return mydb, cursor
    except mysql.connector.Error as error:
        print(error)

def _execute_query(query):
    try:
        mydb, cursor = connect_to_db()
        if(mydb and cursor):
            cursor.execute(query)
            mydb.commit()
            cursor.close()
            mydb.close()
        else:
            print("connection failed")
    except mysql.connector.Error as error:
        print(error)

def _execute_select(query, many = False):
    try:
        mydb, cursor = connect_to_db()
        if(mydb and cursor):
            cursor.execute(query)
            if(many):
                records = cursor.fetchall()
            else:
                records = cursor.fetchone()
            cursor.close()
            mydb.close()
            return records
        else:
            print("connection failed")
    except mysql.connector.Error as error:
        print(error)    


def insert_user():
    _execute_query("")


def select_user_by_code(code):
    user = _execute_select("")
    return user


def insert_question():
    _execute_query("")








