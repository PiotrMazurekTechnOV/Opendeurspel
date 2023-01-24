from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re

class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class HomePagina(Pagina):
   def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        
class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    root.attributes('-fullscreen', True)
    root.wm_geometry("400x400")
    root.iconbitmap('kovlogo.ico')
    root.title('opendeurdag')
    
    #verander de foto onder de naam bg_vraag.png in file explorer om de achtergrond aan te passen
    bgimg= PhotoImage(file = "bg_vraag.png")
    limg= Label(root, i=bgimg)
    limg.pack()
    root.mainloop()