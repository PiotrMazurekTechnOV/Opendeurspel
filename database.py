import mysql.connector



my_connect = mysql.connector.connect(
  host="172.0.0.1",
  user= "",
  passwd="",
  database="database_opendeurdag",)

remote_connect = mysql.connector.connect(
  host="192.168.125.2",
  user= "opendeur",
  passwd="opendeur",
  database="database_opendeurdag",)

my_conn = my_connect.cursor(buffered=True)


def my_connect_database_opendeurdag():
  return remote_connect;

def my_conn_database_opendeurdag():
 return remote_connect;


def better_string(string):
  string = str(string).replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace('{', '').replace('}',
                                                                                                                    '').replace(
    '[', '').replace(']', '')
  return string;

def select_Culumn_out_of_database(tabel, kolom, IDin):
    remote_connect.execute(("SELECT " + tabel + " FROM " + kolom + " WHERE ID = %s"), (IDin,))
    sel = remote_connect.fetchone()
    remote_connect.commit()
    sel = better_string(sel)
    return sel;

def count_true_results(tabel, kolom, IDin):
    my_conn.execute(("SELECT COUNT(" +tabel + ") FROM " +kolom +"WHERE result = true,ID= %s"),(IDin,))
    sel = remote_connect.fetchone()
    my_connect.commit()
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
def insert_user(name,last_name,email_adres,email_kind,age_child,direction,contact,phone_number,code):



    sql = "INSERT INTO user (name,last_name,email_adres,email_kind,age_child,direction,contact,phone_number,code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name,last_name,email_adres,email_kind,age_child,direction,contact,phone_number,code)
    remote_connect.execute(sql, val)




print(select_Culumn_out_of_database('*', 'users', 1))

