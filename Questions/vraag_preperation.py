import vraag1_openVraag
import vraag2_multipleChoise
import vraag3_choose
from tkinter import *
import database as db

vraagKeuze = 4
main = Tk()

if vraagKeuze == 4:

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
        print(resultaten)

        #database compare klas met ID en vraag de soort
<<<<<<< Updated upstream
        vraagKeuze = int(type)
=======
        vraagKeuze = 0
>>>>>>> Stashed changes


        if vraagKeuze == 0:
            print("0")
            main.destroy()
            vraag1_openVraag.SetUp()
        elif vraagKeuze == 1:
            print("1")
            main.destroy()
            vraag2_multipleChoise.SetUp(vraag,resultaten,antwoorden)
        elif vraagKeuze == 2:
            print("2")
            main.destroy()
            vraag3_choose.SetUp()
            
    c = Canvas(main, width=width, height=height, highlightthickness=0)
    c.pack()

    textbox = Text(c, width=30, height=1)
    textbox.pack()

    submitbutton = Button(c, width=10, height=1, text='SUBMIT', command=submit)
    submitbutton.pack()

    mainloop()
elif vraagKeuze == 0:
    print("0")
    vraag1_openVraag.SetUp()
    main.destroy()
elif vraagKeuze == 1:
    print("1")
    vraag2_multipleChoise.SetUp()
    main.destroy()
elif vraagKeuze == 2:
    print("2")
    vraag3_choose.SetUp()
    main.destroy()
else:
    print("err")