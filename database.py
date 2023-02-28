import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password ="root",
            database ="database_opendeurdag",
            auth_plugin='mysql_native_password'
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
            return "Succes"
        else:
            print("connection failed")
            return "Connectie mislukt, probeer opnieuw."
    except mysql.connector.Error as error:
        print(error)
        return "Probeer opnieuw, " + str(error)

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
    user_id = (name[0] + last_name[0]).lower()
    codeId = 0
    while select_user_by_user_id(user_id + str(codeId)) != None:
        codeId += 1
    return (user_id + str(codeId)).lower()

def insert_user(name: str, last_name: str, email_address: str, age_child: int, direction: str, contact: bool, phone_number: int):
    user_id = _generate_user_id(name, last_name)
    return _execute_query(
        f'INSERT INTO users (name, last_name, email_address, age_child, direction, contact, phone_number, user_id) VALUES ("{name}", "{last_name}", "{email_address}", {age_child}, "{direction}", {contact}, {phone_number}, "{user_id}")') + " for user: "+user_id

def select_user_by_user_id(user_id: str):
    return _execute_select(f'SELECT * FROM users WHERE user_id = "{user_id.lower()}"') 


#   QUESTIONS

def insert_question(question_location: str, question: str):
    _execute_query(f'INSERT INTO questions (question_location, question) VALUES ("{question_location.lower()}", "{question}")')

def select_question(question_location: str):
    return _execute_select(f'SELECT * FROM questions WHERE question_location = "{question_location.lower()}"')

def select_all_questions():
    return _execute_select(f'SELECT * FROM questions', True)

def update_question(question_location: str, question: str):
    _execute_query(f'UPDATE questions SET question="{question}" WHERE question_location="{question_location.lower()}"')

## ANSWERS

def insert_answer(question_location: str, answers: str, correct_answers: str):
    _execute_query(f'INSERT INTO answers (question_location, answers, correct_answers) VALUES ("{question_location.lower()}", "{answers}", "{correct_answers}")')

def select_answer(question_location: str):
    return _execute_select(f"SELECT * FROM answers WHERE question_location = '{question_location.lower()}'")

def update_answer(question_location: str, answers: str, correct_answers: str):
    _execute_query(f'UPDATE answers SET answers="{answers}", correct_answers="{correct_answers}" WHERE question_location="{question_location.lower()}"')

def select_all_answers():
    return _execute_select(f'SELECT * FROM answers', True)

##  ANSWERS + QUESTIONS

def insert_question_with_answer(question_location: str, question: str, answers: str, correct_answers: str):
    insert_question(question_location, question)
    insert_answer(question_location, answers, correct_answers)

def update_question_with_answer(question_location: str, question: str, answers: str, correct_answers: str):
    update_question(question_location, question)
    update_answer(question_location, answers, correct_answers)

def change_question_with_answer(question_location: str, question: str, answers: str, correct_answers: str):
    exists = _execute_select(f'SELECT * FROM questions WHERE question_location = "{question_location.lower()}"')
    if (exists):
        return update_question_with_answer(question_location.lower(), question, answers, correct_answers)
    insert_question_with_answer(question_location.lower(), question, answers, correct_answers)

def remove_question_and_answer(question_location: str):
    question_location = question_location.lower()
    _execute_query(f'DELETE FROM questions WHERE question_location= "{question_location}"')
    _execute_query(f'DELETE FROM answers WHERE question_location= "{question_location}"')


## RESULTS

def insert_result(user_id: str, question_id: str, result: int):
    user_id = user_id.lower()
    question_id = question_id.lower()
    exists = _execute_select(f'SELECT * FROM results WHERE user_id="{user_id}" AND question_id="{question_id}"')
    if (not exists):
        _execute_query(f'INSERT INTO results (user_id, question_id, result) VALUES ("{user_id}", "{question_id}", {result})')

def select_result_amount_for(user_id: str):
    user_id = user_id.lower()
    results = _execute_select(f'SELECT * FROM results WHERE user_id="{user_id}"', True)
    score = 0
    for values in results:
        score += values[3]
    return score, len(results)

if __name__ == '__main__':
    #_execute_query("DELETE FROM answers")
    print(_execute_select("SELECT * FROM users", True))
    print(_execute_select("SELECT * FROM questions", True))
    print(select_answer("6ICT"))