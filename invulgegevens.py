from tkinter import *
from PIL import *
from PIL import ImageTk, Image
#import mysql.connector
import re

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
               , fg="#1b709d", font=("Gilroy Light",36))
        welkom.place(relx=0.5, rely=0.05, anchor=N)

        #uitleg
        uitleg = Label(self, text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos 
sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
recusandae alias error harum maxime adipisci amet laborum. Perspiciatis""", fg="#1b709d", font=("gilroy light",24))
        uitleg.place(relx=0.5, rely=0.2, anchor=N)

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

        oY = .07 #Y entry offset

        oYLS = 0.35 #Y label start offset

        oYES += .09
        oYLS += .09
        oY += .025

        #voornaam
        naam_text = Label(self, text = "Voornaam:", fg="#1b709d", font=("Gilroy Light", 20))
        naam_text.place(relx=0.2, rely=oYLS, anchor=CENTER)
        naam_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        naam_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=25, width=150)

        #achternaam
        achternaam_text = Label(self, text = "Achternaam:", fg="#1b709d", font=("Gilroy Light", 20))
        achternaam_text.place(relx=0.192, rely=oYLS + oY, anchor=CENTER)
        achternaam_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        achternaam_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=25, width=150)

        #leeftijd
        leeftijd_text = Label(self, text = "Leeftijd:", fg="#1b709d", font=("Gilroy Light", 20))
        leeftijd_text.place(relx=0.215, rely=oYLS + oY * 2, anchor=CENTER)
        leeftijd_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        leeftijd_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=25, width=150)

        #naam ouder/voogd
        ouder_text = Label(self, text = "Naam ouder/voogd:", fg="#1b709d", font=("Gilroy Light", 20))
        ouder_text.place(relx=0.156, rely=oYLS + oY * 3, anchor=CENTER)
        ouder_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        ouder_entry.place(relx=oXE, rely=oYES + oY * 3, anchor=CENTER, height=25, width=150)

        oXE += .4

        #email kind
        email_kind_text = Label(self, text = "E-mail kind:", fg="#1b709d", font=("Gilroy Light", 20))
        email_kind_text.place(relx=.59, rely=oYLS, anchor=CENTER)
        email_kind_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        email_kind_entry.place(relx=oXE, rely=oYES, anchor=CENTER, height=25, width=150)

        studierighting = StringVar(self)
        studierighting.set("Selecteer studie richting") # default value

        #studierichting
        studie_text = Label(self, text = "Studierichting:", fg="#1b709d", font=("Gilroy Light", 20))
        studie_text.place(relx=0.58, rely=oYLS + oY, anchor=CENTER)
        studie_entry = OptionMenu (self, studierighting, *studie_richting_opties)
        studie_entry.configure(bd = 1, indicatoron=0)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        studie_entry.place(relx=oXE, rely=oYES + oY , anchor=CENTER, height=25, width=150)

        #Telefoon
        tel_text = Label(self, text = "Telefoon:", fg="#1b709d", font=("Gilroy Light", 20))
        tel_text.place(relx=0.605, rely=oYLS + oY * 2, anchor=CENTER)
        tel_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        tel_entry.place(relx=oXE, rely=oYES + oY * 2, anchor=CENTER, height=25, width=150)

        #Email ouders
        email_ouders_text = Label(self, text = "Email:", fg="#1b709d", font=("Gilroy Light", 20))
        email_ouders_text.place(relx=0.622, rely=oYLS + oY * 3, anchor=CENTER)
        email_ouders_entry = Entry (self, bd = 1)
        #gegevens_naam.insert(0, "Voornaam")
        #gegevens_naam.bind("<FocusIn>", lambda: gegevens_naam.delete(1.0, END))
        email_ouders_entry.place(relx=oXE, rely=oYES + oY * 3, anchor=CENTER, height=25, width=150)

        cntctbox = Listbox(self, listvariable = StringVar(value =("Ja","Nee")), height = 2, exportselection=False, bg="#502E93", fg="#F9DEE3", font=("Constantia",10),relief = GROOVE)
        cntctbox = Checkbutton(self, text="Wilt u door ons gecontacteerd worden?")
        #cntctbox.bind('<<ListBoxSelect>>', okbutton)

        def gegevens_ingevuld():
            global adressin, numm, eoudin
            naam = naam_entry.get()
            achternaam = achternaam_entry.get()
            leeftijd = leeftijd_entry.get()
            telefoonnummer = tel_entry.get()
            naam_ouder = ouder_entry.get()
            email_kind = email_kind_entry.get()
            email_ouder = email_ouders_entry.get()

            ##### check e-mail

            if(True): #(re.fullmatch(email_regex, email_kind))and(re.fullmatch(email_regex, email_ouder)) and leeftijd.isnumeric() and telefoonnummer.isnumeric():

                ##SEND TO DATABASE

                #klaarbutton.place_forget()
                #emailfout.place_forget()

                #volgendebutton.place_forget()
                cntctbox.place(relx=0.5, rely=0.75, anchor=CENTER)
            
                #volgendebutton.place(relx=0.5, rely=0.9, anchor=CENTER)

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
        b2 = Button(p1, text=" Start! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=p2.lift, activeforeground="#FFFFFF", activebackground="#1b709d")        

        #b1.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        b2.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 

        p1.show()

def new_window():

    #voornaam
    naam_invul = Label(root, text = "voornaam:"
                    , fg="#1b709d", font=("Gilroy Light",15))
    naam_invul.place(relx=0.25, rely=0.4, anchor=CENTER)
    gegevens_naam = Entry (root, bd = 5)
    gegevens_naam.place(relx=0.4, rely=0.4, anchor=CENTER)

    #achternaam
    acnaam_invul = Label(root, text = "naam:"
                    , fg="#1b709d", font=("Gilroy",15))
    acnaam_invul.place(relx=0.25, rely=0.5, anchor=CENTER)
    gegevens_acnaam = Entry (root, bd = 5)
    gegevens_acnaam.place(relx=0.4, rely=0.5, anchor=CENTER)

    #leeftijd
    leef_invul = Label(root, text = "leeftijd:", fg="#1b709d", font=("Gilroy",15))
    leef_invul.place(relx=0.25, rely=0.6, anchor=CENTER)
    gegevens_leef = Entry (root, bd = 5)
    gegevens_leef.place(relx=0.4, rely=0.6, anchor=CENTER)

    #naam ouders
    oudnaam_invul = Label(root, text = "naam ouders:", fg="#1b709d", font=("Gilroy",15))
    oudnaam_invul.place(relx=0.55, rely=0.6, anchor=CENTER)
    gegevens_oudnaam = Entry (root, bd = 5)
    gegevens_oudnaam.place(relx=0.7, rely=0.6, anchor=CENTER)

    #e-mail ouders
    oudadress_invul = Label(root, text = "e-mail adress ouders:", fg="#1b709d", font=("Gilroy",15))
    oudadress_invul.place(relx=0.55, rely=0.5, anchor=CENTER)
    gegevens_oudadress = Entry (root, bd = 5)
    gegevens_oudadress.place(relx=0.7, rely=0.5, anchor=CENTER)

    #studierichting
    studie_invul = Label(root, text = "Welke studierichting inteseert u:"
                        , fg="#1b709d", font=("Gilroy",15))
    studie_invul.place(relx=0.55, rely=0.4, anchor=CENTER)
    studiebox = Listbox(root,listvariable = StringVar(value =("STEM","STEM-wetenschappen","STEM-technieken"))
                        ,height = 3, exportselection=False)
    studiebox.place(relx=0.7, rely=0.4, anchor=CENTER)

    #telefoon ouders
    tel_invul = Label(root, text = "telefoon ouders:"
                        , fg="#1b709d", font=("Gilroy Light",15))
    tel_invul.place(relx=0.55, rely=0.7, anchor=CENTER)
    gegevens_tel = Entry (root, bd = 5)
    gegevens_tel.place(relx=0.7, rely=0.7, anchor=CENTER)

    #e-mail
    adress_invul = Label(root, text = "e-mail adress:"
                        , fg="#1b709d", font=("GILROY LIGHT",15))
    adress_invul.place(relx=0.25, rely=0.7, anchor=CENTER)
    gegevens_adress = Entry (root, bd = 5)
    gegevens_adress.place(relx=0.4, rely=0.7, anchor=CENTER)

    #e-mail requerements
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    #connecteer met database
    #my_conn = my_conn_database_gip()
    #my_connect = my_connect_database_gip()

    numm = ''
        
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
    root.iconbitmap('kovlogo.ico')
    root.attributes('-fullscreen', True)
    root.mainloop()
