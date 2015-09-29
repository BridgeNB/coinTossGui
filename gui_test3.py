__author__ = 'zhengyangqiao'

from Tkinter import *
import random

def hello(event):
    print("Single Click, Button-l")

def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

def coinToss(event):
    global result

    flip = random.randint(0,1)

    if (flip == 0):
        result = "Head"
    else:
        result = "Tail"

    print(result)
    return result

widget = Button(None, text='Mouse Clicks')
# widget.pack()
widget = Message(None, textvariable = coinToss(1), relief = 'flat')
widget.pack()
widget.bind('<Button-1>', coinToss)
widget.bind('<Double-1>', quit)
widget.mainloop()