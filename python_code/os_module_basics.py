import os
import pwd

print(os.getlogin()) # uses to know the user who is login
print(os.getuid())  # uses to know the user id
print(pwd.getpwuid(os.getuid()))