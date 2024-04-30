#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Check button demonstration that changes font of text field
# @author Mesfin Haftu
# Date jan-8-2024

from tkinter import *


class Check_Button(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Check Button Demo")

        self.frame_1 = Frame(self)
        self.frame_1.pack()

        self.text = Entry(self.frame_1, width=25, font="SF 20")
        self.text.insert(INSERT, "Watch the font style change")
        self.text.pack()

        self.frame_2 = Frame(self)
        self.frame_2.pack(padx=5, pady=5)

        # Create Boolean Variable
        self.bold_on = BooleanVar() # Default is False

        # Create "Bold" check button
        self.check_bold = Checkbutton(self.frame_2, text="Bold",
                                      variable=self.bold_on,
                                      command=self.change_font)
        self.check_bold.pack(side=LEFT, padx=5, pady=5)

        # Create Boolean Variable
        self.italic_on = BooleanVar()

        # Create "Italic" check button
        self.check_italic = Checkbutton(self.frame_2, text="Italic",
                                        variable=self.italic_on,
                                        command=self.change_font)
        self.check_italic.pack(side=LEFT, padx=5, pady=5)

    def change_font(self):
        """Change the font based on selected Check buttons"""

        desired_font = "SF 20"

        if self.bold_on.get():
            desired_font += " bold"

        if self.italic_on.get():
            desired_font += " italic"

        self.text.config(font=desired_font)


def main():
    Check_Button().mainloop()


if __name__ == "__main__":
    main()
