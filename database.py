import mysql.connector



remote_connect = mysql.connector.connect(
  host="127.0.0.1",
  user= "",
  passwd="",
  database="database_opendeurdag",)

#remote_connect = mysql.connector.connect(
 # host="192.168.125.2",
 # user= "opendeur",
 # passwd="opendeur",
 # database="database_opendeurdag",)

my_conn = remote_connect .cursor(buffered=True)


def my_connect_database_opendeurdag():
  return remote_connect;

def my_conn_database_opendeurdag():
 return remote_connect;


def better_string(string):
  string = str(string).replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace('{', '').replace('}',
                                                                                                                    '').replace(
    '[', '').replace(']', '')
  return string;

def select_users(data , IDin):
    remote_connect.execute(("SELECT " + data+ " FROM  users WHERE ID = %s"), (IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;
def select_answer(data, IDin):
    remote_connect.execute(("SELECT " + data + " FROM answer WHERE ID = %s"), (IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;
def select_quesions(data,IDin):
    remote_connect.execute(("SELECT" +data + " FROM questions WHERE ID = %s"), (IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;
def select_results(data, IDin):
    remote_connect.execute(("SELECT " + data + " FROM results WHERE ID = %s"), (IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;
def count_true_results( IDin):
    remote_connect.execute(("SELECT COUNT( result ) FROM result WHERE result = true,ID= %s"),(IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;

#invoeren van een resultaat op een gestelde vraag
def insert_result(user_id, question_id , result):


    sql = "INSERT INTO result (questions_id, users_id,result) VALUES (%s, %s,%s)"
    val = (user_id, question_id,result )
    remote_connect.execute(sql, val)


def insert_question(question,multy,clas):


    sql = "INSERT INTO questions (question,multy,clas) VALUES (%s,%s,%s)"
    val = (question,multy,clas)
    remote_connect.execute(sql, val)

    remote_connect.commit()

def insert_answers(answer, questions_id, correct, possible):
    sql = "INSERT INTO result (answer, questions_id, correct, possible) VALUES (%s, %s,%s)"
    val = (answer, questions_id, correct, possible)
    remote_connect.execute(sql, val)


def update_questions(question,multy,clas):
    sql = 'UPDATE questions SET question = '+question+', multy = '+multy+ ', clas = '+clas+''
    try:
        # Execute the SQL command
        remote_connect.execute(sql)

        # Commit your changes in the database
        remote_connect.commit()
    except:

        remote_connect.rollback()
    sql = '''SELECT * from questions'''
    remote_connect.execute(sql)
    print(remote_connect.fetchall())
    remote_connect.close()
def insert_users(name,last_name,email_address,email_child,age_child,direction,contact,phone_number,code):



    sql = "INSERT INTO user (name,last_name,email_address,email_child,age_child,direction,contact,phone_number,code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name,last_name,email_address,email_child,age_child,direction,contact,phone_number,code)
    remote_connect.execute(sql, val)

def update_users(name,last_name,email_address,email_child,age_child,direction,contact,phone_number,code):
    sql = 'UPDATE  user SET name = ' + name + ', last_name = ' + last_name + ', email_address= ' + email_address + 'email_child ='+email_child+'age_child = '+age_child+ 'direction='+direction+'contact ='+contact+'phone_number ='+phone_number+ 'code ='+code+ ''
    try:
        # Execute the SQL command
        remote_connect.execute(sql)

        # Commit your changes in the database
        remote_connect.commit()
    except:

        remote_connect.rollback()
    sql = '''SELECT * from user'''
    remote_connect.execute(sql)
    print(remote_connect.fetchall())
    remote_connect.close()


print(select_users('*', 'users', 1))
print(('*', 'users', 1))


