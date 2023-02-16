from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import tkinter
import re
from keyboard_new import KeyboardEntry

def SetUp(vraag, resultaten, antwoorden,klas):
    if re.search(",",antwoorden) != None:
        answe = antwoorden.split(",")

    if re.search(",",resultaten) != None:
        correct_answers = resultaten.split(",")
        if len(answe) :
            correct_answer = correct_answers + {0}
    else:
        if resultaten == "1":
            correct_answers = {1}
            if len(answe) :
                correct_answer = correct_answers + {0}
            if resultaten == "2":
                correct_answers = {0,1}
                if len(answe) :
                    correct_answer = correct_answers + {0}
            if resultaten == "3":
                correct_answers = {0,0,1}
                if len(answe) :
                    correct_answer = correct_answers + {0}
            if resultaten == "4":
                correct_answers = {0,0,0,1}
                if len(answe) :
                    correct_answer = correct_answers + {0}
            
            #self.correct_answers = {"a", "b","c","nd",None}  -- oude code
        correct_answer = correct_answers


    ##############################################################################

    class question():
        location = klas
        question = vraag
        answers = answe
    
    
    
    class Pagina(Frame):
        def __init__(self, *args, **kwargs):
            Frame.__init__(self, *args, **kwargs)
        def show(self):
            self.lift()



class Vraag(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        qu = question()
        rely_v = 0.35
        #titel
        location_label = Label(self, text = qu.location, fg="#1b709d", font=("Gilroy Light", 65))
        location_label.place(relx=0.5, rely=0.1, anchor=N)

        self.answers = [None] * len(qu.answers)
        
        def button_activated(index: int):
            print(self.answers[index])
            if (self.answers[index]):
                for button in self.answers:
                  if (button):
                       button.config(bg="#D5DF3A")
                self.answers[index].config(bg="#1b709d")

        #button generation
        for x in range(0, len(qu.answers)):
            self.answers[x] = Button(self, name=str(x),text=str(qu.answers[x]), bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",15), pady=50, width=20, height=1, command=lambda x=x: button_activated(x))
            self.answers[x].place(relx=0.5, rely=rely_v, anchor=N)
            print(self.answers)
            rely_v = rely_v + 0.15
        
        vraag_label = Label(self, text ="Vraag: " + qu.question, fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.20, anchor=N)

class login_locatie(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        
        entry_font = ("Gilroy Light", 45)
        
        vraag_label = Label(self, text ="Waar staat dit scherm?", fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        naam_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        naam_entry.place(relx=0.5, rely=0.45, anchor=CENTER, height=85, width=1000)
        
class login_mensen(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        
        entry_font = ("Gilroy Light", 45)
        
        vraag_label = Label(self, text ="Wat is je ID?", fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        naam_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        naam_entry.place(relx=0.5, rely=0.45, anchor=CENTER, height=85, width=1000)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = login_locatie(self)
        p2 = login_mensen(self)
        p3 = Vraag(self)
            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
        
            canvas = Canvas(container, width=1920, height=1080)
            canvas.pack()

            logo = PhotoImage(file="technov-logo.png")
            label1 = Label(image=logo)
            label1.image = logo
            label1.place(x=1, y=1)
        
            kalspng = PhotoImage(file="Klas.png")
            label1 = Label(image=kalspng)
            label1.image = kalspng
            label1.place(relx=0.81, rely=0.85)
        

        plaats_btn = Button(p1, text="Plaats", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command=p2.lift)
        plaats_btn.place(relx=0.5, rely=0.525, anchor=N)
        
        login_btn = Button(p2, text="Log in", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command=p3.lift)
        login_btn.place(relx=0.5, rely=0.525, anchor=N)
        
        ans_name = Button(p3, text="Verstuur!", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command= p2.lift)
        ans_name.place(relx=0.8, rely=0.5, anchor=N)
        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)    
        p1.show()

    if __name__ == "__main__":  
        root = Tk()
        main = MainView(root)
    
        root.wm_geometry("400x400")
        root.attributes('-fullscreen', True)
        root.iconbitmap('kovlogo.ico')
        root.title('opendeurdag')
        main.pack(side="top", fill="both", expand=True)
        root.mainloop()


SetUp("Klas?","1","Nee,Ja,Mischien","6ICT")