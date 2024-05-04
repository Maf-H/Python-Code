from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S %p")
    day_number = int(strftime("%w")) # day number of the week
    month_number = int(strftime("%m"))
    day_string = strftime("%A") # day of the week
    date_string = strftime("%B %d, %Y")
    months_am = ["ጥር","የካቲት","መጋቢት","ሚያዝያ","ግንቦት","ሰኔ","ሐምሌ","ነሐሴ","መስከረም","ጥቅምት","ሕዳር","ታሕሳስ"]

    date_string = date_string.replace(strftime("%B"), months_am[month_number - 1])
    
    days_am = ["ሰኞ","ማክሰኞ","ረቡዕ","ኃሙስ","ዐርብ","ቅዳሜ","እሁድ"]
    if time_string.endswith('AM'):
        time_string = time_string.replace("AM", "ቀን")
    if time_string.endswith('PM'):
        time_string = time_string.replace("PM", "ሌሊት")
    time_label.config(text = time_string)
    day_label.config(text = days_am[day_number - 1])
    date_label.config(text = date_string)

    window.after(1000,update)
    
window = Tk()
window.title("Clock")

time_label = Label(window, font=("Aerial", 50), fg ="#00ff00", bg = "black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), fg ="#00ff00")
day_label.pack()

date_label = Label(window, font=("Ink Free", 25), fg ="#00ff00")
date_label.pack()

print(update())

window.mainloop()