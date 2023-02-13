from PIL import *
from tkinter import *
import mysql.connector
import os
from database_gip import *

root= Tk()
root.iconbitmap('kovlogo.ico')

root.attributes('-fullscreen', True)
bg = PhotoImage(file = "bg_vraag.png")

imagelabel = Label(root, image = bg)
imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)

punt = 0
vr = ""
punt1 = 0
vraagzin1 = ''
vraagzin2 = ''
vraagzin3 = ''
##chekt als persoon al geweest is #er is al 1 ID in zodat hij niet crashed
al_geweest = [""]     #array

#loginbutton
def lgnbutton():
    global naam, IDin, hallotekst
    IDin = login.get()
    
    mail = select_database("email", "users", IDin)
    naam = select_database("naam", "users", IDin)

            ##bestaat het nummer
    if(mail == "None"):
        hallo.configure(text = "ongeldig nummer"
                            , bg="#DF3740", font=("Constantia",35),relief = GROOVE)
        okbutton.configure(text='Ok',
                                   font=("Constantia",35))
        okbutton.place(relx=0.8, rely=0.5, anchor=CENTER)
    else:
                #om hallo tegen de gebruiker te zeggen, gebruiker kan nu ook terug gaan
        hallo.configure(text = f"hallo {naam} , \n Welkom bij de vraag"
                            , bg="#FCF1AF", font=("Constantia",35),relief = GROOVE)
        vraagbutton.place(relx=0.8, rely=0.5, anchor=CENTER)
        okbutton.configure(text='Terug',
                                   font=("Constantia",25))
        okbutton.place(relx=0.5, rely=0.7, anchor=CENTER)

    hallo.place(relx=0.5, rely=0.5, anchor=CENTER)

    log.place_forget()
    login.place_forget()
    loginbutton.place_forget()

#vraagbutton
def vrgbutton():
    global al_geweest
    al_geweest.extend(IDin)
    hallo.place_forget()
    vraagbutton.place_forget()
    okbutton.place_forget()

    #checkt wat de vraag is
    vraagzin1 = select_database("vraag", "questions", 17)
    
    #config de vraagzin
    vraag1.configure(text = vraagzin1)
    
    vraag.place(relx=0.5, rely=0.2, anchor=CENTER)
    vraag1.place(relx=0.5, rely=0.35, anchor=CENTER)
    
    antwoord1.place(relx=0.5, rely=0.5, anchor=CENTER)

    klaarbutton.place(relx=0.5, rely=0.9, anchor=CENTER)

#klaarbutton
def klbutton():
    global IDin, punt, vr, punt1
    #we gebruiken dit om te kijken welke vraag iemand fout had
    vr1 = "1"

    #dit is om vragen opnieuw op 0 te zetten
    punt1 = 0
    
    #is het ingegeven juist of fout?
    for i in antwoord1.curselection():
        an1 = ""
        #we replacen al de ,()' omdat die van de database komen
        an1 = better_string(antwoord1.get(i))
        #kijk of ant juist is
        my_conn.execute(("SELECT juist_ant FROM answer WHERE question_id = 17 AND answertext = %s"),(an1,))
        #fetch one en replace onodige tekens
        an1 = better_string(my_conn.fetchone())
        my_connect.commit()
        
        if an1 == "1":
            #replace het nummer van de vraag die je juist hebt met niets
            vr1 = ""
            punt1 = 5
        
    if punt1 == 5:
        zin.configure(text = "Correct"
                      ,font = ("Constantia",50) ,bg="#EA4413", fg="#FFEEF1",relief = RIDGE)
    else:
        zin.configure(text = "Dat is niet helemaal juist."
                      ,font = ("Constantia",50) ,bg="#EA4413", fg="#FFEEF1",relief = RIDGE)

    #vergeet vraag en antwoorden
    antwoord1.place_forget()
    antwoord1.selection_clear(0,END)
    klaarbutton.place_forget()
    vraag.place_forget()
    vraag1.place_forget()

    #maak een antwoordzin
    zin.place(relx=0.5, rely=0.35, anchor=CENTER)

    okbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    #my_conn.execute(("INSERT INTO results (user_id, question_id, result) VALUES(%s, 2 ,result + %s)")
                    #,(IDin, punt))
    my_conn.execute(("INSERT INTO results (user_id, question_id, result) VALUES(%s, 17 ,result + %s)")
                    ,(IDin, punt1))
    my_connect.commit()

def okbutton():
    hallo.place_forget()
    okbutton.place_forget()
    zin.place_forget()
    vraagbutton.place_forget()

    login.delete(0,END)

    log.place(relx=0.5, rely=0.35, anchor=CENTER)
    login.place(relx=0.5, rely=0.5, anchor=CENTER)
    loginbutton.place(relx=0.7, rely=0.5, anchor=CENTER)
    
#connecteer met database
my_conn = my_conn_database_gip()
my_connect = my_connect_database_gip()

#login
log = Label(root, text = "Geef hier je nummer in"
            ,font = ("Constantia",35) ,bg="#A1ACD9", fg="#3C1B3A",relief = RIDGE)
log.place(relx=0.5, rely=0.35, anchor=CENTER)
login = Entry (root, bd = 5)
login.place(relx=0.5, rely=0.5, anchor=CENTER)
loginbutton = Button(root, text='login',bg="#502E93", fg="#F9DEE3", font=("Constantia",25),relief = GROOVE
                     , command=lgnbutton)
loginbutton.place(relx=0.7, rely=0.5, anchor=CENTER)

#andere buttons en labels
hallo = Label(root)
vraag = Label(root, text = "Zet de juiste antwoorden bij de vraag"
              ,bg="#8C4509", fg="#F9DEE3", font=("Constantia",40),relief = GROOVE)
klaarbutton = Button(root, text='klaar', command=klbutton
                     ,bg="#502E93", fg="#F9DEE3", font=("Constantia",35),relief = GROOVE)
vraagbutton = Button(root, text='Ga naar de vraag'
                     ,bg="#502E93", fg="#F9DEE3", font=("Constantia",30),relief = GROOVE
                     , command=vrgbutton)
okbutton = Button(root, text='Ok', command=okbutton
                  , bg="#502E93", fg="#F9DEE3",relief = GROOVE)
zin = Label(root)

#de vraag
vraag1 = Label(root, text = "wat is 7-1"
               ,bg="#8C4509", fg="#FBF4D7", font=("Constantia",30),relief = GROOVE)

#alle antwoorden
#eerst fetch de getallen
my_conn.execute(("SELECT answertext FROM answer WHERE question_id = 17"))
ant1 = my_conn.fetchall()
my_connect.commit()

antwoord1 = Listbox(root,listvariable = StringVar(value = ant1 )
                    ,height = 3, exportselection=False
                   ,bg="#8C4509", fg="#F9DEE3", font=("Constantia",30),relief = GROOVE)

root.mainloop()
