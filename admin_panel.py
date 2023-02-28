from tkinter import *
import database

from enum import Enum

class QuestionType(Enum):
    OPEN_VRAAG = 0
    MULTIPLE_CHOICE = 2     
    PICK_ONE = 1

class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class VragenPagina(Pagina):
   def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)

        geselecteerde_vraag = StringVar(self)
        geselecteerde_vraag.set("Selecteer een vraag")

        welkom = Label(self, text = "Welkom op het admin paneel!", font=("Gilroy Light", 25))
        welkom.place(relx=0.45, rely=0.035, anchor=N)

        def creer_nieuwe_vraag():
            #type = QuestionType.OPEN_VRAAG.value
            #if (antwoord2.get() == "" and antwoord3.get() == "" and antwoord4.get() == ""):
            #    type = QuestionType.OPEN_VRAAG.value
            
            correcte_answers_string = ""
            if check1.get():
                correcte_answers_string += "1,"
            if check2.get():
                correcte_answers_string += "2,"
            if check3.get():
                correcte_answers_string += "3,"
            if check4.get():
                correcte_answers_string += "4,"
            #if (len(correcte_answers_string) > 2):
            #    type = QuestionType.MULTIPLE_CHOICE.value
            #else:
            #    type = QuestionType.PICK_ONE.value
            antwoorden = ",".join([antwoord1.get(), antwoord2.get(), antwoord3.get(), antwoord4.get()])
            print(antwoorden)
            database.change_question_with_answer(vraag_naam.get(), vraag_entry.get(), antwoorden, correcte_answers_string)

        def vraag_selecteer(vraag):
            print(vraag)
            if (not vraag):
                return
            question = database.select_question(vraag)
            answers = database.select_answer(vraag)
            print(answers)
            answers_texts = answers[1].split(",")
            correcte_antwoorden = answers[3]

            vraag_naam.delete(0, END)
            vraag_naam.insert(0, vraag)

            vraag_entry.delete(0, END)
            vraag_entry.insert(0, question[1])

            antwoord1.delete(0, END)
            antwoord1.insert(0, answers_texts[0])
            antwoord1_checkbox.select() if "1" in correcte_antwoorden else antwoord1_checkbox.deselect()

            antwoord2.delete(0, END)
            antwoord2.insert(0, answers_texts[1])
            antwoord2_checkbox.select() if "2" in correcte_antwoorden else antwoord2_checkbox.deselect()

            antwoord3.delete(0, END)
            antwoord3.insert(0, answers_texts[2])
            antwoord3_checkbox.select() if "3" in correcte_antwoorden else antwoord3_checkbox.deselect()

            antwoord4.delete(0, END)
            antwoord4.insert(0, answers_texts[3])
            antwoord4_checkbox.select() if "4" in correcte_antwoorden else antwoord4_checkbox.deselect()

            geselecteerde_vraag.set(vraag)
        
        def vraag_delete():
            database.remove_question_and_answer(vraag_naam.get())
            vraag_naam.delete(0, END)
            vraag_entry.delete(0, END)

            antwoord1.delete(0, END)
            antwoord1_checkbox.deselect()

            antwoord2.delete(0, END)
            antwoord2_checkbox.deselect()

            antwoord3.delete(0, END)
            antwoord3_checkbox.deselect()

            antwoord4.delete(0, END)
            antwoord4_checkbox.deselect()

            geselecteerde_vraag.set("Selecteer een vraag")
            updateMenu()

        def maak_vraag():
            creer_nieuwe_vraag()
            geselecteerde_vraag.set(vraag_naam.get())
            vraag_naam.delete(0, END)
            vraag_entry.delete(0, END)

            antwoord1.delete(0, END)
            antwoord1_checkbox.deselect()

            antwoord2.delete(0, END)
            antwoord2_checkbox.deselect()

            antwoord3.delete(0, END)
            antwoord3_checkbox.deselect()

            antwoord4.delete(0, END)
            antwoord4_checkbox.deselect()

            geselecteerde_vraag.set("Selecteer een vraag")
            updateMenu()

        def updateMenu():
            menu = selecteer_vraag["menu"]
            menu.delete(0, "end")
            questions = database.select_all_questions()
            question_names = [question[2] for question in questions]
            for string in question_names:
                menu.add_command(label=string, command=lambda value=string: vraag_selecteer(value))

        questions = database.select_all_questions()
        question_names = [question[2] for question in questions]

        if (len(question_names) == 0):
            question_names = ["Geen vragen gevonden"]

        #selecteer vraag menu
        selecteer_vraag = OptionMenu(self, geselecteerde_vraag, *question_names, command=vraag_selecteer)
        selecteer_vraag.configure(bd = 1, indicatoron=0, height=2, width=20)
        selecteer_vraag.place(relx=0.4, rely=0.275)

        #vraag aanmaak knop
        maak_vraag = Button(self, text="Creer nieuwe vraag", command=maak_vraag)
        maak_vraag.place(relx=0.4, rely=0.15)

        #vraag delete knop
        delete_vraag = Button(self, text="Verwijder vraag", command=vraag_delete)
        delete_vraag.place(relx=0.4, rely=0.19)

        #vraag naam text
        vraag_naam = Entry(self)
        vraag_naam.place(relx=0.4, rely=0.24)

        vraag_naam_label = Label(self, text="Klas naam:")
        vraag_naam_label.place(relx=0.35, rely=0.24)

        #vraag text
        vraag_entry = Entry(self, width=75)
        vraag_entry.place(relx=0.5, rely=0.24)

        vraag_naam_label = Label(self, text="Vraag:")
        vraag_naam_label.place(relx=0.5, rely=0.2)

        #antwoord1 text
        antwoord1 = Entry(self, width=75)
        antwoord1.place(relx=0.4, rely=0.4)

        antwoord1_label = Label(self, text="Antwoord 1:")
        antwoord1_label.place(relx=0.34, rely=0.4)

        #antwoord1 checkbox
        check1 = BooleanVar()
        antwoord1_checkbox = Checkbutton(self, text="Correct antwoord", variable=check1)
        antwoord1_checkbox.place(relx=0.4, rely=0.45)

        #antwoord2 text
        antwoord2 = Entry(self, width=75)
        antwoord2.place(relx=0.4, rely=0.5)

        antwoord2_label = Label(self, text="Antwoord 2:")
        antwoord2_label.place(relx=0.34, rely=0.5)

        #antwoord2 checkbox
        check2 = BooleanVar()
        antwoord2_checkbox = Checkbutton(self, text="Correct antwoord", variable=check2)
        antwoord2_checkbox.place(relx=0.4, rely=0.55)

        #antwoord3 text
        antwoord3 = Entry(self, width=75)
        antwoord3.place(relx=0.4, rely=0.6)

        antwoord3_label = Label(self, text="Antwoord 3:")
        antwoord3_label.place(relx=0.34, rely=0.6)

        #antwoord3 checkbox
        check3 = BooleanVar()
        antwoord3_checkbox = Checkbutton(self, text="Correct antwoord", variable=check3)
        antwoord3_checkbox.place(relx=0.4, rely=0.65)

        #antwoord4 text
        antwoord4 = Entry(self, width=75)
        antwoord4.place(relx=0.4, rely=0.7)

        antwoord4_label = Label(self, text="Antwoord 4:")
        antwoord4_label.place(relx=0.34, rely=0.7)

        #antwoord4 checkbox
        check4 = BooleanVar()
        antwoord4_checkbox = Checkbutton(self, text="Correct antwoord", variable=check4)
        antwoord4_checkbox.place(relx=0.4, rely=0.75)

        

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = VragenPagina(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)     

        #b1 = Button(p2, text="Klaar!", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 20), relief= FLAT , command=p1.lift, activeforeground="#FFFFFF", activebackground="#1b709d")
        #b2 = Button(p1, text=" Start! ", bg="#D5DF3A", fg="#FFFFFF", font=("Gilroy", 30), relief= FLAT , command=p2.lift, activeforeground="#FFFFFF", activebackground="#1b709d")        

        #b1.place(relx=.5 ,rely=0.875, relwidth=.1, anchor=CENTER) 
        #b2.place(relx=.5 ,rely=0.875, relwidth=.15, anchor=CENTER) 

        #titel
        welkom = Label(self, text = "Admin panel"
               , fg="#1b709d", font=("Gilroy Light", 30))
        welkom.place(relx=0.4, rely=0.05, anchor=N)

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.state('zoomed')
    root.title("Admin panel")
    #root.iconbitmap('kovlogo.ico')
    #root.attributes('-fullscreen', True)
    root.mainloop()

#Vragen toevoegen/ aanpassen, antwoorden aanpassen


#0 openvraag
#1 meerkeuzevraag 4 antwoorden 1 juist
#2 alle_juiste_antwoorden 4 antwoorden met 2-3 juist