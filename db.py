import mysql.connector


def connect_to_db():

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="opendeur",
            password ="opendeur",
            database ="opendeurspel"
        )

        cursor = mydb.cursor()
        return mydb, cursor
    except mysql.connector.Error as error:
        print(error)

def _execute(query):
    try:
        mydb, cursor = connect_to_db()
        if(mydb and cursor):
            cursor.execute(query)
            mydb.commit()
            cursor.close()
        else:
            print("connection failed")
    except mysql.connector.Error as error:
        print(error)


