from cryptography.fernet import Fernet
import os
BASE = os.path.dirname(os.path.abspath(__file__))

'''
def write_key():
    key = Fernet.generate_key()
    with open(os.path.join(BASE, "key.key"), "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open(os.path.join(BASE, "key.key"), "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open(os.path.join(BASE, "passwords.txt"), "r") as f:
        for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|")
           print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open(os.path.join(BASE, "passwords.txt"), "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, quit)? ").lower().strip()
    if mode == "quit":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

