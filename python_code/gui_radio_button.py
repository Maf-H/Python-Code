#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Same as the checkbox but you have to choose only one

from tkinter import *

window = Tk()
drinks = [
        'Coffee',
        'Tea',
        'Milk',
        'Water',
        'Pepsi']
coffee = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/coffee.png")
tea = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/coffee.png")
milk = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/coffee.png")
water = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/coffee.png")
pepsi = PhotoImage(file="/Users/mesfinhaftu/Downloads/Images/coffee.png")
drink_image = [coffee, tea, milk, water, pepsi]

window.title("Radio Button")
# window.geometry("300x150")
window.config(bg="#27476E")


def radio_cmd():
    print("You chose to drink: " + drinks[x.get()])


x = IntVar()
for i in range(len(drinks)):
    radio_button = Radiobutton(window,
                               text=drinks[i],
                               font=('Aerial', 20, 'bold'),
                               fg='#BEBEBE',
                               bg='#27476E',
                               variable=x,          # groups radio buttons if they share the same variable
                               value=i,             # Assigns different values to each radio button
                               padx=25,
                               pady=10,
                               # image=drink_image[i],
                               compound='left',
                               command=radio_cmd,   # function to be called when the radio button is clicked.
                               indicatoron=True,       # removes the radio button indicator.
                               width=10)           # sets the width of the radio button
    radio_button.pack(anchor=W)  # anchor is used to align the radio buttons to the left.

window.mainloop()
