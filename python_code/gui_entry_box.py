#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from tkinter import *

window = Tk()
window.title("Entry Box")
window.geometry("300x150")


def submit():
    username = entry.get()
    entry_password = password.get()
    print("Username: " + username + "\nPassword: " + entry_password)


def delete():
    entry.delete(0, END)  # Deletes from 0 to END


def backspace():
    entry.delete(len(entry.get()) - 1, END)


entry = Entry(window,
              width=50,
              font=('Aerial', 30, 'bold'),
              fg='#BEBEBE',
              bg='#27476E')
# entry.insert(0, "Enter your name")  # default text
entry.pack(side=TOP)
password = Entry(window,
                 width=50,
                 font=('Aerial', 30, 'bold'),
                 fg='#BEBEBE',
                 bg='#27476E',
                 show="*")  # displays * for password
# entry.insert(0, "Enter your name")  # default text
password.pack(side=TOP)

submit_button = Button(window,
                       text='Submit',
                       command=submit)
submit_button.pack(side=LEFT)
delete_button = Button(window,
                       text='Delete',
                       command=delete)
delete_button.pack(side=LEFT)
backspace_button = Button(window,
                          text='Backspace',
                          command=backspace)
backspace_button.pack(side=LEFT)

window.mainloop()
