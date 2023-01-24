import tkinter as tk

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
        self.correct_answers = {"a", "b"}
        self.create_widgets()

    def create_widgets(self):
        question_label = tk.Label(self, textvariable=self.question)
        question_label.pack()
        option_a_check = tk.Checkbutton(self, textvariable=self.option_a, variable=tk.IntVar(), onvalue=1, offvalue=0, command=self.check_answer)
        option_a_check.pack()
        option_b_check = tk.Checkbutton(self, textvariable=self.option_b, variable=tk.IntVar(), onvalue=1, offvalue=0, command=self.check_answer)
        option_b_check.pack()
        option_c_check = tk.Checkbutton(self, textvariable=self.option_c, variable=tk.IntVar(), onvalue=1, offvalue=0, command=self.check_answer)
        option_c_check.pack()
        option_d_check = tk.Checkbutton(self, textvariable=self.option_d, variable=tk.IntVar(), onvalue=1, offvalue=0, command=self.check_answer)
        option_d_check.pack()

    def check_answer(self):
        selected_answers = {
            "a" if option_a_check.get() == 1 else "",
            "b" if option_b_check.get() == 1 else "",
            "c" if option_c_check.get() == 1 else "",
            "d" if option_d_check.get() == 1 else ""
        }
        if selected_answers == self.correct_answers:
            result_label = tk.Label(self, text="Correct!")
        else:
            result_label = tk.Label(self, text="Incorrect!")
        result_label.pack()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.mainloop()