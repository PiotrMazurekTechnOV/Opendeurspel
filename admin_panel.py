from tkinter import *
from PIL import *
from PIL import ImageTk, Image
    

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

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    #root.iconbitmap('kovlogo.ico')
    #root.attributes('-fullscreen', True)
    root.mainloop()