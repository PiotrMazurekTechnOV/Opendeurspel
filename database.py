import mysql.connector



my_connect = mysql.connector.connect(
  host="172.0.0.1",
  user= "",
  passwd="",
  database="database_opendeurdag",)

my_conn = my_connect.cursor(buffered=True)


def my_connect_database_opendeurdag():
  return my_connect;

def my_conn_database_opendeurdag():
 return my_conn;


def better_string(string):
  string = str(string).replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace('{', '').replace('}',
                                                                                                                    '').replace(
    '[', '').replace(']', '')
  return string;

def select_database(wat, waar, IDin):
    my_conn.execute(("SELECT " + wat + " FROM " + waar + " WHERE ID = %s"), (IDin,))
    sel = my_conn.fetchone()
    my_connect.commit()
    sel = better_string(sel)
    return sel;

<<<<<<< HEAD
def count_true_results():
    query = "SELECT COUNT(wat) FROM waar WHERE result = true"
    my_conn.execute(query)
    count = my_conn.fetchone()
    my_connect.commit()
    return count;
=======
def insert_database(wat , waar , IDin): 
    my_conn.execute<(("INSERT " + wat +  " FROM " + " WHERE ID = %s "), (IDin,))
    sel = my_conn.fetchone()
    my_connect.commit()
    sel = better_string(sel)
    return sel;
>>>>>>> 5d8899c2f9ea6b450f74a74ae4a871c74f921396
