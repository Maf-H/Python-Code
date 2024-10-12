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
window.title("Window")
# window.geometry("300x200")
icon = PhotoImage(file="Mesfin-logo.png")  # used to change icon
photo = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/code.png")
window.iconphoto(True, icon)
window.config(bg="#27476E")


label = Label(window,
              text="Hello GUI.\nHTML tags",
              font=('Aerial', 40, 'bold'),
              fg='#BEBEBE',
              bg='#27476E',
              # relief=GROOVE,# we can use borders RAISED, SUNKEN, GROOVE, RIDGE
              bd=2,           # border width
              padx=20,        # padding (before and after),(top and bottom) of the text
              pady=20,
              image=photo,
              compound='bottom'
              )
label.pack()                  # we can use pack() instead of place()
# label.place(x=0, y=0)       # label is placed at x=0, y=0


window.mainloop()
