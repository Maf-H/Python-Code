#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

# GUI Label demonstration
from tkinter import *


class Label_Demo(Frame):
    """ Demonstration of Labels"""

    def __init__(self):
        """Creating Labels"""

        Frame.__init__(self)  # Initialize inherited Frame class
        # frame fills all available space
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Labels")
        self.master.geometry( "300x120" )  # window size width * length

        self.Label1 = Label(self, text="Label With Text")
        self.Label1.pack()          # Resize frame to accommodate Label

        self.Label2 = Label(self, text="Label With Text and Bitmap")

        # insert Label against left side of frame
        self.Label2.pack(side=LEFT)

        # using default bitmap image as label
        self.Label3 = Label(self, bitmap="question")
        self.Label3.pack(side=RIGHT)


def main():
    Label_Demo().mainloop()  # Starts event loop


if __name__ == "__main__":
    main()
