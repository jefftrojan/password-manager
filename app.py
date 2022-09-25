from cryptography.fernet import Fernet 

default_password = input("Enter admin password: ")


# function to create decryption key 
'''' def write_key(): 
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

#function to add password to file
def add():
    name = input("Account name: ")
    add_password = input("Password: ")

    #Open password file in append mode
    with open("passwords.txt", "a") as f:
        # Write into the passwords.txt file
        f.write(name + " | " + add_password +"\n")

# function read passwords
def view():
    with open("passwords.txt", "r") as f:
        # Loop through the lines in the file and return output
        for line in f.readlines():
            data = line.strip()
            # split data into a list with 2 accesible elements 
            user, password = data.split("|")


def menu():
    opt1 = 1
    opt2 = 0
    while opt1 == opt1:
        return add()

add()
view()

