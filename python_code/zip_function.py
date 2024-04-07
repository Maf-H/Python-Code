#  Copyright (c) 02-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

username = ['Mesfin', 'Haftu', 'Teshome']
passwords = ('P@ssword', 'abc123', 'guest')

# users = zip(username, passwords)
# users = list(zip(username, passwords))
users = dict(zip(username, passwords))

for key, value in users.items():
    print(key, value)