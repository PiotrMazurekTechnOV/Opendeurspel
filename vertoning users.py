from tkinter import *
import mysql.connector
import os
from database_gip import *
import re

root= Tk()

Labelid = Label(root, text = "ID")
Labelna = Label(root, text = "Naam")
Labelem = Label(root, text = "E-Mail")
Labelco = Label(root, text = "Contact")
Labelac = Label(root, text = "Achternaam")
Labelle = Label(root, text = "Leeftijd")
Labelri = Label(root, text = "Geintreseerde Richting")
Labelno = Label(root, text = "Naam Ouder")
Labeleo = Label(root, text = "E-Mail Ouder")
Labelte = Label(root, text = "Telefoonnummer")

Labelid.grid(row = 0, column = 0)
Labelna.grid(row = 0, column = 1)
Labelem.grid(row = 0, column = 2)
Labelco.grid(row = 0, column = 3)
Labelac.grid(row = 0, column = 4)
Labelle.grid(row = 0, column = 5)
Labelri.grid(row = 0, column = 6)
Labelno.grid(row = 0, column = 7)
Labeleo.grid(row = 0, column = 8)
Labelte.grid(row = 0, column = 9)

#connecteer met database
my_conn = my_conn_database_gip()
my_connect = my_connect_database_gip()

my_conn.execute("SELECT * FROM users WHERE contact = 1")
i=1 
for student in my_conn: 
    for j in range(len(student)):
        e = Entry(root, width=20, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1

root.mainloop()
