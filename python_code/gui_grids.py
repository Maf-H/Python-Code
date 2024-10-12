#  Date & Time 29/04/2024, 23:52.
#  @author Mesfin Haftu
#  grid is a geometry ,manager that organizes widgets in tabular form.
from tkinter import *


def submit():
    print("Full Name: ", first_name_entry.get(), last_name_entry.get(), "\nemail:", email_entry.get())


window = Tk()
window.title("Grids")

Label(window, text="Enter Your info", font=("Aerial", "20")).grid(row=0, column=0, columnspan=2)
Label(window, text="First Name: ").grid(row=1, column=0)
first_name_entry = Entry(window)
first_name_entry.grid(row=1, column=1)
Label(window, text="First Name: ").grid(row=2, column=0)
last_name_entry = Entry(window)
last_name_entry.grid(row=2, column=1)
Label(window, text="email ").grid(row=3, column=0)
email_entry = Entry(window)
email_entry.grid(row=3, column=1)
Button(window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)  #  size column = 2 column
#  label size will be to the size of largest label size

window.mainloop()
