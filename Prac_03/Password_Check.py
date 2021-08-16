"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 4

def initial_version():
    password = input("Enter password of at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MIN_LENGTH))

    print('*' * len(password))


# Initial_version()

def get_passcode():
    passcode = input("Enter passcode of at least {} Characters").format(MIN_LENGTH)
    while passcode < MIN_LENGTH:
        print("Password too Short")
        passcode = input("Enter passcode of at least {} Characters").format(MIN_LENGTH)
    return passcode

