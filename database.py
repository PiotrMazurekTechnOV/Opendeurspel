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