#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
from tkinter import *
from tkinter import colorchooser


def color_chooser_cmd():
    # colorchooser.askcolor() returns tuple of ((r, g, b), '#rrggbb')
    window.config(bg=str(colorchooser.askcolor()[1]))


window = Tk()
window.title("Color Chooser")
window.geometry("300x200")

color_chooser = Button(window,
                       text="Choose Color",
                       command=color_chooser_cmd)
color_chooser.pack()

window.mainloop()
