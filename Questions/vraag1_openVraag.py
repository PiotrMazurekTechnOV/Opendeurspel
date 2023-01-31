from tkinter import *
def SetUp():
    import tkinter as tk
    import os
    #from database_gip import *

    root= Tk()
    root.attributes('-fullscreen', True)

    #bg = PhotoImage(file = "../bg_vraag.png")

    #imagelabel = Label(root, image = bg)
    #imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)
    hallo = Label(root)

    vraagzin = ''
    naam = ''
    antzin= ''
    IDin = 0
    punt = 0
    vraagnr = 0

    #loginbutton
    def lgnbutton():
        global naam, IDin, hallotekst
        IDin = login.get()

        #mail = select_database("email", "users", IDin)
        #naam = select_database("naam", "users", IDin)
        ##bestaat het nummer
    
            #om hallo tegen de gebruiker te, gebruiker kan nu ook terug gaan
        hallo.configure(text = f"hallo test , \n Welkom bij de vraag"
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
        global vraagzin, antzin
        hallo.place_forget()
        vraagbutton.place_forget()
        okbutton.place_forget()

        #checkt wat de vraag is
        vraagzin = "test"
        #select_database("vraag", "questions", 1)

        #checkt wat het antwoord is
        #my_conn.execute(("SELECT answertext FROM answer WHERE question_id = 1 "))
        #antzin = better_string(my_conn.fetchone())
        #my_connect.commit()

        print(antzin)
        vraag.configure(text = vraagzin)
        vraag.place(relx=0.5, rely=0.35, anchor=CENTER)
    
        antwoord.place(relx=0.5, rely=0.5, anchor=CENTER) #dit is de entry

        klaarbutton.place(relx=0.7, rely=0.5, anchor=CENTER)


    #klaarbutton
    def klbutton():
        global IDin, antzin
        #is het ingegeven juist of fout?
        if antwoord.get() == antzin:
            punt = 5
            ant_zin = "Correct"
        else:
            punt = 0
            ant_zin = "Dat is niet juist"
        print(punt)

        #vergeet vraag met inputbox
        antwoord.place_forget()
        antwoord.delete(0,END)
        klaarbutton.place_forget()
        vraag.place_forget()

        #plaats een antwoordzin
        zin.config(text = ant_zin,font = ("Constantia",50) ,bg="#EA4413", fg="#FFEEF1",relief = RIDGE)
        zin.place(relx=0.5, rely=0.35, anchor=CENTER)

        okbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
    
        #my_conn.execute(("INSERT INTO results (user_id, question_id, result) VALUES(%s, 1 ,result + %s)"),(IDin, punt))
        #my_connect.commit()

    def okbutton():
        hallo.place_forget()
        okbutton.place_forget()
        zin.place_forget()
        #deze vergeten voor terug te kunnen
        vraagbutton.place_forget()

        login.delete(0,END)

        log.place(relx=0.5, rely=0.35, anchor=CENTER)
        login.place(relx=0.5, rely=0.5, anchor=CENTER)
        loginbutton.place(relx=0.7, rely=0.5, anchor=CENTER)

    #login
    log = Label(root, text = "Geef hier je nummer in"
                ,font = ("Constantia",35) ,bg="#A1ACD9", fg="#3C1B3A",relief = RIDGE)
    log.place(relx=0.5, rely=0.35, anchor=CENTER)
    login = Entry (root, bd = 5)
    login.place(relx=0.5, rely=0.5, anchor=CENTER)
    loginbutton = Button(root, text='login',bg="#502E93", fg="#F9DEE3", font=("Constantia",25),relief = GROOVE
                     , command=lgnbutton)
    loginbutton.place(relx=0.7, rely=0.5, anchor=CENTER)

    zin = Label(root)
    hallo = Label(root)
    vraag = Label(root, text = vraagzin
              ,bg="#8C4509", fg="#F9DEE3", font=("Constantia",40),relief = GROOVE)
    klaarbutton = Button(root, text='klaar', command=klbutton
                     ,bg="#502E93", fg="#F9DEE3", font=("Constantia",35),relief = GROOVE)
    antwoord = Entry (root, bd = 5)
    vraagbutton = Button(root, text='Ga naar de vraag',bg="#502E93", fg="#F9DEE3", font=("Constantia",30),relief = GROOVE
                     , command=vrgbutton)
    okbutton = Button(root, bg="#502E93", fg="#F9DEE3",relief = GROOVE
                  , command=okbutton)

    #connecteer met database
    #my_conn = my_conn_database_gip()
    #my_connect = my_connect_database_gip()

    root.mainloop()