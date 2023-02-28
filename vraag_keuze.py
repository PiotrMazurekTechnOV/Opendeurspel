from tkinter import * 
from PIL import *
from PIL import ImageTk, Image
import tkinter
from tkinter import messagebox
import re
from keyboard_new import KeyboardEntry
import database as database


class Pagina(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Vraag(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self ,*args, **kwargs)
        self.location = "IICT"
        self.id = ""
        self.question = ""
        self.buttons = []
        self.activated_buttons = []

        answers = [1, 2, 3]
        question = "Wa?"

        location_label = Label(self, text = self.location, fg="#1b709d", font=("Gilroy Light", 65))
        location_label.place(relx=0.5, rely=0.1, anchor=N)
        self.location_label = location_label

        vraag_label = Label(self, text ="Vraag: " + self.question, fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.20, anchor=N)
        self.vraag_label = vraag_label
             

    def change_location(self, location):
        self.destroy_buttons()
        self.location = location

        database_question_info = database.select_question(self.location)
        database_answer_info = database.select_answer(self.location)
        self.question = database_question_info[1]

        self.answers = list(filter(None, database_answer_info[1].split(",")))
        self.correct_answers = list(filter(None,database_answer_info[3].split(",")))

        self.location_label.config(text=self.location)
        self.vraag_label.config(text="Vraag: " + self.question)
        self.generate_buttons()

    
    def change_id(self, id):
        self.id = id

    def button_activated(self, index: int):
        print(self.activated_buttons)
        if (len(self.correct_answers) <= 1):
            for button in self.buttons:
                if (button):
                    button.config(bg="#D5DF3A")
            self.buttons[index].config(bg="#1b709d")
            self.activated_buttons = index
        else:
            if (self.activated_buttons[index]):
                self.activated_buttons[index].config(bg="#D5DF3A")
                self.activated_buttons[index] = None
            else:
                self.activated_buttons[index] = self.buttons[index]
                self.activated_buttons[index].config(bg="#1b709d")


    def generate_buttons(self):
        self.buttons = [None] * len(self.answers)
        self.activated_buttons = self.buttons.copy()
        rely_v = 0.35
        for x in range(0, len(self.answers)):
            self.buttons[x] = Button(self, name=str(x),text=str(self.answers[x]), bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",15), pady=50, width=20, height=1, command=lambda x=x: self.button_activated(x))
            self.buttons[x].place(relx=0.5, rely=rely_v, anchor=N)
            rely_v = rely_v + 0.15

    def destroy_buttons(self):
        for button in self.buttons:
            if (button):
                button.destroy()
        self.activated_buttons = []

    def get_score(self):
        answers = []
        if (type(self.activated_buttons) == int):
            return 2 if str(self.activated_buttons + 1) in self.correct_answers else 0

        for i in range(1, len(self.buttons) + 1):
            if (self.activated_buttons[i-1] and str(i) in self.correct_answers):
                answers.append(2)
        return (sum(answers), len(self.correct_answers))

    def clear_buttons(self):
        self.destroy_buttons()
        self.generate_buttons()
        

class login_locatie(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        
        entry_font = ("Gilroy Light", 45)
        
        vraag_label = Label(self, text ="Waar staat dit scherm?", fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        locatie_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        locatie_entry.place(relx=0.5, rely=0.45, anchor=CENTER, height=85, width=1000)
        self.locatie_entry = locatie_entry.entry
    
    def get_location(self):
        return self.locatie_entry.get()

        
class login_mensen(Pagina):
    def __init__(self, *args, **kwargs):
        Pagina.__init__(self, *args, **kwargs)
        
        entry_font = ("Gilroy Light", 45)
        
        vraag_label = Label(self, text ="Wat is je ID?", fg="#1b709d", font=("gilroy light",35), pady=50)
        vraag_label.place(relx=0.5, rely=0.25, anchor=N)
        
        id_entry = KeyboardEntry(self, bd = 1, font=entry_font)
        id_entry.place(relx=0.5, rely=0.45, anchor=CENTER, height=85, width=1000)
        self.id_entry = id_entry.entry

    def get_id(self):
        return self.id_entry.get()

    def clear_id(self):
        return self.id_entry.delete(0, END)

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

        def loginLocationChanged():
            print("loginLocationChanged")
            location = p1.get_location()
            if (database.select_question(location) == None):
                messagebox.showerror("Fout", "Locatie niet gevonden")
                return
            p3.change_location(location)
            p2.lift()

        def idChanged():
            user_id = p2.get_id()
            if (database.select_user_by_user_id(user_id) == None):
                messagebox.showerror("Fout", "ID niet gevonden")
                return
            p3.change_id(user_id)
            p2.clear_id()
            p3.lift()

        def sendAnswer():
            print(p3.get_score(), p3.id, p3.location)
            score = p3.get_score()
            if type(score) != int:
                score = score[0] / score[1]
            database.insert_result(p3.id, p3.location, score)
            messagebox.showinfo("Gelukt", "Je antwoord is verzonden")
            p3.clear_buttons()
            p2.lift()

        plaats_btn = Button(p1, text="Plaats", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command=loginLocationChanged)
        plaats_btn.place(relx=0.5, rely=0.525, anchor=N)
        
        login_btn = Button(p2, text="Log in", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command=idChanged)
        login_btn.place(relx=0.5, rely=0.525, anchor=N)
        
        ans_name = Button(p3, text="Verstuur!", bg="#D5DF3A", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#1b709d", font=("gilroy light",30), pady=50, width=20, height=1, command=sendAnswer)
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