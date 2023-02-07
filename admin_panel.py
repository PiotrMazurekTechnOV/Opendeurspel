from tkinter import *
from tkinter import ttk
from PIL import *
from PIL import ImageTk, Image
    

class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class VragenPagina(Pagina):
   def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)

        vraag_namen = {"vraag1", "vraag2"}
        vragen = {"vraag1": "Ja?", "vraag2": "Nee?"}
        antwoorden = {"vraag1": {"antw1": (True, "juist antwoord"), 
        "antw2": (False, "nee eing ni"), "antw3": (False, "ma echt"), 
        "antw4": (False, "")}, "vraag2": {"antw1": (False, "niet juist antwoord"), 
        "antw2": (False, "nee eing ni"), "antw3": (True, "ma echt"), 
        "antw4": (False, "a")}}

        geselecteerde_vraag = StringVar(self)
        geselecteerde_vraag.set("Selecteer een vraag")

        def vraag_selecteer(vraag):
            vraag_naam.delete(0, END)
            vraag_naam.insert(0, vraag)

            vraag_entry.delete(0, END)
            vraag_entry.insert(0, vragen.get(vraag))

            antwoord1.delete(0, END)
            antwoord1.insert(0, antwoorden.get(vraag).get("antw1")[1])
            antwoord1_checkbox.select() if antwoorden.get(vraag).get("antw1")[0] else antwoord1_checkbox.deselect()

            antwoord2.delete(0, END)
            antwoord2.insert(0, antwoorden.get(vraag).get("antw2")[1])
            antwoord2_checkbox.select() if antwoorden.get(vraag).get("antw2")[0] else antwoord2_checkbox.deselect()

            antwoord3.delete(0, END)
            antwoord3.insert(0, antwoorden.get(vraag).get("antw3")[1])
            antwoord3_checkbox.select() if antwoorden.get(vraag).get("antw3")[0] else antwoord3_checkbox.deselect()

            antwoord4.delete(0, END)
            antwoord4.insert(0, antwoorden.get(vraag).get("antw4")[1])
            antwoord4_checkbox.select() if antwoorden.get(vraag).get("antw4")[0] else antwoord4_checkbox.deselect()

            geselecteerde_vraag.set(vraag)
        
        def vraag_delete():
            vraag_namen.remove(vraag_naam.get())
            vraag_naam.delete(0, END)
            vraag_entry.delete(0, END)

            antwoord1.delete(0, END)
            antwoord1_checkbox.deselect()

            antwoord2.delete(0, END)
            antwoord2_checkbox.deselect()

            antwoord3.delete(0, END)
            antwoord3_checkbox.deselect()

            antwoord4.delete(0, END)
            antwoord4_checkbox.deselect()

            geselecteerde_vraag.set("Selecteer een vraag")
            updateMenu()

        def maak_vraag():
            vraag_namen.add(vraag_naam.get())
            geselecteerde_vraag.set(vraag_naam.get())

            vragen[vraag_naam.get()] = vraag_entry.get()

            antwoorden[vraag_naam.get()] = {"antw1": (check1.get(), antwoord1.get()),
                "antw2": (check2.get(), antwoord2.get()),
                "antw3": (check3.get(), antwoord3.get()),
                "antw4": (check4.get(), antwoord4.get())}

            updateMenu()

        def updateMenu():
            menu = selecteer_vraag["menu"]
            menu.delete(0, "end")
            for string in vraag_namen:
                menu.add_command(label=string, command=lambda value=string: vraag_selecteer(value))

        #selecteer vraag menu
        selecteer_vraag = OptionMenu(self, geselecteerde_vraag, *vraag_namen, command=vraag_selecteer)
        selecteer_vraag.configure(bd = 1, indicatoron=0, height=2, width=20)
        selecteer_vraag.place(relx=0.05, rely=0.175)

        #vraag aanmaak knop
        maak_vraag = Button(self, text="Creer nieuwe vraag", command=maak_vraag)
        maak_vraag.place(relx=0.05, rely=0.05)

        #vraag naam text
        vraag_naam = Entry(self)
        vraag_naam.place(relx=0.05, rely=0.14)

        #vraag delete knop
        delete_vraag = Button(self, text="Verwijder vraag", command=vraag_delete)
        delete_vraag.place(relx=0.05, rely=0.09)

        #vraag text
        vraag_entry = Entry(self)
        vraag_entry.place(relx=0.15, rely=0.14)

        #antwoord1 text
        antwoord1 = Entry(self)
        antwoord1.place(relx=0.05, rely=0.3)


        #antwoord1 checkbox
        check1 = BooleanVar()
        antwoord1_checkbox = Checkbutton(self, text="Correct antwoord", variable=check1)
        antwoord1_checkbox.place(relx=0.05, rely=0.35)

        #antwoord2 text
        antwoord2 = Entry(self)
        antwoord2.place(relx=0.05, rely=0.4)

        #antwoord2 checkbox
        check2 = BooleanVar()
        antwoord2_checkbox = Checkbutton(self, text="Correct antwoord", variable=check2)
        antwoord2_checkbox.place(relx=0.05, rely=0.45)

        #antwoord3 text
        antwoord3 = Entry(self)
        antwoord3.place(relx=0.05, rely=0.5)

        #antwoord3 checkbox
        check3 = BooleanVar()
        antwoord3_checkbox = Checkbutton(self, text="Correct antwoord", variable=check3)
        antwoord3_checkbox.place(relx=0.05, rely=0.55)

        #antwoord4 text
        antwoord4 = Entry(self)
        antwoord4.place(relx=0.05, rely=0.6)

        #antwoord4 checkbox
        check4 = BooleanVar()
        antwoord4_checkbox = Checkbutton(self, text="Correct antwoord", variable=check4)
        antwoord4_checkbox.place(relx=0.05, rely=0.65)

     

        



class AntwoordenPagina(Pagina):
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
        

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = VragenPagina(self)
        p2 = AntwoordenPagina(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        #b1 = Button(p2, text="Klaar!", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=p1.lift, activeforeground="#FFFFFF", activebackground="#1b709d")
        #b2 = Button(p1, text=" Start! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 30), relief= FLAT , command=p2.lift, activeforeground="#FFFFFF", activebackground="#1b709d")        

        #b1.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        #b2.place(relx=.5 ,rely=0.875, relwidth=.15, anchor=CENTER) 

        #titel
        welkom = Label(self, text = "Admin panel"
               , fg="#1b709d", font=("Gilroy Light", 30))
        welkom.place(relx=0.5, rely=0.05, anchor=N)

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.state('zoomed')
    root.title("Admin panel")
    root.iconbitmap('kovlogo.ico')
    #root.attributes('-fullscreen', True)
    root.mainloop()

#Vragen toevoegen/ aanpassen, antwoorden aanpassen


#0 openvraag
#1 meerkeuzevraag 4 antwoorden 1 juist
#2 alle_juiste_antwoorden 4 antwoorden met 2-3 juist