from tkinter import *
from PIL import *
import mysql.connector
import re
from database_gip import *

root= Tk()
root.iconbitmap('kovlogo.ico')

root.attributes('-fullscreen', True)
bg = PhotoImage(file = "bg_inlog.png")

imagelabel = Label(root, image = bg)
imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)

welkom = Label(root, text = "Welkom op de opendeurdag van Technov!"
               ,bg="#BEEBEC", fg="#4572a3", font=("Constantia",30))
welkom.place(relx=0.5, rely=0.2, anchor=CENTER)

#canvas1 = Canvas(root, width = 400, height = 300)
#canvas1.pack()
uitleg = Label(root, text = "Vul u naam en e-mail adres in. Dan krijgt u een nummer"
               ,bg="#A1EAEC", fg="#5B89A5", font=("Constantia",20))
uitleg.place(relx=0.5, rely=0.3, anchor=CENTER)

#voornaam
naam_invul = Label(root, text = "voornaam:"
                   , fg="#5B89A5", font=("Constantia",15))
naam_invul.place(relx=0.25, rely=0.4, anchor=CENTER)
gegevens_naam = Entry (root, bd = 5)
gegevens_naam.place(relx=0.4, rely=0.4, anchor=CENTER)

#achternaam
acnaam_invul = Label(root, text = "naam:"
                   , fg="#5B89A5", font=("Constantia",15))
acnaam_invul.place(relx=0.25, rely=0.5, anchor=CENTER)
gegevens_acnaam = Entry (root, bd = 5)
gegevens_acnaam.place(relx=0.4, rely=0.5, anchor=CENTER)

#leeftijd
leef_invul = Label(root, text = "leeftijd:"
                   , fg="#5B89A5", font=("Constantia",15))
leef_invul.place(relx=0.25, rely=0.6, anchor=CENTER)
gegevens_leef = Entry (root, bd = 5)
gegevens_leef.place(relx=0.4, rely=0.6, anchor=CENTER)

#naam ouders
oudnaam_invul = Label(root, text = "naam ouders:"
                   , fg="#5B89A5", font=("Constantia",15))
oudnaam_invul.place(relx=0.55, rely=0.6, anchor=CENTER)
gegevens_oudnaam = Entry (root, bd = 5)
gegevens_oudnaam.place(relx=0.7, rely=0.6, anchor=CENTER)

#e-mail ouders
oudadress_invul = Label(root, text = "e-mail adress ouders:"
                     , fg="#5B89A5", font=("Constantia",15))
oudadress_invul.place(relx=0.55, rely=0.5, anchor=CENTER)
gegevens_oudadress = Entry (root, bd = 5)
gegevens_oudadress.place(relx=0.7, rely=0.5, anchor=CENTER)

#studierichting
studie_invul = Label(root, text = "Welke studierichting inteseert u:"
                     , fg="#5B89A5", font=("Constantia",15))
studie_invul.place(relx=0.55, rely=0.4, anchor=CENTER)
studiebox = Listbox(root,listvariable = StringVar(value =("STEM","STEM-wetenschappen","STEM-technieken"))
                    ,height = 3, exportselection=False)
studiebox.place(relx=0.7, rely=0.4, anchor=CENTER)

#telefoon ouders
tel_invul = Label(root, text = "telefoon ouders:"
                     , fg="#5B89A5", font=("Constantia",15))
tel_invul.place(relx=0.55, rely=0.7, anchor=CENTER)
gegevens_tel = Entry (root, bd = 5)
gegevens_tel.place(relx=0.7, rely=0.7, anchor=CENTER)

#e-mail
adress_invul = Label(root, text = "e-mail adress:"
                     , fg="#5B89A5", font=("Constantia",15))
adress_invul.place(relx=0.25, rely=0.7, anchor=CENTER)
gegevens_adress = Entry (root, bd = 5)
gegevens_adress.place(relx=0.4, rely=0.7, anchor=CENTER)

#e-mail requerements
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#connecteer met database
my_conn = my_conn_database_gip()
my_connect = my_connect_database_gip()

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
        my_conn.execute(add,val)
        my_connect.commit()

        #volgendebutton.place(relx=0.5, rely=0.7, anchor=CENTER)

        klaarbutton.place_forget()
        emailfout.place_forget()

        volgendebutton.place_forget()
        nummer.configure(text="Wil je door ons gecontacteert worden?",font=("Constantia",30))
        cntctbox.place(relx=0.5, rely=0.75, anchor=CENTER)

        nummer.place(relx=0.5, rely=0.7, anchor=CENTER)

        adressin = gegevens_adress.get()
        my_conn.execute(("SELECT ID FROM users WHERE email = %s"),(adressin,))
        num = my_conn.fetchone()
        my_connect.commit()
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
            my_conn.execute(("UPDATE users SET contact = 1 WHERE ID = %s"),(numm,))
            print (numm)
            my_connect.commit()
        if cntctbox.get(i) == "Nee":
            my_conn.execute(("UPDATE users SET contact = 0 WHERE ID = %s"),(numm,))
            my_connect.commit()
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

klaarbutton = Button(root, text='klaar', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE 
                     , command=klbutton)
klaarbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
volgendebutton = Button(root, text='volgende', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                        , command=vlgndbutton)
emailfout = Label(root, text = "foute e-mail"
                  , bg="#DF3740", font=("Constantia",15),relief = GROOVE)

okbutton = Button(root, text='Ok', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                  , command=okbutton)
finbutton = Button(root, text='Fin', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                  , command=finbutton)
cntctbox = Listbox(root,listvariable = StringVar(value =("Ja","Nee"))
                    ,height = 2, exportselection=False
                   ,bg="#502E93", fg="#F9DEE3", font=("Constantia",10),relief = GROOVE)
cntctbox.bind('<<ListBoxSelect>>', okbutton)
nummer = Label(root)


root.mainloop()
