from tkinter import *
from tkinter.ttk import *
import time
def start():
    tasks = 10
    x = 0
    while x < tasks:
        progress_bar['value'] = int(x/tasks*100) # set the progress bar value to the current percentage
        time.sleep(1) # wait for one second
        x += 1
        percent.set(str(int((x/tasks)*100)) + "%")
        text.set(str(x) + "/" + str(tasks) + " tasks downloaded")
        window.update_idletasks()  # Update the GUI


window = Tk()
window.title("Progress Bar")

percent = StringVar()
text = StringVar()
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text).pack()
Button(window, text="download", command=start).pack()

window.mainloop()