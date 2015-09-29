__author__ = 'zhengyangqiao'

import Tkinter as tk
import random
import tkMessageBox as tb

LARGE_FONT= ("Verdana", 12)

class TossCoinApp(tk.Tk):

    global result

    result = ""

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def coinToss(self):
    # global result

    flip = random.randint(0,1)

    if (flip == 0):
        result = "Head"
    else:
        result = "Tail"

    print(result)
    return result

def showCoinToss(label):

    flip = random.randint(0,1)

    if (flip == 0):
        result = "Head"
    else:
        result = "Tail"

    tb.showinfo("Toss Result", result)

class StartPage(tk.Frame):

    global result

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Toss",
                            command=lambda: coinToss(1))
        button.pack()

        button2 = tk.Button(self, text="Yes",
                            command=lambda: showCoinToss(1))
        button2.pack()

        button3 = tk.Button(self, text="No",
                            command=lambda: coinToss(1))
        button3.pack()

        w = tk.Label(self, text = result)

        w.pack()



app = TossCoinApp()
app.mainloop()