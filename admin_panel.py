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

        geselecteerde_vraag = StringVar(self)
        vragen = ["vraag1", "vraag2"]

        #selecteer vraag menu
        selecteer_vraag = OptionMenu(self, geselecteerde_vraag, *vragen)
        selecteer_vraag.configure(bd = 1, indicatoron=0, height=2, width=10)
        selecteer_vraag.place(relx=0.5, rely=0.2, anchor=N)

        #vraag aanmaak knop
        maak_vraag = Button(self, text="Creer nieuwe vraag")
        maak_vraag.place(relx=0.5, rely=0.3, anchor=N)

        #vraag naam text
        vraag_naam = Entry(self)
        vraag_naam.place(relx=0.5, rely=0.35, anchor=N)

        #vraag delete knop
        delete_vraag = Button(self, text="Verwijder vraag")
        delete_vraag.place(relx=0.5, rely=0.4, anchor=N)

        #weizig antwoorden vraag knop
        antwoorden_aanpassen = Button(self, text="Antwoorden aanpassen")
        antwoorden_aanpassen.place(relx=0.5, rely=0.45, anchor=N)

        #toon alle antwoorden treeview
        antwoorden = ttk.Treeview(self)
        antwoorden.place(relx=0.5, rely=0.5, anchor=N)

        def itemClicked(self):
            print("a", antwoorden.focus())

        antwoorden.insert('', 'end', text="Antwoord 1", tags=('ttk',))
        antwoorden.tag_bind('ttk', '<1>', itemClicked) 
        



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