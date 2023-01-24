import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.attributes('-fullscreen', True)

bg = PhotoImage(file = "bg_vraag.png")

imagelabel = Label(root, image = bg)
imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)

root.mainloop()