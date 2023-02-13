from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re


class question():
    location = "ICT lokaal"
    question = "In welke taal is dit geschreven"
    answers = ["Python", "C#", "Java"]
    
    
    
class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()



class Vraag(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        qu = question()
          
        #titel
        location_label = Label(self, text = qu.location, fg="#1b709d", font=("Gilroy Light", 65))
        location_label.place(relx=0.5, rely=0.1, anchor=N)
        
        vraag_label = Label(self, text ="Vraag: "+qu.question, fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        b1 = Button(self, text="Python", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",25), pady=50, width=10, height=1)
        b2 = Button(self, text="C#", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",25), pady=50, width=10, height=1)
        b3 = Button(self, text="Java", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",25), pady=50, width=10, height=1)
        
        b1.place(relx=0.5, rely=0.4, anchor=N)
        b2.place(relx=0.5, rely=0.6, anchor=N)
        b3.place(relx=0.5, rely=0.8, anchor=N)
        
        

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