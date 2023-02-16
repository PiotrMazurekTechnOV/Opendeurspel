import tkinter as tk

def SetUp(vraag,antwoord):
    class Quiz(tk.Tk):
        def __init__(self, vraag, antwoord):
            tk.Tk.__init__(self)
            self.title("Quiz")
            self.vraag = vraag
            self.antwoord = antwoord
            self.create_widgets()

        def create_widgets(self):
            self.question_label = tk.Label(
            self,
            text=self.vraag,
            font=("TkDefaultFont", 16)
            )   
            self.question_label.pack()

            self.answer_entry = tk.Entry(self, font=("TkDefaultFont", 16))
            self.answer_entry.pack()

            self.submit_button = tk.Button(
            self,
            text="Submit",
            command=self.check_answer
            )
            self.submit_button.pack()

        def check_answer(self):
            input = self.answer_entry.get()
            if input.lower() == self.antwoord.lower():
                self.question_label.config(text="Correct!")
                self.answer_entry.config(state="disabled")
                self.submit_button.config(state="disabled")
            else:
                self.question_label.config(text="Incorrect, try again.")

    quiz = Quiz(vraag, antwoord)
    quiz.mainloop()