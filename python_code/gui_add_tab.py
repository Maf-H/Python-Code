#  Date & Time 29/04/2024, 23:38.
#  @author Mesfin Haftu
from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays

tab1 = Frame(notebook) # new frame for tab 1
tab2 = Frame(notebook) # new frame for tab 2
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill='both')  # expand: fill any space not used
                                                              # fill: fill space on x,y axis
Label(tab1, text='This is tab # 1', width = 50, height = 25).pack()
Label(tab2, text='This is tab # 2 \n See you.', width = 50, height = 25).pack()


window.mainloop()
