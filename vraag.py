from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re

class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Vraag(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Vraag(self)
         
     
        
        
if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    
    canvas = Canvas(root, width=1920, height=1080, bd=0)
    canvas.pack()


    background = PhotoImage(file="bg_vraag.png")
    canvas.create_image(960,540,image=background)

    character = PhotoImage(file="technov-logo.png")
    canvas.create_image(300,125,image=character)
    
    
    root.attributes('-fullscreen', True)
    root.wm_geometry("400x400")
    root.iconbitmap('kovlogo.ico')
    root.title('opendeurdag')
    
    #verander de foto onder de naam bg_vraag.png in file explorer om de achtergrond aan te passen
    root.mainloop()