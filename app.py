default_password = input("Enter admin password")

def view(): 
    pass
def add():
    name = input("Account name: ")
    password = input("Password: ")

    #Open password file in append mode
    with open("passwords.txt", "a") as f:
        # Write into the passwords.txt file
        f.write(name + " | " + password +"\n")

add()


