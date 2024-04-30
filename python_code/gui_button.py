#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from tkinter import *


count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()
window.title("Button")
photo = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/like_button.png")
button = Button(window,
                text='Click Me',
                command=click,
                font=('Comic Sans', 40, 'bold'),
                fg='#BEBEBE',
                bg='#27476E',
                activebackground='#BEBEBE',  # when button is clicked it changes the background color
                activeforeground='#27476E',  # when button is clicked it changes the foreground color
                state=ACTIVE,
                image=photo,
                compound='top'
                )
button.pack()
window.mainloop()
