#  Copyright (c) 02-06/04/2024, 16:48.
#  @author Mesfin Haftu

username = ['Mesfin', 'Haftu', 'Teshome']
passwords = ('P@ssword', 'abc123', 'guest')

# users = zip(username, passwords)
# users = list(zip(username, passwords))
users = dict(zip(username, passwords))

for key, value in users.items():
    print(key, value)