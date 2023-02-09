import vraag1_openVraag
import vraag2_multipleChoise
import vraag3_choose
from tkinter import *
import database as db

main = Tk()

width = 600
height = 600

def submit():  # Callback function for SUBMIT Button
    klas = textbox.get("1.0", "end-1c")  # For line 1, col 0 to end.
    print(klas)
    idk = db.select_question(klas)
    idkk = db.select_answer(klas)

    type = idk[2]
    vraag = idk[1]
    antwoorden = idkk[1]
    resultaten = idkk[3]

    #database compare klas met ID en vraag de soort
    vraag = str(vraag)
    print(vraag)
    vraagKeuze = str(type)
    print(vraagKeuze)
    antwoorden = str(antwoorden)
    print(antwoorden)
    resultaten = str(resultaten)
    print(resultaten)
    print("--------")


    if vraagKeuze == 0:
            print("0")
            main.destroy()
            vraag1_openVraag.SetUp(vraag,resultaten)
    elif vraagKeuze == 1:
            print("1")
            vraag2_multipleChoise.SetUp(vraag,resultaten,antwoorden)
    elif vraagKeuze == 2:
            print("2")
            main.destroy()
            vraag3_choose.SetUp(vraag,resultaten,antwoorden)
            
c = Canvas(main, width=width, height=height, highlightthickness=0)
c.pack()

textbox = Text(c, width=30, height=1)
textbox.pack()

submitbutton = Button(c, width=10, height=1, text='SUBMIT', command=submit)
submitbutton.pack()

mainloop()