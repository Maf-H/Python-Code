#  Date & Time 29/04/2024, 23:24.
#  @author Mesfin Haftu
from tkinter import *

def create_window():
    # new_window = Toplevel()  # new window on top of the other window, destroying old window will destroy both; but not vice versal.
    new_window = Tk()  # new window independent of other window, you can destroy old on your choice.
    old_window.destroy()  # close out old window and open new window

old_window = Tk()
Button(old_window, text = "Create new window", command = create_window).pack()
old_window.mainloop()
