#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu



window = Tk()
window.title("Text Area")
window.config(bg='#27476E')


def submit_cmd():
    print(text_area.get("1.0", END))


text_area = Text(window,
                 font=("ink free", 30),
                 width=20,              # Amount of characters per line
                 height=8,
                 bg='#27476E',
                 fg='#BEBEBE',
                 border=0,
                 padx=20,
                 pady=20
                 )
text_area.pack()

button = Button(window,
                text="Enter",
                command=submit_cmd)
button.pack()

window.mainloop()
