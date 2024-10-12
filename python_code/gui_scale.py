#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from tkinter import *

window = Tk()
window.title("Scale")
window.config(bg="#27476E")

x = IntVar


def scale_cmd() -> None:
    print("Temperature is : ", str(scale.get()) + "ºC------->" + str((scale.get() + 32) * 9 / 5) + "ºF")


def button_cmd() -> None:
    print("Temperature is : ", str(scale.get()) + "ºC------->" + str((scale.get() + 32) * 9 / 5) + "ºF")


hot = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/hot.png")
hot_label = Label(window, image=hot)
hot_label.pack()
cold = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/snow.png")


scale = Scale(window,
              from_=100,
              to=0,
              orient=VERTICAL,
              font=('Aerial', 20, 'bold'),
              tickinterval=10,  # sets the interval of the scale
              resolution=1,
              troughcolor='red',
              fg='#000000',
              bg='#ffffff',
              length=500,
              )
scale.pack()

cold = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/snow.png")
cold_label = Label(window, image=cold)
cold_label.pack()

button = Button(window,
                text="Get Temperature",
                font=('Aerial', 20, 'bold'),
                fg='#000000',
                bg='#ffffff',
                command=button_cmd,
                compound='bottom',
                padx=25,
                pady=10
                )
button.pack()

window.mainloop()
