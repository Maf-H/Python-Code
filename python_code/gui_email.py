from tkinter import *
import smtplib
import ssl

window = Tk()
window.title("Email Sender")

sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com'
password = 'password'

message = f"""\
    From: Mesfin {sender}
    To: Haftu  {receiver}
    Subject: Hi there

    This message is sent from Python."""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
try:
    server.login(sender, password)
    print("Logged in ...")
    server.sendmail(sender, receiver, message)
    print("Message sent...")
    
except smtplib.SMTPAuthenticationError:
    print("Login failed...")

window.mainloop()