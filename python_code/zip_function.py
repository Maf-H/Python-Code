#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

username = ['Mesfin', 'John', 'Doe']
passwords = ('P@ssword', 'abc123', 'guest')

# users = zip(username, passwords)
# users = list(zip(username, passwords))
users = dict(zip(username, passwords))

for key, value in users.items():
    print(key, value)
