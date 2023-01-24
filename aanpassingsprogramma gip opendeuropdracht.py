import tkinter as tk
from tkinter import *
import mysql.connector
import os
from database_gip import *

root= Tk()

def v_of_abutton():
    #kijk of die een vraag of antwoord moet veranderen
    global tabel ,zin ,vrant
    #vrg_of_antbox.select_set(1)
    for i in vrg_of_antbox.curselection():
        vrgant = better_string(vrg_of_antbox.get(i))
        if vrgant == "vraag":
            tabel = "questions"
            zin = "vraag"
            vrg_of_antbox.place_forget()
            vrg_of_antbutton.place_forget()
            welkebutton.place(relx=0.5, rely=0.6, anchor=CENTER)

            welkebox.place(relx=0.5, rely=0.5, anchor=CENTER)
            instructies.configure(text = "Welke " + vrgant)
            
        if vrgant == "antwoord":
            tabel = "answer"
            zin = "answertext"
            vrg_of_antbox.place_forget()
            vrg_of_antbutton.place_forget()
            welkebutton.place(relx=0.5, rely=0.6, anchor=CENTER)

            welkebox.place(relx=0.5, rely=0.5, anchor=CENTER)
            instructies.configure(text = "Welke " + vrgant)
            
        print(tabel,zin)

    #delete alle vragen en antwoorden in de box 
    welkebox.delete(0,END)
        
    if tabel == "answer" :
        my_conn.execute(("SELECT ID FROM "+tabel))
        zinnen_id = my_conn.fetchall()
        my_connect.commit()
        for z_id in zinnen_id:
            z_id = better_string(z_id)

            vrzinnen = select_database("answertext", "answer", z_id)

            #get alle question ids om ervoor te zorgen dat we de vragen kunnen krijgen
            q_id = select_database("question_id", "answer", z_id)
            
            #select alle vragen
            vraag_id = select_database("vraag", "questions", q_id)

            #insert alle zinnen op een nieuwe lijn in listbox
            zinnen = "Ant: " + vrzinnen + " |vraag : " + vraag_id + " ID: " + z_id
            welkebox.insert(ANCHOR, zinnen)
            print(zinnen)
      
    if tabel == "questions" :
        my_conn.execute(("SELECT ID FROM "+tabel))
        zinnen_id = my_conn.fetchall()
        my_connect.commit()
        for z_id in zinnen_id:
            z_id = better_string(z_id)

            vrzinnen = select_database(zin, tabel, z_id)
            
            q_id = select_database("ID", tabel, z_id)

            zinnen = vrzinnen + " ID: " + q_id
            print(zinnen)
            welkebox.insert(ANCHOR, zinnen)

def wlkbutton():
    #clear de selectie van de vorige
    vrg_of_antbox.selection_clear(0,END)
    global tabel, wlke
    for j in welkebox.curselection():
        wlke = better_string(welkebox.get(j))
        print(wlke)

        if welkebox.get(j) != 0:
            
            instructies.configure(text = "Orgineel " + wlke + "\n Nieuwe:")
            welkebox.place_forget()
            newentry.delete(0,END)
            newentry.place(relx=0.5, rely=0.5, anchor=CENTER)
            welkebutton.place_forget()
            
            #als we antwoorden aanpassen moeten we een andere button voor het vragen of de vraag juist of fout is
            if tabel == "questions" :
                okbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
            if tabel == "answer" :
                instructiesant.place(relx=0.5, rely=0.4, anchor=CENTER)
                okansbutton.place(relx=0.5, rely=0.6, anchor=CENTER)

def okansbutton():
    print("okansbutton")
    newentry.place_forget()
    okansbutton.place_forget()
    instructiesant.place_forget()
    jst_of_ftbox.selection_clear(0,END)
    jst_of_ftbox.place(relx=0.5, rely=0.5, anchor=CENTER)
    instructies.configure(text = "Is het antwoord juist of fout?")
    okbutton.place(relx=0.5, rely=0.6, anchor=CENTER)

def okbutton():
    print("okbutton")
    global tabel, zin, wlke
    nieuw = newentry.get()

    # we geven de ID mee om de juiste vraag aan te passen
    my_conn.execute(("UPDATE "+tabel+" SET "+zin+" = '"+nieuw+"' WHERE ID = '"+str(wlke.split("ID: ")[1])+ "'"))
    my_connect.commit()
    # pas juist of fout aan
    if tabel == "answer":
        for j in jst_of_ftbox.curselection():
            j_f = better_string(jst_of_ftbox.get(j))
            if j_f == "Juist":
                nieuw2 = "1"
            if j_f == "Fout":
                nieuw2 = "0"
        my_conn.execute(("UPDATE "+tabel+" SET juist_ant = '"+nieuw2+"' WHERE ID = '"+str(wlke.split("ID: ")[1])+ "'"))
        my_connect.commit()
    instructies.configure(text = "Wil je een vraag of antwoord veranderen?")
    newentry.place_forget()
    jst_of_ftbox.place_forget()
    
    vrg_of_antbox.place(relx=0.5, rely=0.5, anchor=CENTER)
    vrg_of_antbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
    okbutton.place_forget()
    
#connecteer met database
my_conn = my_conn_database_gip()
my_connect = my_connect_database_gip()

#labels buttons listboxen...
instructies = Label(root, text= "Wil je een vraag of antwoord veranderen?")
instructies.place(relx=0.5, rely=0.35, anchor=CENTER)

instructiesant = Label(root, text= "Liefst geen spaties")

vrg_of_antbox = Listbox(root,listvariable = StringVar(value = ("vraag","antwoord") )
                    ,height = 2, exportselection=False)
vrg_of_antbox.place(relx=0.5, rely=0.5, anchor=CENTER)

welkebox = Listbox(root, width = 30
                        , xscrollcommand = True, yscrollcommand = True,exportselection=False)
jst_of_ftbox = Listbox(root,listvariable = StringVar(value = ("Juist","Fout") )
                    ,height = 2, exportselection=False)
#scrollbarx = Scrollbar(zin_vrgantbox, orient = "vertical")
#scrollbary = Scrollbar(zin_vrgantbox, orient = "horizontal")

vrg_of_antbutton = Button(root, text = "next"
                  , command=v_of_abutton)
vrg_of_antbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
welkebutton = Button(root, text = "next"
                  , command=wlkbutton)
okbutton = Button(root, text = "Ok"
                  , command=okbutton)
okansbutton = Button(root, text = "next"
                  , command=okansbutton)

newentry = Entry (root, bd = 5)

tabel = ""
zin = ""
wlke = ""
vrgant = ""

root.mainloop()
