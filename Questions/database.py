import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="192.168.125.2",
            user="opendeur",
            password ="opendeur",
            database ="opendeurspel",
            auth_plugin='mysql_native_password'
        )
    

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


#   USERS


def _generate_user_code(name, last_name):
    code = name[0] + last_name[0]
    codeId = 0
    while select_user_by_code(code + str(codeId)) != None:
        codeId += 1
    return code + str(codeId)

def insert_user(name, last_name, email_address, email_child, age_child, direction, contact, phone_number):
    code = _generate_user_code(name, last_name)
    _execute_query(
        f'INSERT INTO users (name, last_name, email_address, email_child, age_child, direction, contact, phone_number, code) VALUES ("{name}", "{last_name}", "{email_address}", "{email_child}", {age_child}, "{direction}", {contact}, {phone_number}, "{code}")')

def select_user_by_code(code):
    user = _execute_select(f'SELECT * FROM users WHERE code = "{code}"')
    return user


#   QUESTIONS

'''
Testing
'''
def insert_question(question_location, question, question_type, answers, correct_answers):
    _execute_query(f'INSERT INTO questions (question_location, question, question_type) VALUES ("{question_location}", "{question}", {question_type})')
    insert_answer(question_location, answers, correct_answers)

def select_question(question_location):
    return _execute_select(f'SELECT * FROM questions WHERE question_location = "{question_location}"')

## ANSWERS

def insert_answer(question_location, answers, correct_answers):
    _execute_query(f'INSERT INTO answers (question_location, answers, correct_answers) VALUES ("{question_location}", "{answers}", "{correct_answers}")')

def select_answer(question_location):
    return _execute_select(f"SELECT * FROM answers WHERE question_location = '{question_location}'")

## RESULTS
