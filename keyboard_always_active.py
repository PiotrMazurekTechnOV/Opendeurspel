'''Popup Keyboard is a module to be used with Python's Tkinter library
It subclasses the Entry widget as KeyboardEntry to make a pop-up
keyboard appear when the widget gains focus. Still early in development.
'''

from tkinter import *


class _PopupKeyboard(Toplevel):
    '''A Toplevel instance that displays a keyboard that is attached to
    another widget. Only the Entry widget has a subclass in this version.
    '''
    
    def __init__(self, parent, attach, x, y, keycolor, textcolor, keysize=2, keyheight=1, font=('Arial', 20)):
        Toplevel.__init__(self, takefocus=1)
        self.attributes('-topmost', 'true')
        #self.focus_force()
        self.overrideredirect(True)
        self.attributes('-alpha',0.95)

        self.parent = parent
        self.attach = attach
        self.keysize = keysize
        self.keyheight = keyheight
        self.font = font
        self.keycolor = keycolor
        self.textcolor = textcolor
        self.x = x
        self.y = y
        
        self._init_keys()

        # resize to fit keys
        self.update_idletasks()
        self.geometry('{}x{}+{}+{}'.format(self.winfo_width(),
                                           self.winfo_height(),
                                           int(self.winfo_width()/2), int(self.winfo_height() * 3.5))) #+ int(keyheight/4)))
        
    def _init_keys(self):
        self.row1 = Frame(self)
        self.row2 = Frame(self)
        self.row3 = Frame(self)
        self.row4 = Frame(self)

        self.row1.grid(row=1)
        self.row2.grid(row=2)
        self.row3.grid(row=3)
        self.row4.grid(row=4)

        self.alpha = {
            'row1' : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←'],
            'row2' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
            'row3' : ['','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',''],
            'row4' : ['↑','u', 'v', 'w', 'x', '␣', 'y', 'z', '.', '@', ""]
            }
        
        for row in self.alpha: # iterate over dictionary of rows
            if row == 'row1':             # TO-DO: re-write this method
                i = 1                     # for readability and functionality
                for k in self.alpha[row]:
                    Button(self.row1,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row2,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row3,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            else:
                i = 3
                for k in self.alpha[row]:
                    if k == '[ space ]':
                        Button(self.row4,
                               text=k,
                               font=self.font,
                               width=self.keysize,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    else:
                        Button(self.row4,
                               text=k,
                               font=self.font,
                               width=self.keysize,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1

    def _init_capital_keys(self):
        self.row1.destroy()
        self.row2.destroy()
        self.row3.destroy()
        self.row4.destroy()

        self.row1 = Frame(self)
        self.row2 = Frame(self)
        self.row3 = Frame(self)
        self.row4 = Frame(self)

        self.row1.grid(row=1)
        self.row2.grid(row=2)
        self.row3.grid(row=3)
        self.row4.grid(row=4)



        self.alpha = {
            'row1' : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←'],
            'row2' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
            'row3' : ['','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',''],
            'row4' : ['↓', 'U', 'V', 'W', 'X', '␣', 'Y', 'Z', '.', '@', ""]
            }

        for row in self.alpha: # iterate over dictionary of rows
            if row == 'row1':             # TO-DO: re-write this method
                i = 1                     # for readability and functionality
                for k in self.alpha[row]:
                    Button(self.row1,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row2,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row3,
                           text=k,
                           font=self.font,
                           width=self.keysize,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            else:
                i = 3
                for k in self.alpha[row]:
                    if k == '[ space ]':
                        Button(self.row4,
                               text=k,
                               font=self.font,
                               width=self.keysize,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    else:
                        Button(self.row4,
                               text=k,
                               font=self.font,
                               width=self.keysize,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1

    def _attach_key_press(self, k):
        if k == '←':
            self.attach.delete(len(self.attach.get())-1, END)
        elif k == '␣':
            self.attach.insert(END, ' ')
        elif k == '❌':
            self.destroy()
        elif k == '↑':
            self._init_capital_keys()
        elif k == '↓':
            self.row1.destroy()
            self.row2.destroy()
            self.row3.destroy()
            self.row4.destroy()
            self._init_keys()
        else:
            self.attach.insert(END, k)

'''
TO-DO: Implement Number Pad
class _PopupNumpad(Toplevel):
    def __init__(self, x, y, keycolor='gray', keysize=5):
        Toplevel.__init__(self, takefocus=0)
        
        self.overrideredirect(True)
        self.attributes('-alpha',0.85)

        self.numframe = Frame(self)
        self.numframe.grid(row=1, column=1)

        self.__init_nums()

        self.update_idletasks()
        self.geometry('{}x{}+{}+{}'.format(self.winfo_width(),
                                           self.winfo_height(),
                                           self.x,self.y))

    def __init_nums(self):
        i=0
        for num in ['7','4','1','8','5','2','9','6','3']:
            print num
            Button(self.numframe,
                   text=num,
                   width=int(self.keysize/2),
                   bg=self.keycolor,
                   command=lambda num=num: self.__attach_key_press(num)).grid(row=i%3, column=i/3)
            i+=1
'''

class KeyboardEntry(Frame):
    '''An extension/subclass of the Tkinter Entry widget, capable
    of accepting all existing args, plus a keysize and keycolor option.
    Will pop up an instance of _PopupKeyboard when focus moves into
    the widget

    Usage:
    KeyboardEntry(parent, keysize=6, keycolor='white').pack()
    '''
    
    def __init__(self, parent, keysize=5, keycolor="white", textcolor="#1b709d", *args, **kwargs):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.entry = Entry(self, *args, **kwargs)
        self.entry.pack()

        self.keysize = keysize
        self.keycolor = keycolor
        self.textcolor = textcolor
        
        
        self.kb = _PopupKeyboard(attach=self.entry,
                                 parent=self.parent,
                                 x=self.entry.winfo_rootx(),
                                 y=self.entry.winfo_rooty() + self.entry.winfo_reqheight(),
                                 keysize=self.keysize,
                                 textcolor=self.textcolor,
                                 keycolor=self.keycolor)

    

def test():  
    root = Tk()
    KeyboardEntry(root, keysize=6, keycolor='white').pack()
#KeyboardEntry(root).pack()
    root.mainloop()

if __name__ == '__main__':
    test()