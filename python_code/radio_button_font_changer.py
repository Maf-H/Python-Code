#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Radio Button Demonstration for font changing
# @author Mesfin Haftu
# Date jan-8-2024

from tkinter import *

class Radio_Button(Frame):
    """Demonstration of Radio Button"""

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Radio Button Demo")

        self.frame_1 = Frame(self)
        self.frame_1.pack()

        self.text = Entry(self.frame_1, width=25, font="SF 20")
        self.text.insert(INSERT, "Watch the font style change")
        self.text.pack(padx = 5, pady = 5)

        self.frame_2 = Frame(self)
        self.frame_2.pack()

        # Font types
        font_selections = ["Plain", "Bold", "Italic", "Bold/Italic"]

        # Radio button unselected
        self.chosen_font = StringVar() # Default is ""

        # Initial selection
        self.chosen_font.set(font_selections[0])

        # Create group of radio button components
        for style in font_selections:
            a_button = Radiobutton(self.frame_2, text = style,
                                   variable = self.chosen_font,
                                   value = style,
                                   command = self.change_font)
            a_button.pack(side = LEFT, padx = 5, pady = 5)

    def change_font(self):
        """ 'Event Handler' Change the font based on selected Radio buttons"""

        desired_font = "SF 20"

        if self.chosen_font.get() == "Bold":
            desired_font += " bold"

        elif self.chosen_font.get() == "Italic":
            desired_font += " italic"

        elif self.chosen_font.get() == "Bold/Italic":
            desired_font += " bold italic"
        self.text.config(font = desired_font)

def main():
    Radio_Button().mainloop()

if __name__ == "__main__":
    main()
