import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            #host="192.168.125.2",
            #user="opendeur",
            #password ="opendeur",
            #database ="opendeurspel",
            host="sql7.freemysqlhosting.net",
            user="sql7597227",
            password="7x9Ssuvhlq",
            database="sql7597227"
            )
    
        cursor = mydb.cursor(buffered=True)
        return mydb, cursor
    except mysql.connector.Error as error:
        print(error)

def _execute_query(query: str):
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

def _execute_select(query: str, many = False):
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

def _generate_user_id(name, last_name):
    user_id = name[0] + last_name[0]
    codeId = 0
    while select_user_by_user_id(user_id + str(codeId)) != None:
        codeId += 1
    return user_id + str(codeId)

def insert_user(name: str, last_name: str, email_address: str, email_child: str, age_child: int, direction: str, contact: bool, phone_number: int):
    user_id = _generate_user_id(name, last_name)
    _execute_query(
        f'INSERT INTO users (name, last_name, email_address, email_child, age_child, direction, contact, phone_number, user_id) VALUES ("{name}", "{last_name}", "{email_address}", "{email_child}", {age_child}, "{direction}", {contact}, {phone_number}, "{user_id}")')

def select_user_by_user_id(user_id: str):
    user = _execute_select(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    return user


#   QUESTIONS

def insert_question(question_location: str, question: str, question_type: int):
    _execute_query(f'INSERT INTO questions (question_location, question, question_type) VALUES ("{question_location}", "{question}", {question_type})')

def select_question(question_location: str):
    return _execute_select(f'SELECT * FROM questions WHERE question_location = "{question_location}"')

def select_all_questions():
    return _execute_select(f'SELECT * FROM questions', True)

def update_question(question_location: str, question: str, question_type : int):
    _execute_query(f'UPDATE questions SET question="{question}", question_type="{question_type}" WHERE question_location="{question_location}"')

## ANSWERS

def insert_answer(question_location: str, answers: str, correct_answers: str):
    _execute_query(f'INSERT INTO answers (question_location, answers, correct_answers) VALUES ("{question_location}", "{answers}", "{correct_answers}")')

def select_answer(question_location: str):
    return _execute_select(f"SELECT * FROM answers WHERE question_location = '{question_location}'")

def update_answer(question_location: str, answers: str, correct_answers: str):
    _execute_query(f'UPDATE answers SET answers="{answers}", correct_answers="{correct_answers}" WHERE question_location="{question_location}"')

def select_all_answers():
    return _execute_select(f'SELECT * FROM answers', True)

##  ANSWERS + QUESTIONS

def insert_question_with_answer(question_location: str, question: str, question_type: int, answers: str, correct_answers: str):
    insert_question(question_location, question, question_type)
    insert_answer(question_location, answers, correct_answers)

def update_question_with_answer(question_location: str, question: str, question_type: int, answers: str, correct_answers: str):
    update_question(question_location, question, question_type)
    update_answer(question_location, answers, correct_answers)

def change_question_with_answer(question_location: str, question: str, question_type: int, answers: str, correct_answers: str):
    exists = _execute_select(f'SELECT * FROM questions WHERE question_location = "{question_location}"')
    if (exists):
        return update_question_with_answer(question_location, question, question_type, answers, correct_answers)
    insert_question_with_answer(question_location, question, question_type, answers, correct_answers)

def remove_question_and_answer(question_location: str):
    _execute_query(f'DELETE FROM questions WHERE question_location= "{question_location}"')
    _execute_query(f'DELETE FROM answers WHERE question_location= "{question_location}"')


## RESULTS

def insert_result(user_id: str, question_id: str, result: int):
    exists = _execute_select(f'SELECT * FROM results WHERE user_id="{user_id}" AND question_id="{question_id}"')
    if (not exists):
        _execute_query(f'INSERT INTO results (user_id, question_id, result) VALUES ("{user_id}", "{question_id}", {result})')

def select_result_amount_for(user_id: str):
    results = _execute_select(f'SELECT * FROM results WHERE user_id="{user_id}"', True)
    score = 0
    for values in results:
        score += values[3]
    return score, len(results)

if __name__ == '__main__':
    #_execute_query("DELETE FROM answers")
    pass