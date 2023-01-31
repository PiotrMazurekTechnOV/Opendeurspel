import vraag1_openVraag
import vraag2_multipleChoise
import vraag3_choose
from tkinter import *

vraagKeuze = 0

if vraagKeuze == 0:
    print("0")
    vraag1_openVraag.MyFunction()
elif vraagKeuze == 1:
    print("1")
    vraag2_multipleChoise.MyFunction()
else:
    print("2")
    vraag3_choose.MyFunction()
