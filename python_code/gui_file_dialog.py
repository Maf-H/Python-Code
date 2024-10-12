from tkinter import *
from tkinter import filedialog

def open_file():
    try:
        file_path = filedialog.askopenfilename(initialdir = "/Volumes/Mesfin's Drive/Programming/Python Code/python_code",
                                               # gives where to open when we click open
                                               title = "Open File",
                                               filetypes = (("text files", "*.txt"),  # used allowed file types example .txt
                                                            ("all files", "*.*")))
        if file_path is None:
            return
        file = open(file_path, 'r')
        print(file.read())
        file.close()
    except:
        print("Opening Canceled.")
def save_file():
    try:
        file = filedialog.asksaveasfile(initialdir = "/Volumes/Mesfin's Drive/Programming/Python Code/python_code",
                                        # gives where to save when we click save
                                        defaultextension = '.txt',  # Default saving extension
                                        filetypes = [("text file", '.txt'),  # Allowed file types
                                                     ("html file", '.html'),
                                                     ("all files", '.*')],
                                        title = "Save File")
        if file is None:
            return
        file_text = str(text.get(1.0, END))  # getting text from text area
        file.write(file_text)
        file.close()
    except:
        print("Saving Canceled.")

window = Tk()
window.title("File Dialog")
text = Text(window,
            font = "Aerial  10")
text.pack()
save = Button(window,
              text = 'Save',
              command = save_file)
save.pack()
button = Button(window,
                text = 'Open',
                command = open_file)
button.pack()
window.mainloop()
