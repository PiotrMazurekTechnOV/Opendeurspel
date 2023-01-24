import tkinter as tk
from tkinter import *
import os

root= Tk()
root.attributes('-fullscreen', True)

bg = PhotoImage(file = "../bg_vraag.png")

imagelabel = Label(root, image = bg)
imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)
hallo = Label(root)










class Quiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz")
        self.question = tk.StringVar()
        self.question.set("What is the capital of France?")
        self.option_a = tk.StringVar()
        self.option_a.set("Paris")
        self.option_b = tk.StringVar()
        self.option_b.set("London")
        self.option_c = tk.StringVar()
        self.option_c.set("Berlin")
        self.option_d = tk.StringVar()
        self.option_d.set("Rome")
        self.correct_answer = "a"
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

if __name__ == "__main__":
    quiz = Quiz()
    quiz.mainloop()