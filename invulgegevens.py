from tkinter import *
from PIL import *
from PIL import ImageTk, Image
#import mysql.connector
import re

import os
import subprocess

from keyboard_new import KeyboardEntry

#from database_gip import *

#import pyglet
#pyglet.font.add_file('Gilroy-Light.otf')

#e-mail requirements
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

studie_richting_opties = ["a", "b", "c"]
    

class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class HomePagina(Pagina):
   def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)

        #titel
        welkom = Label(self, text = "Welkom op de opendeurdag van Technov!"
               , fg="#1b709d", font=("Gilroy Light", 65))
        welkom.place(relx=0.5, rely=0.1, anchor=N)

        #uitleg
        uitleg = Label(self, text = """Dit is het opendeurspel gemaakt door de leerlingen Industriele ICT.
Tijdens u traject op onze school zal u vragen kunnen invullen met uw ID.
Als u hieronder op Start! duwt.
Gaat u naar de registratiepagina waar u uw persoonlijk quiz ID ontvangt!
Op het einde van je rondleiding zal u uw score kunnen afdrukken als een 'diploma'!
Veel plezier!""", fg="#1b709d", font=("gilroy light",35), pady=50)
        uitleg.place(relx=0.5, rely=0.25, anchor=N)

class GegevensPagina(Pagina):
   def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        #canvas = Canvas(self, width="100c", height="100c", bg="#1b709d")
        #canvas.pack()

        #titel
        welkom = Label(self, text = "Welkom op de opendeurdag van Technov!", fg="#1b709d", font=("Gilroy Light", 36))
        welkom.place(relx=0.5, rely=0.05, anchor=N)

        #uitleg
        uitleg = Label(self, text = "Vul uw gegevens hier in, dan ontvangt u uw ID.", fg="#1b709d", font=("gilroy light", 24))
        uitleg.place(relx=0.5, rely=0.2, anchor=N)

        oXE = .32 #X entry offset
        oYES = 0.354 #Y entry start offset

        font = ("Gilroy Light", 30)
        entry_font = ("Gilroy Light", 20)
        height = 25

        oY = .07 #Y entry offset

        oYLS = 0.35 #Y label start offset

        oYES += .09
        oYLS += .09
        oY += .025

        #voornaam
        naam_text = Label(self, text = "Voornaam:", fg="#1b709d", font=font)
        naam_text.place(relx=0.2, rely=oYLS, anchor=CENTER)
        naam_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        naam_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=height, width=150)

        #achternaam
        achternaam_text = Label(self, text = "Achternaam:", fg="#1b709d", font=font)
        achternaam_text.place(relx=0.192, rely=oYLS + oY, anchor=CENTER)
        achternaam_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        achternaam_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=height, width=150)

        #leeftijd
        leeftijd_text = Label(self, text = "Leeftijd:", fg="#1b709d", font=font)
        leeftijd_text.place(relx=0.215, rely=oYLS + oY * 2, anchor=CENTER)
        leeftijd_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        leeftijd_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=height, width=150)

        #naam ouder/voogd
        ouder_text = Label(self, text = "Naam ouder/voogd:", fg="#1b709d", font=font)
        ouder_text.place(relx=0.156, rely=oYLS + oY * 3, anchor=CENTER)
        ouder_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        ouder_entry.place(relx=oXE, rely=oYES + oY * 3, anchor=CENTER, height=height, width=150)

        oXE += .4

        #email kind
        email_kind_text = Label(self, text = "E-mail kind:", fg="#1b709d", font=font)
        email_kind_text.place(relx=.59, rely=oYLS, anchor=CENTER)
        email_kind_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        email_kind_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=height, width=150)

        studierighting = StringVar(self)
        studierighting.set("Selecteer studie richting") # default value

        #studierichting
        studie_text = Label(self, text = "Studierichting:", fg="#1b709d", font=font)
        studie_text.place(relx=0.58, rely=oYLS + oY, anchor=CENTER)
        studie_entry = OptionMenu (self, studierighting, *studie_richting_opties)
        studie_entry.configure(bd = 1, indicatoron=0, height=height)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        studie_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=height, width=150)

        #Telefoon
        tel_text = Label(self, text = "Telefoon:", fg="#1b709d", font=font)
        tel_text.place(relx=0.605, rely=oYLS + oY * 2, anchor=CENTER)
        tel_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        tel_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=height, width=150)

        #Email ouders
        email_ouders_text = Label(self, text = "Email:", fg="#1b709d", font=font)
        email_ouders_text.place(relx=0.622, rely=oYLS + oY * 3, anchor=CENTER)
        email_ouders_entry = KeyboardEntry (self, bd = 1, font=font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        email_ouders_entry.place(relx=oXE, rely=oYES + oY * 3, anchor=CENTER, height=height, width=150)

        contact_box = Checkbutton(self, text="Wilt u door ons gecontacteerd worden?", font=font)
        contact_box.place(relx=0.5, rely=0.8, anchor=CENTER)

        #cntctbox.bind('<<ListBoxSelect>>', okbutton)

        def gegevens_ingevuld():
            global adressin, numm, eoudin
            naam = naam_entry.entry.get()
            achternaam = achternaam_entry.entry.get()
            leeftijd = leeftijd_entry.entry.get()
            telefoonnummer = tel_entry.entry.get()
            naam_ouder = ouder_entry.entry.get()
            email_kind = email_kind_entry.entry.get()
            email_ouder = email_ouders_entry.entry.get()
            contact_value = contact_box.instate(['selected'])

            ##### check e-mail

            if(True): #(re.fullmatch(email_regex, email_kind))and(re.fullmatch(email_regex, email_ouder)) and leeftijd.isnumeric() and telefoonnummer.isnumeric():

                ##SEND TO DATABASE

                #klaarbutton.place_forget()
                #emailfout.place_forget()

                #volgendebutton.place_forget()
            
                #volgendebutton.place(relx=0.5, rely=0.9, anchor=CENTER)
                pass
            else:

                print("Invalid Email")
                emailfout.place(relx=0.5, rely=0.9, anchor=CENTER)

        klaar = Button(self, text=" Klaar! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=gegevens_ingevuld, activeforeground="#FFFFFF", activebackground="#1b709d")        
        klaar.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = HomePagina(self)
        p2 = GegevensPagina(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        #b1 = Button(p2, text="Klaar!", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=p1.lift, activeforeground="#FFFFFF", activebackground="#1b709d")
        b2 = Button(p1, text=" Start! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 30), relief= FLAT , command=p2.lift, activeforeground="#FFFFFF", activebackground="#1b709d")        

        #b1.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        b2.place(relx=.5 ,rely=0.875, relwidth=.15, anchor=CENTER) 

        p1.show()

def new_window():
    #klaarbutton
    def klbutton():
        global adressin, numm, eoudin
        naamin = gegevens_naam.get()
        adressin = gegevens_adress.get()
        achin = gegevens_acnaam.get()
        leefin = gegevens_leef.get()
        studin = ""
        for j in studiebox.curselection():
            studin = better_string(studiebox.get(j))
        noudin = gegevens_oudnaam.get()
        eoudin = gegevens_oudadress.get()
        telein = gegevens_tel.get()

        ##### check e-mail

        if(re.fullmatch(regex, adressin))and(re.fullmatch(regex, eoudin)) and leefin.isnumeric() and telein.isnumeric():

            print("Valid Email")
            #Mazurek: user input valideren voordat het in de query wordt geplaatst
            add =("INSERT INTO users(naam, email , achternaam , leeftijd, richting , naam_ouder , email_ouder , telefoonnummer) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
            val = (naamin, adressin, achin, leefin, studin, noudin, eoudin, telein)
            #my_conn.execute(add,val)
            #my_connect.commit()

            #volgendebutton.place(relx=0.5, rely=0.7, anchor=CENTER)

            klaarbutton.place_forget()
            emailfout.place_forget()

            volgendebutton.place_forget()
            nummer.configure(text="Wil je door ons gecontacteert worden?",font=("Constantia",30))
            cntctbox.place(relx=0.5, rely=0.75, anchor=CENTER)

            nummer.place(relx=0.5, rely=0.7, anchor=CENTER)

            adressin = gegevens_adress.get()
            #my_conn.execute(("SELECT ID FROM users WHERE email = %s"),(adressin,))
            #num = my_conn.fetchone()
            #my_connect.commit()
            numm = str(num).replace(',','').replace('(','').replace(')','').replace("'",'')
        
            volgendebutton.place(relx=0.5, rely=0.9, anchor=CENTER)
            print(numm)

        else:

            print("Invalid Email")
            emailfout.place(relx=0.5, rely=0.9, anchor=CENTER)
            
        ##### 
    #contactbutton
    def vlgndbutton():
        global cont, numm, adressin
        #cont = ""
        print(numm)
        #mag je gecontacteert worden?
        for i in cntctbox.curselection():
            if cntctbox.get(i) == "Ja":
                #my_conn.execute(("UPDATE users SET contact = 1 WHERE ID = %s"),(numm,))
                print (numm)
                #my_connect.commit()
            if cntctbox.get(i) == "Nee":
                pass
                #my_conn.execute(("UPDATE users SET contact = 0 WHERE ID = %s"),(numm,))
                #my_connect.commit()
        cntctbox.selection_clear(0,END)
        cntctbox.place_forget()
        volgendebutton.place_forget()
        nummer.configure(text = "Uw nummer is: " + numm + "\n Vergeet dit nummer niet!"
                            ,font = ("Constantia",20))
        nummer.place(relx=0.5, rely=0.7, anchor=CENTER)
        okbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
        '''for i in cntctbox.curselection():
            if cntctbox.get(i) == "Ja":
                okbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
                cont = cntctbox.get(i)
            if cntctbox.get(i) == "Nee":
                okbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
                cont = cntctbox.get(i)    '''      
    
    #okbutton
    def okbutton():
        #okbutton.place_forget()
        global numm
        nummer.configure(text = "Uw nummer is: " + numm + "\n Vergeet dit nummer niet!"
                            ,font = ("Constantia",20))
        nummer.place(relx=0.5, rely=0.7, anchor=CENTER)
            
            #delete dingen in entry
        gegevens_naam.delete(0,END)
        gegevens_adress.delete(0,END)
        gegevens_acnaam.delete(0,END)
        gegevens_leef.delete(0,END)
        gegevens_oudnaam.delete(0,END)
        gegevens_oudadress.delete(0,END)
        gegevens_tel.delete(0,END)
        studiebox.selection_clear(0,END)
        klaarbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
        #finbutton.place(relx=0.5, rely=0.7, anchor=CENTER)
        okbutton.place_forget()
        nummer.place_forget()

    def finbutton():
        #klaarbuton.place_forget()
        klaarbuton.place_forget()
        finbutton.place_forget()
        nummer.place_forget()
        klaarbutton.place(relx=0.5, rely=0.7, anchor=CENTER)

    klaarbutton = Button(root, text='klaar', bg="#502E93", fg="#F9DEE3", font=("Constantia", 15), relief = GROOVE , command=klbutton)
    klaarbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
    volgendebutton = Button(root, text='volgende', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE, command=vlgndbutton)
    emailfout = Label(root, text = "foute e-mail", bg="#DF3740", font=("Constantia",15),relief = GROOVE)

    okbutton = Button(root, text='Ok', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE, command=okbutton)
    finbutton = Button(root, text='Fin', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE, command=finbutton)
    cntctbox = Listbox(root,listvariable = StringVar(value =("Ja","Nee")), height = 2, exportselection=False, bg="#502E93", fg="#F9DEE3", font=("Constantia",10),relief = GROOVE)
    cntctbox.bind('<<ListBoxSelect>>', okbutton)
    nummer = Label(root)

def welcome_screen():
    #create button that will be placed
    button = Button(root, text="new window", bg='black', fg='#469A00',
                              command=lambda: new_window())
    button.place(relx=0.5, rely=0.8, anchor=CENTER)

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    #root.iconbitmap('kovlogo.ico')
    root.attributes('-fullscreen', True)
    root.mainloop()
