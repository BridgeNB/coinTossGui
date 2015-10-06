__author__ = 'zhengyangqiao'

import Tkinter as tk
import random as rd
import sys


TITLE_FONT = ("Helvetica", 50, "bold")

repeatTime = 3

class coinToss(tk.Tk):
    container = False

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.configure(height = 100, width = 100)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(10, weight = 1)
        container.grid_columnconfigure(10, weight = 1)

        # Stack all the frames in the same location
        self.frames = {}
        for F in (PageOne, PageTwo, PageThree,
                  PageFour, PageFive, PageSix,
                  PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=5, column=5, sticky="nsew")

        # need more progress
        self.show_frame(PageOne)
        showTime_pageOne = 3000 + self.randomTime(4, 1000)
        self.after(showTime_pageOne, lambda:self.close_page(PageOne))
        self.after(showTime_pageOne, lambda:self.show_frame(PageTwo))

        showTime_pageTwo = showTime_pageOne + 5000 + self.randomTime(4, 1000)
        self.after(showTime_pageTwo, lambda:self.close_page(PageTwo))
        self.after(showTime_pageTwo, lambda:self.show_frame(PageThree))

        showTime_pageThree = showTime_pageTwo + 1000
        self.after(showTime_pageThree, lambda:self.close_page(PageThree))
        self.after(showTime_pageThree, lambda:self.show_frame(PageFour))

        showTime_pageFour = showTime_pageThree + 500
        self.after(showTime_pageFour, lambda:self.close_page(PageFour))
        self.after(showTime_pageFour, lambda:self.show_frame(PageFive))

        showTime_pageFive = showTime_pageFour + 800
        self.after(showTime_pageFive, lambda:self.close_page(PageFive))
        self.after(showTime_pageFive, lambda:self.show_frame(PageSix))

        showTime_pageSix =  showTime_pageFive + 500
        self.after(showTime_pageSix, lambda:self.close_page(PageSix))
        self.after(showTime_pageSix, lambda:self.show_frame(PageSeven))

        showTime_pageSeven = showTime_pageSix + 4500
        print showTime_pageSeven
        self.after(showTime_pageSeven,lambda:self.destroy())
        self.quit()


    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
        # frame.after(5000, self.close_pageOne(c))


    def close_page(self,c):
        '''Close a frame after certain time'''
        frame = self.frames[c]
        frame.destroy()  # Hide the window
        # frame.after(10000, self.show_frame(PageTwo))

    def randomTime (self, sValue, eValue):
        '''give an int type of random time interval'''
        randomTime = rd.randint(sValue, eValue)
        return randomTime


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent.master.wm_minsize(width = 1000, height = 1000)
        label = tk.Label(self, text="Toss Coin", font=TITLE_FONT)
        # label.grid(row = 50, column = 50, sticky = "nesw")
        label.pack(expand ="true", side= "bottom", fill= "both")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Showing Outcome to Reporter", font=TITLE_FONT)
        label.pack(expand ="true", side= "bottom", fill= "both")

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The reporter says", font=TITLE_FONT)
        label.pack(expand ="true", side= "bottom", fill= "both")

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="", font=TITLE_FONT)
        label.pack(expand ="true", side= "bottom", fill= "both", pady=10)

class PageFive(tk.Frame):

    def Toss (self):
        '''This function is for simulate the coin flip'''
        flip = rd.randint(0,1)

        if (flip == 0):
            result = "Head"
        else:
            result = "Tail"

        # self.label4String.set(result)
        return result

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label_title = tk.Label(self, text="Result", font=TITLE_FONT)
        # label_title.pack(side="top", fill=None, pady=10)
        tem = self.Toss()
        self.label_result = tk.Label(self, text=tem, font = TITLE_FONT)
        self.label_result.pack(expand ="true", side= "bottom", fill= "both", pady=10)

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Your guess?", font = TITLE_FONT)
        label.pack(expand ="true", side= "bottom", fill= "both", pady=10)


class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="HEADS", font = TITLE_FONT)
        button1.grid(row = 5, column = 5, sticky = "w")
        # button2 = tk.Button(self, text="TAILS", font = TITLE_FONT)
        #
        # # button1.grid(row = 3, column = 20, sticky = "w")
        # button1.pack()
        #
        # button2.pack(expand ="true", side = "right")
        # # button2.pack(side = "bottom")

for i in range(0, 2):
    app = coinToss()
    app.mainloop()



