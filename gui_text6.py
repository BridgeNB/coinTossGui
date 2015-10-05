__author__ = 'zhengyangqiao'


from Tkinter import *
import time
import random

class GridDemo( Frame ):
    def coinToss (self):
        flip = random.randint(0,1)

        if (flip == 0):
            result = "Head"
        else:
            result = "Tail"

        self.label4String1.set(result)

    def reportResult(self):
        flip = random.randint(0,1)

        if (flip == 0):
            result = "Reporter is right"
        else:
            result = "You are right"

        self.label4String2.set(result)


    def __init__(self):

        Frame.__init__(self)

        # Frame(self, width = 100, height = 100)
        self.master.wm_minsize(width = 500, height = 200)
        self.master.title( "Coin Toss Exam" )
        self.variable = "Start Variable"

        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )

        # Toss button
        self.button1 = Button( self, text = "Toss", command = self.coinToss )
        self.button1.grid( row = 1, column = 1,  sticky = W )

        # indication label for reporter
        self.label1 = Label(self, text = "Reporter observed")
        self.label1.grid( row = 2, column = 2, sticky = W )

        # Status button
        self.label4String1 = StringVar()
        self.label2 = Label(self, textvariable=self.label4String1)
        self.label2.grid( row = 3, column = 2, sticky = W )

        # indication label for user selection
        self.label3= Label(self, text = "What do you think?")
        self.label3.grid( row = 4, column = 3, sticky = W )

        # user selection button
        self.button2 = Button( self, text = "Head", command = self.reportResult )
        self.button2.grid( row = 5, column = 3,  sticky = W )

        self.button3 = Button( self, text = "Tail", command = self.reportResult)
        self.button3.grid( row = 5, column = 4,  sticky = W )

        # final result
        self.label4 = Label(self, text = "Final Result")
        self.label4.grid( row = 6, column = 5, sticky = W )

        # final result
        self.label4String2 = StringVar()
        self.label5 = Label(self, textvariable = self.label4String2)
        self.label5.grid( row = 7, column = 5, sticky = W )



def main():
    GridDemo().mainloop()

if __name__ == '__main__':
    main()