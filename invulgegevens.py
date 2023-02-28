from tkinter import *
from PIL import *
from PIL import ImageTk, Image
import database
import re

import os
import subprocess

from keyboard_new import KeyboardEntry


#import pyglet
#pyglet.font.add_file('Gilroy-Light.otf')

#e-mail requirements
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

studie_richting_opties = ["1A STEM-WETENSCHAPPEN", "1A STEM-TECHNIEKEN", "1B STEM-TECHNIEKEN", "2A STEM-WETENSCHAPPEN", "2A STEM-TECHNIEKEN", "2B STEM-TECHNIEKEN",
                          "Technologische wetenschappen", "Elektrotechnieken", "Mechanische technieken", "Elektriciteit", "Hout", "Mechanica", "Technologische wetenschappen en engineering", 
                          "Elektrotechnieken", "Industriele ICT", "Mechanische Vormgevings Technieken", "Binnenschrijnwerk en interieur", "Elektrische instalaties", "Fiets instalaties", "Lassenconstructie", "Onderhoudsmechanica Auto"]
    

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
        uitleg.place(relx=0.5, rely=0.15, anchor=N)

        #error
        self.error = Label(self, text = "", fg="red", font=("gilroy light", 24))
        self.error.place(relx=0.5, rely=0.25, anchor=N)

        oXE = .35 #X entry offset
        oYES = 0.354 #Y entry start offset

        font = ("Gilroy Light", 30)
        entry_font = ("Gilroy Light", 20)
        height = 35
        entry_width = 350

        oY = .07 #Y entry offset

        oYLS = 0.35 #Y label start offset

        oYES += .09
        oYLS += .09
        oY += .025

        oYES -= .025
        oYLS -= .025
        #oY -= .025

        #voornaam
        naam_text = Label(self, text = "Voornaam:", fg="#1b709d", font=font)
        naam_text.place(relx=0.2, rely=oYLS, anchor=CENTER)
        naam_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        naam_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=height, width=entry_width)

        #achternaam
        achternaam_text = Label(self, text = "Achternaam:", fg="#1b709d", font=font)
        achternaam_text.place(relx=0.192, rely=oYLS + oY, anchor=CENTER)
        achternaam_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        achternaam_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=height, width=entry_width)

        #leeftijd
        leeftijd_text = Label(self, text = "Leeftijd:", fg="#1b709d", font=font)
        leeftijd_text.place(relx=0.215, rely=oYLS + oY * 2, anchor=CENTER)
        leeftijd_entry = KeyboardEntry (self, bd = 1, font=entry_font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        leeftijd_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=height, width=entry_width)

        oXE += .4

        studierighting = StringVar(self)
        studierighting.set("In welke richting bent u geïnteresseerd?") # default value

        #studierichting
        studie_text = Label(self, text = "Studierichting:", fg="#1b709d", font=font)
        studie_text.place(relx=0.58, rely=oYLS, anchor=CENTER)
        studie_entry = OptionMenu (self, studierighting, *studie_richting_opties)
        studie_entry.configure(bd = 1, indicatoron=0, height=height)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        studie_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=height, width=entry_width)

        #Telefoon
        tel_text = Label(self, text = "Telefoon:", fg="#1b709d", font=font)
        tel_text.place(relx=0.605, rely=oYLS + oY, anchor=CENTER)
        tel_entry = KeyboardEntry (self, bd = 1, font=font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        tel_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=height, width=entry_width)

        #Email ouders
        email_ouders_text = Label(self, text = "Email:", fg="#1b709d", font=font)
        email_ouders_text.place(relx=0.622, rely=oYLS + oY * 2, anchor=CENTER)
        email_ouders_entry = KeyboardEntry (self, bd = 1, font=font)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        email_ouders_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=height, width=entry_width)

        def change_contact_box():
            contact_allowed.set(not contact_allowed.get())
            contact_box.config(text="✅ Wilt u door ons gecontacteerd worden?" if contact_allowed.get() else "❌ Wilt u door ons gecontacteerd worden?")

        contact_allowed = BooleanVar(value=False)
        contact_box = Button(self, text="✅ Wilt u door ons gecontacteerd worden?", font=("", 15), command=change_contact_box)
        contact_box.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.contact_box = contact_box


        #cntctbox.bind('<<ListBoxSelect>>', okbutton)
        self.naam_entry = naam_entry.entry
        self.achternaam_entry = achternaam_entry.entry
        self.leeftijd_entry = leeftijd_entry.entry
        self.tel_entry = tel_entry.entry
        self.email_entry = email_ouders_entry.entry
        self.studierichting = studierighting
        self.contact_allowed = contact_allowed


    def gegevens_ingevuld(self):
        global adressin, numm, eoudin
        naam = self.naam_entry.get()
        achternaam = self.achternaam_entry.get()
        leeftijd = self.leeftijd_entry.get()
        telefoonnummer = self.tel_entry.get()
        email = self.email_entry.get()
        contact_value = self.contact_allowed.get()
        studierighting_value = self.studierichting.get()
        self.error.config(text="")
        ##### check e-mail
        if (not(len(email) <= 0 or re.fullmatch(email_regex, email))):
            self.error.config(text="Ongeldig e-mailadres")
            return False
        if (not(len(telefoonnummer) <= 0 or telefoonnummer.isnumeric())):
            self.error.config(text="Ongeldig telefoonnummer")
            return False
        if (not(len(leeftijd) <= 0 or leeftijd.isnumeric())):
            self.error.config(text="Ongeldig leeftijd")
            return False
        if (len(naam) <= 0 or len(achternaam) <= 0):
            self.error.config(text="Vul uw naam en achternaam in")
            return False

        if (len(leeftijd) == 0):
            leeftijd = 0
        if (len(telefoonnummer) == 0):
            telefoonnummer = 0
        
        result = database.insert_user(naam, achternaam, email, leeftijd, studierighting_value, contact_value, telefoonnummer)
        if (result.find(" for user: ")):
            return (True, result.split(" for user: ")[1])
        self.error.config(text=result)
        return False
    
    def clearInputFields(self):
        self.naam_entry.delete(0, END)
        self.achternaam_entry.delete(0, END)
        self.leeftijd_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.contact_allowed.set(True)
        self.contact_box.config(text="✅ Wilt u door ons gecontacteerd worden?")
        self.studierichting.set("In welke richting bent u geïnteresseerd?")
   

class SuccesPage(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        welkom = Label(self, text = "Welkom op de opendeurdag van Technov!", fg="#1b709d", font=("Gilroy Light", 36))
        welkom.place(relx=0.5, rely=0.05, anchor=N)

        #uitleg
        uitleg = Label(self, text = """Je bent succesvol geregistreerd. 

        Hieronder staat je code om je bij de vragenschermen in te loggen:""", fg="#1b709d", font=("gilroy light", 40))
        uitleg.place(relx=0.5, rely=0.25, anchor=N)

        self.code = Label(self, text = "", fg="#1b709d", font=("gilroy light", 50))
        self.code.place(relx=0.5, rely=0.5, anchor=N)

        onthoud = Label(self, text = "Onthoud deze!", fg="#1b709d", font=("gilroy light", 40))
        onthoud.place(relx=0.5, rely=0.62, anchor=N)
    
    def show_with_id(self, id):
        self.code.config(text=id)
        self.lift()

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = HomePagina(self)
        p2 = GegevensPagina(self)
        p3 = SuccesPage(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)       
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)    

        def klaar():
            result = p2.gegevens_ingevuld()
            if (result and result[0]):
                p3.show_with_id(result[1])
            print(result[1])
            p2.clearInputFields()

        b1 = Button(p1, text=" Start! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 30), relief= FLAT , command=p2.lift, activeforeground="#FFFFFF", activebackground="#1b709d")        
        b2 = Button(p2, text=" Klaar! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=klaar, activeforeground="#FFFFFF", activebackground="#1b709d")  
        b3 = Button(p3, text=" Klaar! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=p1.lift, activeforeground="#FFFFFF", activebackground="#1b709d")              

        b1.place(relx=.5 ,rely=0.875, relwidth=.15, anchor=CENTER) 
        b2.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        b3.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    #root.iconbitmap('kovlogo.ico')
    root.attributes('-fullscreen', True)
    root.mainloop()
