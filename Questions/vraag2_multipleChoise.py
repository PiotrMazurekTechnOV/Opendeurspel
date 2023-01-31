import tkinter as tk

## Option_a_check is niet zichtbaar voor check en is dus niet bruikbaar op lijn 45-50 
## Zie benden!

# option_a_check = datbase
# option_b_check = datbase
# option_c_check = datbase
# option_d_check = datbase
def SetUp():

    class Quiz(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Quiz")
            self.question = tk.StringVar()
            self.question.set("Which are the colors of the French flag?")
            self.option_a = tk.StringVar()
            self.option_a.set("Red")
            self.option_b = tk.StringVar()
            self.option_b.set("White")
            self.option_c = tk.StringVar()
            self.option_c.set("Blue")
            self.option_d = tk.StringVar()
            self.option_d.set("Green")
            self.correct_answers = {"a", "b","c","nd",None}
            self.create_widgets()

        def create_widgets(self):

            global varA
            global varB
            global varC
            global varD

            varA = tk.IntVar()
            varB = tk.IntVar()
            varC = tk.IntVar()
            varD = tk.IntVar()

            question_label = tk.Label(self, textvariable=self.question)
            question_label.pack()
            option_a_check = tk.Checkbutton(self, textvariable=self.option_a, variable=varA, onvalue=1, offvalue=0, command=self.check_answer)
            option_a_check.pack()
            option_b_check = tk.Checkbutton(self, textvariable=self.option_b, variable=varB, onvalue=1, offvalue=0, command=self.check_answer)
            option_b_check.pack()
            option_c_check = tk.Checkbutton(self, textvariable=self.option_c, variable=varC, onvalue=1, offvalue=0, command=self.check_answer)
            option_c_check.pack()
            option_d_check = tk.Checkbutton(self, textvariable=self.option_d, variable=varD, onvalue=1, offvalue=0, command=self.check_answer)
            option_d_check.pack()

        def check_answer(self):
            selected_answers = {
                ######################################################
                "a" if varA.get() == 1 else "na",
                print(varA.get()),
                "b" if varB.get() == 1 else "nb",
                print(varB.get()),
                "c" if varC.get() == 1 else "nc",
                print(varC.get()),
                "d" if varD.get() == 1 else "nd",
                print(varD.get())
                ######################################################
            }
            if selected_answers == self.correct_answers:
                result_label = tk.Label(self, text="Correct!")
                print("")
                print(selected_answers)
                print(self.correct_answers)
                print("---")
            else:
                result_label = tk.Label(self, text="Incorrect!")
                print("")
                print(selected_answers)
                print(self.correct_answers)
                print("---")
            selected_answers.clear()
            result_label.pack()


    quiz = Quiz()
    quiz.mainloop()