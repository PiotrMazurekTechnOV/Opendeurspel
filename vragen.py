import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
#Imports

root = Tk()
root.attributes('-fullscreen', True)
#Screen Settings

bg = PhotoImage(file = "bg_vraag.png")
#Achtergrond

vraagzin = ''
naam = ''
antzin= ''
IDin = 0
punt = 0
#Variabellen


def lgnbutton():
    global naam, IDin, hallotekst
    #IDin = login.get()         Login id krijgen

    #Database
    mail = "kaan"
    name = "kaan"
    #Database

    ##bestaat het nummer
    if(mail == "None"):
        hallo.configure(text = "ongeldig nummer"
                            , bg="#DF3740", font=("Constantia",35),relief = GROOVE)
        okbutton.configure(text='Ok',
                            font=("Constantia",35))
        okbutton.place(relx=0.8, rely=0.5, anchor=CENTER)
    else:
        #om hallo tegen de gebruiker te, gebruiker kan nu ook terug gaan
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


root.mainloop()