default_password = input("Enter admin password: ")


#function to add password to file
def add():
    name = input("Account name: ")
    password = input("Password: ")

    #Open password file in append mode
    with open("passwords.txt", "a") as f:
        # Write into the passwords.txt file
        f.write(name + " | " + password +"\n")

# function read passwords
def view():
    with open("passwords.txt", "r") as f:
        # Loop through the lines in the file and return output
        for line in f.readlines():
            print(line)


def menu():
    opt1 = 1
    opt2 = 0
    while opt1 == opt1:
        return add()

add()
view()

