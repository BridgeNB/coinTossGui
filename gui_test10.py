__author__ = 'zhengyangqiao'

import Tkinter as tk


TITLE_FONT = ("Helvetica", 18, "bold")


class coinToss(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


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
            frame.grid(row=0, column=0, sticky="nsew")


        # self.after_idle(self.show_frame(PageOne))
        # self.start_page_close(PageOne)
        # self.root.after_idle(self.start_page_close())
        # self.show_frame(PageOne)
        # PageOne.show_frame()
        self.show_frame(PageOne)
        self.after(5000, lambda:self.quit())

    # def show_frame(self):
    #     self.tkraise(self);

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
        # frame.after(5000, self.close_pageOne(c))


    def close_pageOne(self,c):
        '''Close a frame after certain time'''
        frame = self.frames[c]
        frame.destroy()  # Hide the window
        # frame.after(10000, self.show_frame(PageTwo))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Toss Coin", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Showing Outcome to Reporter", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The reporter says", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is a blank page.", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="You Guess.", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="HEADS",
                            command=lambda: controller.show_frame(PageOne))


        button2 = tk.Button(self, text="TAILS",
                           command=lambda: controller.show_frame(StartPage))

        button1.pack()
        button2.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Your guess?", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page seven", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)



if __name__ == "__main__":
    app = coinToss()
    app.mainloop()