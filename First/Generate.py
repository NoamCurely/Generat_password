import string
import random

def Generate():

    letters = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars + uppercase

    password_len = int(input("Longeur password: ") or "10" )

    password = ''

    for i in range(password_len):
        password += ''.join(random.choice(selection_list))
    print(password)

    return

Generate()
