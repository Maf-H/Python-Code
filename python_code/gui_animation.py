# Date and Time 04/05/2024, 07:43 ሌሊት.
# @author Mesfin Haftu
# Animation using canvas
from tkinter import *
import time

WIDTH = 500  # Width of canvas in pixels               
HEIGHT = 500 # Height of canvas in pixels
xVelocity = 2 # Change of distance over 0.001 seconds 
yVelocity = 3 # Change of distance over 0.001 seconds

window = Tk()
window.title("Animation")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file="sky.png")
background = canvas.create_image(0, 0, image=background_image, anchor=NW)

angel_image = PhotoImage(file="angel.png")
angel = canvas.create_image(0, 0, image=angel_image, anchor=NW)

image_width = angel_image.width() # angel image width
image_height = angel_image.height() # angel image height

while True:
    coordinates = canvas.coords(angel)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(angel, xVelocity, yVelocity)
    window.update()
    time.sleep(0.001)

window.mainloop()