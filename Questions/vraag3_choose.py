import tkinter as tk
from tkinter import *
#import os

#root= Tk()
#root.attributes('-fullscreen', True)

#bg = PhotoImage(file = "../bg_vraag.png")

#imagelabel = Label(root, image = bg)
#imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)
#hallo = Label(root)

        #De SetUp code voor choose
        ##Er moet nog de database code hier in komen.

def SetUp():
    import tkinter as tk
    import os

    vraag = "What is the capital of France?"
    antwoorden = "Paris,Londen,Berlin,Rome"
    correctAnswer = "a"

    antwoordeLijst = antwoorden.split(',')
    print(antwoordeLijst)

    aAntwoord = antwoordeLijst[0]
    bAntwoord = antwoordeLijst[1]
    cAntwoord = antwoordeLijst[2]
    dAntwoord = antwoordeLijst[3]

    print(aAntwoord)
    print(bAntwoord)
    print(cAntwoord)
    print(dAntwoord)

    class Quiz(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Quiz")
            self.question = tk.StringVar()
            self.question.set(vraag)
            self.option_a = tk.StringVar()
            self.option_a.set(aAntwoord)
            self.option_b = tk.StringVar()
            self.option_b.set(bAntwoord)
            self.option_c = tk.StringVar()
            self.option_c.set(cAntwoord)
            self.option_d = tk.StringVar()
            self.option_d.set(dAntwoord)
            self.correct_answer = correctAnswer
            self.v = tk.StringVar()
            self.create_widgets()

        def create_widgets(self):
            question_label = tk.Label(self, textvariable=self.question)
            question_label.pack()
            option_a_button = tk.Radiobutton(self, textvariable=self.option_a, value="a", variable = self.v, command=self.check_answer)
            option_a_button.pack()
            option_b_button = tk.Radiobutton(self, textvariable=self.option_b, value="b", variable = self.v, command=self.check_answer)
            option_b_button.pack()
            option_c_button = tk.Radiobutton(self, textvariable=self.option_c, value="c", variable = self.v, command=self.check_answer)
            option_c_button.pack()
            option_d_button = tk.Radiobutton(self, textvariable=self.option_d, value="d", variable = self.v, command=self.check_answer)
            option_d_button.pack()

        def check_answer(self):
            if self.correct_answer == self.v.get():
                result_label = tk.Label(self, text="Correct!")
            else:
                result_label = tk.Label(self, text="Incorrect!")
            result_label.pack()

    
    quiz = Quiz()
    quiz.mainloop()