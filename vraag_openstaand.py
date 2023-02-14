from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import re

def SetUp(vraag,antwoord,klas):
    class question():
        location = klas
        question = vraag
        ans = antwoord
    
    
    
    class Pagina(Frame):
      def __init__(self, *args, **kwargs):
          Frame.__init__(self, *args, **kwargs)
      def show(self):
          self.lift()



    class Vraag(Pagina):
        def __init__(self, *args, **kwargs):
            Pagina.__init__(self, *args, **kwargs)
            qu = question()

            def check_ans():
                input = Vraag().answer_entry.get()
                if input.lower() == qu.ans.lower():
                    print("juist")
                else:
                    print("fout")
                print(input)

            self.submit_button = Button(
            self,
            text="Submit",
            command=check_ans()
            )
            self.submit_button.pack()

            #titel
            location_label = Label(self, text = qu.location, fg="#1b709d", font=("Gilroy Light", 65))
            location_label.place(relx=0.5, rely=0.1, anchor=N)
        
            vraag_label = Label(self, text ="Vraag: "+qu.question, fg="#1b709d", font=("gilroy light",35), pady=50)
            vraag_label.place(relx=0.5, rely=0.25, anchor=N)

            name_entry = Entry(self,textvariable = "ans", font=('calibre',10,'normal'))
            name_entry.place(relx=0.5, rely=0.6, anchor=N)

        

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
        
            klaspng = PhotoImage(file="Klas.png")
            label1 = Label(image=klaspng)
            label1.image = klaspng
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

SetUp("Het juiste antwoord is 1234","1234","Een klas")