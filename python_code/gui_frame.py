#  Date & Time 26/04/2024, 01:32.
#  @author Mesfin Haftu
# Frame is a rectangular container to group and hold widgets

from tkinter import *

window = Tk()
window.title("Frame")
window.config(bg="#27476E")
frame = Frame(window, bg="Pink", bd=5, relief = SUNKEN)
# frame.place(x=0, y=0)
# anonymous buttons
Button(frame, text='W', font=("Console", 25), width = 3).pack(side=TOP)
Button(frame, text='A', font=("Console", 25), width = 3).pack(side=LEFT)
Button(frame, text='S', font=("Console", 25), width = 3).pack(side=LEFT)
Button(frame, text='D', font=("Console", 25), width = 3).pack(side=LEFT)

frame.pack(side=BOTTOM)
window.mainloop()
