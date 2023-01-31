from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re


class question():
    location = "ICT lokaal"
    question_id = "1"
    question = "In welke taal is dit geschreven"
    answers = ["Python", "C#","HTML"]
    
    
    
class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()



class Vraag(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        rely_v = 0.4
        qu = question()
          
        #titel
        location_label = Label(self, text = qu.location, fg="#1b709d", font=("Gilroy Light", 65))
        location_label.place(relx=0.5, rely=0.1, anchor=N)
        
        for x in range(0, len(qu.answers)):
            ans_name = "c" + str(x)
            ans_var = "a" + str(x)
            ans_var = IntVar()
            ans_name = Button(self, text=str(qu.answers[x]), bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",25), pady=50, width=10, height=1)
            ans_name.place(relx=0.5, rely=rely_v, anchor=N)
            rely_v = rely_v + 0.2
        
        vraag_label = Label(self, text ="Vraag: "+ qu.question_id +")  "+qu.question, fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Vraag(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        canvas = Canvas(container, width=1920, height=1080)
        canvas.pack()
        
        #----------------TEXT EN FOTOS OP HETZELFDE MOMENT LUKT NIET DAAROM STAAT ALLES IN COMMENTAAR ------------
        
        #background = PhotoImage(file="bg_vraag.png")
        #canvas.create_image(960,540,image=background)

        #logo = PhotoImage(file="technov-logo.png")
        #canvas.create_image(300,125,image=logo)
        
        #---------------------------------------------------------------------------------------------------------
        
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
    #verander de foto onder de naam bg_vraag.png in file explorer om de achtergrond aan te passen
    root.mainloop()