from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import tkinter
import re

def SetUp(vraag, resultaten, antwoorden,klas):

    global correct_answer
    print(resultaten)
    if re.search(",",antwoorden) != None:
        answe = antwoorden.split(",")

    if re.search(",",resultaten) != None:
        correct_answers = resultaten.split(",")
        if len(answe) :
            correct_answer = correct_answers + {0}
    else:
        if resultaten == "1":
            correct_answers = [1,0,0]
            if resultaten == "2":
                correct_answers = {0,1,0}
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
        print(correct_answer)
        


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

            global ans_name
            global selected_answers
            selected_answers = [0] * len(qu.answers)
            print(selected_answers)
            global ans_name
            ans_name = [Button] * len(qu.answers)
            
            #Submit button en checker als de resultaat van de speler. Speler nummer moet nog opgevraagd worden.
            def buttonSubmit():
                print("Click!")

            #answer check
            def checkanswer(x):
                print(x)
                selected_answers[x]= 1 if selected_answers[x]==0 else 0

                print(selected_answers)
                global checker

                if selected_answers == correct_answer:
                    print("Correrct!")
                    checker = True
                else:
                    print("Niet Correct!")
                    print(str(selected_answers)+str(correct_answer))
                    checker = False


                
            
            #button generation
            for x in range(0, len(qu.answers)):
                
                ans_name[x] = Button(self, text=str(qu.answers[x]), bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",15), pady=50, width=20, height=1,command=lambda x=x: checkanswer(x))
               
                ans_name[x].place(relx=0.5, rely=rely_v, anchor=N)
                rely_v = rely_v + 0.15 
                

            vraag_label = Label(self, text ="Vraag: " + qu.question, fg="#1b709d", font=("gilroy light",35), pady=50)
            vraag_label.place(relx=0.5, rely=0.20, anchor=N)
        
            submit_button = Button(self, text="Ga door!", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",15), pady=50, width=20, height=1,command=buttonSubmit)
            submit_button.place(relx=0.7, rely=0.8, anchor=N)

        
        

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


SetUp("Klas?","1","Nee,Ja,Mischien","6ICT")