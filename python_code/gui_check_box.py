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
window.title("Check Box")


# window.geometry("300x150")
photo = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/like_button.png")

def check_cmd():
    if x.get() == 1:
        print("Agree")
    else:
        print("Not Agreed")


x = IntVar()  # IntVar() is an integer variable
# BooleanVar(), DoubleVar(), StringVar() these are some options.
check_button = Checkbutton(window,
                           text="Agree",
                           font=('Aerial', 20, 'bold'),
                           fg='#BEBEBE',
                           bg='#27476E',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=check_cmd,
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack()

window.mainloop()
