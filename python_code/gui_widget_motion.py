# Date and Time 14/04/2024, 21:56.
# @author Mesfin Haftu
# we can move widget or label by passing it's label.place(x, y)

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
    
def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())
    
def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())
    
from tkinter import *

window = Tk()
window.title("Motion of Widgets")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

my_image = PhotoImage(file="kali_icon.png") 
label = Label(window, image=my_image)
label.place(x=0, y=0)

window.mainloop()