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
window.title("Listbox")
window.config(bg="#27476E")


def submit_cmd():
    foods = []
    for index in listbox.curselection():
        foods.insert(index, listbox.get(index))
    print("You have ordered: ")
    for food in foods:
        print(food)


def add_cmd():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())   # updates the size of the listbox


def delete_cmd():
    for index in reversed(listbox.curselection()):  # we reverse it during the first deletion the index will change.
        listbox.delete(index)


listbox = Listbox(window,
                  fg='#BEBEBE',
                  bg='#27476E',
                  font=('Aerial', 20, 'bold'),
                  width=12,
                  selectmode=MULTIPLE,            # only one item can be selected or Multiple
                  selectbackground='#27476E', )
listbox.pack()
listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Kitfo")
listbox.insert(4, "Samosa")
listbox.insert(5, "Pasta")
listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text="Submit",
                       font=('Aerial', 20, 'bold'),
                       fg='#BEBEBE',
                       bg='#27476E',
                       activebackground='#27476E',
                       activeforeground='#BEBEBE',
                       command=submit_cmd
                       )
submit_button.pack()

add_button = Button(window,
                    text="Add",
                    font=('Aerial', 20, 'bold'),
                    fg='#BEBEBE',
                    bg='#27476E',
                    activebackground='#27476E',
                    activeforeground='#BEBEBE',
                    command=add_cmd
                    )
add_button.pack()

delete_button = Button(window,
                       text="Delete",
                       font=('Aerial', 20, 'bold'),
                       fg='#BEBEBE',
                       bg='#27476E',
                       activebackground='#27476E',
                       activeforeground='#BEBEBE',
                       command=delete_cmd
                       )
delete_button.pack()
listbox.mainloop()
