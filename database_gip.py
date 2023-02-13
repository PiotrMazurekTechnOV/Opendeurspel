import mysql.connector
import os
from tkinter import *

#connecteer met database
my_connect = mysql.connector.connect(
  host="192.168.106.101",
  user="extern", 
  passwd="GIPFaraTom2022",
  database="gip opendeuropdracht"
)
my_conn = my_connect.cursor(buffered=True)
def my_connect_database_gip():
    return my_connect;
    
def my_conn_database_gip():
    return my_conn;

def better_string(string):
    string = str(string).replace(',','').replace('(','').replace(')','').replace("'",'').replace('{','').replace('}','').replace('[','').replace(']','')
    return string;

'''def in_lab(txt):
    return Label(root, text = txt ,bg="#A1EAEC", fg="#5B89A5", font=("Constantia",20));

def in_ent():
    return Entry (root, bd = 5);'''

def select_database(wat, waar, IDin):
    my_conn.execute(("SELECT "+wat+" FROM "+waar+" WHERE ID = %s"),(IDin,))
    sel = my_conn.fetchone()
    my_connect.commit()
    sel = better_string(sel)
    return sel;

                
    

    
    
