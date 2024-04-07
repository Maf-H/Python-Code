#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

# GUI Label demonstration
from tkinter import *
from tkinter.messagebox import showinfo


class Entry_Demo(Frame):
    """ Demonstration of Labels"""

    def __init__(self):
        """Creating Labels"""

        Frame.__init__(self)  # Initialize inherited Frame class
        # frame fills all available space
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Entry")
        self.master.geometry( "325x100" )  # window size width * length

        self.frame1 = Frame(self)
        self.frame1.pack(pady = 5)

        self.text1 = Entry(self.frame1, name = "text1")
        self.text1.bind("<Return>", self.show_contents)         # bind the Entry component to event
        self.text1.pack(side = LEFT, padx = 5)

        self.text2 = Entry(self.frame1, name = "text2")
        self.text2.insert(INSERT, "Enter Text Here:") # Instead of INSERT if I put END The text inserted is append at
        # the end of text
        self.text2.bind("<Return>", self.show_contents)  # Tells to listen the event
        self.text2.pack(side = LEFT, padx = 5) # packs the textfield inside a frame

        self.frame2 = Frame(self)
        self.frame2.pack(pady = 5)

        self.text3 = Entry(self.frame2, name = "text3")
        self.text3.insert(INSERT,  "Un-editable Text Field")
        self.text3.config(state =  DISABLED)   # prohibit user from altering text in Entry component text3
        self.text3.bind("<Return>", self.show_contents)
        self.text3.pack(side = LEFT, padx = 5)

        self.text4 = Entry(self.frame2, name = "text4", show = "*") # text in Entry component text4 appears as *
        self.text4.insert(INSERT, "Hidden Text")
        self.text4.bind("<Return>", self.show_contents)
        self.text4.pack(side = LEFT, padx = 5)
    def show_contents(self, event):
        """Display the content of the entry."""
        the_name = event.widget.winfo_name()# acquire name of Entry component that generated event
        the_contents = event.widget.get()  # acquire contents of Entry component that generated event
        showinfo("Message", the_name + " : " + the_contents)

def main():
    Entry_Demo().mainloop()  # Starts event loop


if __name__ == "__main__":
    main()
