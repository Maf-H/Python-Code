#  Date & Time 30/04/2024, 00:27.
#  @author Mesfin Haftu
from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 10
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        progress_bar['value'] += (speed/GB) * 100
        download += speed
        percent.set(str(int((download/GB)*100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB downloaded")
        window.update_idletasks()  # Update the GUI


window = Tk()
window.title("Progress Bar")

percent = StringVar()
text = StringVar()
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300, mode="determinate")
progress_bar.pack(pady=10)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text).pack()
Button(window, text="download", command=start).pack()

window.mainloop()
