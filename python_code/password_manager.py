#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# import base64
import os


def generate_key():
    """
    A function that generates a key using Fernet and saves it to a file named "key.key".
    """
    gen_key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(gen_key)


def load_key():
    """
    This function loads a key from a file and returns it.
    """
    file = open('key.key', 'rb')
    loaded_key = file.read()
    file.close()
    return loaded_key


# If file named 'key.key is not exist, it will generate key and save it to 'key.key'
if os.path.exists('key.key') is False:
    generate_key()
key = load_key()
fer = Fernet(key)


def add(user_name, password):
    """
    Add user_name and password to passwords.txt file.
    Parameters:
        user_name (str): The username to add.
        password (str): The password to add.
    Returns:
        None
    """
    password = fer.encrypt(password.encode())
    with open('passwords.txt', 'a') as file:
        file.write(user_name + '|' + password.decode('utf-8') + '\n')


def view():
    """
    A function that opens and reads passwords file to display usernames and passwords.
    """
    with open('passwords.txt', 'r') as file:
        print("%20s | %-20s \n%20s | %-20s" % ('User Name', 'Password', '=========', '====================='))
        for line in file.readlines():
            data = line.rstrip()
            user_name, cipher_password = data.split('|')
            cipher_password = fer.decrypt(cipher_password.encode())
            plain_password = cipher_password.decode('utf-8')
            print("%20s | %-20s" % (user_name, plain_password))


if __name__ == '__main__':
    # add('google', 'I_know_everything')
    # add('facebook', 'time_consumer')
    # add('twitter', 'speak_freely')
    view()
