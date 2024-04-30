#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Button demonstration
# @author Mesfin Haftu
# Date jan-7-2024

from tkinter import *
from tkinter.messagebox import showinfo


class Plain_and_Fancy(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)

        self.master.title("Button")

        # create button with text
        self.plain_button = Button(self, text="Plain Button", command=self.button_pressed)
        self.plain_button.bind("<Enter>", self.rollover_enter)
        self.plain_button.bind("<Leave>", self.rollover_leave)
        self.plain_button.pack(side=LEFT, padx=5, pady=5)

        # create button with image
        self.my_image = PhotoImage(file="Mesfin-logo.png")
        self.fancy_button = Button(self, image=self.my_image, command=self.fancy_pressed)
        self.fancy_button.bind("<Enter>", self.rollover_enter)
        self.fancy_button.bind("<Leave>", self.rollover_leave)
        self.fancy_button.pack(side=LEFT, padx=5, pady=5)

    def button_pressed(self):
        showinfo("Message", "You pressed: Plain Button")

    def fancy_pressed(self):
        showinfo("Message", "You pressed: Fancy Button")

    def rollover_enter(self, event):
        event.widget.config(relief=GROOVE)

    def rollover_leave(self, event):
        event.widget.config(relief=RAISED)


def main():
    Plain_and_Fancy().mainloop()  # Starts event loop


if __name__ == "__main__":
    main()
