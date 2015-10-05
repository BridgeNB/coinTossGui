__author__ = 'zhengyangqiao'


from Tkinter import *

root = Tk()
root.after(5000, lambda: root.focus_force())
root.mainloop()