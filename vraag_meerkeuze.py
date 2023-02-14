from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re

class question():
    location = "ICT lokaal"
    question = "In welke taal is dit geschreven"
    answers = ["Python", "C#", "Java", "C++"]
    
    
    
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
        
        submit_button = Button(self, text="Verstuur!", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",15), pady=50, width=20, height=1)
        submit_button.place(relx=0.8, rely=0.5, anchor=N)
        
        

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Vraag(self)

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
        
              
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)    
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