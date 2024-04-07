#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Mouse event example
# @author Mesfin_Haftu
# Date jan-10-2024

from tkinter import *


class Mouse_Location(Frame):
    """Demonstrating binding mouse events"""

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demonstrating Mouse Events")
        self.master.geometry("275x100")

        self.mouse_position = StringVar()
        self.mouse_position.set("Mouse outside window")
        self.position_label = Label(self, textvariable=self.mouse_position)
        self.position_label.pack(side=BOTTOM)

        # Bind mouse event to window
        self.bind("<Button-1>", self.left_clicked)
        self.bind("<Button-2>", self.centre_clicked)
        self.bind("<Button-3>", self.right_clicked)
        # self.bind("<Button-1>", self.button_pressed)
        self.bind("<ButtonRelease>", self.button_released)
        self.bind("<Enter>", self.entered_window)
        self.bind("<Leave>", self.exited_window)
        self.bind("<B1-Motion>", self.mouse_dragged)

    def button_pressed(self, event):
        """Display coordinate of button pressed"""
        self.mouse_position.set("Pressed at [" + str(event.x) + ',' + str(event.y) + "]")

    def button_released(self, event):
        """Display coordinate of button released"""
        self.mouse_position.set("Released at [" + str(event.x) + "," + str(event.y) + "]")

    def entered_window(self, event):
        """Display message mouse entered window."""
        self.mouse_position.set("Mouse inside window")

    def exited_window(self, event):
        """Display message that mouse has left window"""
        self.mouse_position.set("Mouse outside window")

    def mouse_dragged(self, event):
        """Display coordinate of mouse being used"""
        self.mouse_position.set("Dragged at [" + str(event.x) + "," + str(event.y) + "]")

    def left_clicked(self, event):
        """Display left button clicked"""
        self.master.title("Clicked with left mouse button")

    def centre_clicked(self, event):
        """Display left button clicked"""
        self.master.title("Clicked with middle mouse button")


    def right_clicked(self, event):
        """Display left button clicked"""
        self.master.title("Clicked with right mouse button")





def main():
    Mouse_Location().mainloop()


if __name__ == "__main__":
    Mouse_Location().mainloop()
