#  Date & Time 30/04/2024, 02:19.
#  @author Mesfin Haftu
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

window = Tk()  # create window
window.title("Canvas")
points = [150, 50, 250, 250, 50, 250]

canvas = Canvas(window, width=300, height=300)
# canvas.create_line(0, 0, 300, 300, fill='green', width=6) # (x0, y0, x1, y1) of the line
# canvas.create_line(0, 300, 300, 0, fill="red", width=6)
# canvas.create_rectangle(50, 50, 250, 250, fill="purple") # (x0, y0, x1, y1) of the rectangle
# canvas.create_polygon(points, fill="yellow", outline="black") # (x0, y0, x1, y1) of the rectangle
# canvas.create_arc(0, 0, 300, 300, 
#                   start=180, # starting angle of the arc
#                   extent=90, # angle of the arc
#                   fill="blue", # filling color
#                   outline="white", # bordering color
#                   style="pie") # style can be 'chord', 'pie', 'arc'


canvas.create_arc(0, 0, 300, 300, 
                  start=0, # starting angle of the arc
                  extent=180, # angle of the arc
                  fill="red", # filling color
                  outline="black", # bordering color
                  style="pie", # style can be 'chord', 'pie', 'arc'
                  width=6)
canvas.create_arc(0, 0, 300, 300, 
                  start=180, # starting angle of the arc
                  extent=180, # angle of the arc
                  fill="white", # filling color
                  outline="black", # bordering color
                  style="pie", # style can be 'chord', 'pie', 'arc'
                  width=6)
canvas.create_oval(120, 120, 180, 180, outline="black", width=6, fill="white")
canvas.pack()

window.mainloop()
