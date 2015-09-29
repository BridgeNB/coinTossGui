__author__ = 'zhengyangqiao'


from Tkinter import *

root = Tk()
text = Text(root)

diary = "result"

text.insert(INSERT, diary)
text.pack()

root.mainloop()