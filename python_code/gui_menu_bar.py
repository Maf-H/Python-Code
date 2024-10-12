#  Date & Time 26/04/2024, 01:32.
#  @author Mesfin Haftu

from tkinter import *

def new_file():
    print("file created.")
def open():
    print("file opened.")
def save():
    print("file saved.")
    
def copy():
    print("some text copied.")
    
def cut():
    print("some text cuted.")
    
def paste():
    print("some text pasted.")
        
window = Tk()
window.title("Menu Bar")

save_image = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/save.png")
open_image = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/open_file.png")
new_image = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/new_file.png")
exit_image = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/exit.png")


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, image=new_image, compound=LEFT)
file_menu.add_command(label="Open", command=open, image=open_image, compound=LEFT)
file_menu.add_command(label="Save", command=save, image=save_image, compound=LEFT)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy, image=exit_image, compound=LEFT)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Cut", command=cut)

window.mainloop()