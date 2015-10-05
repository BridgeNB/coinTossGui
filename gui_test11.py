__author__ = 'zhengyangqiao'


import Tkinter

class Reminder(object):
    def __init__(self, show_interval=3, hide_interval=6):
        self.hide_int = hide_interval  # In seconds
        self.show_int = show_interval  # In seconds
        self.root = Tkinter.Tk()
        Tkinter.Frame(self.root, width=250, height=100).pack()
        Tkinter.Label(self.root, text='Tossing Coin').place(x=10, y=10)
        self.root.after_idle(self.show)  # Schedules self.show() to be called when the mainloop starts

    def hide(self):
        self.root.withdraw()  # Hide the window
        self.root.after(1000 * self.hide_int, self.show) # Schedule self.show() in hide_int seconds

    def show(self):
        self.root.deiconify() # Show the window
        self.root.after(1000 * self.show_int, self.hide)  # Schedule self.hide in show_int seconds

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    r = Reminder()
    r.start()