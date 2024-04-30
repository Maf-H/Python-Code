# Date and Time: 14/04/2024, 21:56
# @author Mesfin Haftu
# Key Events:

from tkinter import *

def do_function(event):
    # print("You pressed: ", event.keysym)
    label.config(text=event.keysym) # event.keysym grabs each keys pressed
window = Tk()
window.title("Events")
# key loggers can be build with the bind() method
window.bind("<Key>", do_function) # binds the event (<Enter>) to the function (do_function) to use all keys:(<Key>)

label = Label(window, font=("Helvetica", 100))
label.pack()
window.mainloop()