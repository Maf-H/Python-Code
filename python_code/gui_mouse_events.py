# Date and Time: 14/04/2024, 21:56
# @author Mesfin Haftu
# Mouse Events:

from tkinter import *

def do_function(event):
    print("Mouse cooerdinates: ", str(event.x), ",", str(event.y))
def do_function2(event):
    print("Right clicked")
def do_function3(event):
    print("Scroll clicked")


window = Tk()
window.title("Mouse Events")
window.bind("<Button-1>", do_function) # takes event (<Button-1>) means left click and do_function
window.bind("<Button-2>", do_function2) # takes event (<Button-1>) means right click and do_function
window.bind("<Button-3>", do_function3) # takes event (<Button-1>) means scroll click and do_function
window.bind("<ButtonRelease>", do_function) # takes event when button is released
window.bind("<Enter>", do_function) # takes event when enter is clicked
window.bind("<Leave>", do_function) # takes event when button is released
window.bind("<Motion>", do_function) # takes event when mouse moves

window.mainloop()