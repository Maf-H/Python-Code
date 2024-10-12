#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Message Box")
window.config(bg="#27476E")


def click_cmd():
    messagebox.showinfo("Info", "You pressed: Show Info", icon="info")
    messagebox.showwarning("Warning", "You pressed: Show Warning")
    messagebox.showerror("error", "You pressed: Show Error", icon="error")
    if messagebox.askquestion("ask question", "Choose yes or no?") == 'yes':
        print("Yes")
    else:
        print("No")
    if messagebox.askokcancel("ok to cancel", "You pressed: Ask OK Cancel"):
        print("ok")
    else:
        print("cancel")
    if messagebox.askyesno("yes or no", "You pressed: Ask Yes No"):
        print("Yes")
    else:
        print("No")
    if messagebox.askretrycancel("retry or cancel", "You pressed: Ask Retry Cancel"):
        print("Retry")
    else:
        print("Cancel")

    answer = messagebox.askyesnocancel("yes, no or cancel", "Ask yes, no or Cancel", icon="question")
    # yes = True, no = False, cancel = None
    if answer is True:
        print("yes")
    elif answer is False:
        print("no")
    else:
        print("Cancel")


button = Button(window,
                text="Click Me",
                command=click_cmd)
button.pack()

window.mainloop()
