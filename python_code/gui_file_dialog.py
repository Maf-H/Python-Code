from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfile()
    print(file_path[0])

window = Tk()
button = Button(window,
                text='Open',
                command=open_file)
button.pack()
window.mainloop()