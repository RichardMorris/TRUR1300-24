def write_file(user):
    file = open("Names.txt", "a")
    file.write(user + "\n")
    file.close()

def check_file(user):
    try:
        file = open("Names.txt", "r")
        for line in file:
            if line != user:
                write_file(user)
                print("you have been added to the file")

    except FileNotFoundError:
        file = open("Names.txt", "w")
        write_file(user)
        print("The file was created, and you were added.")
    file.close()

def read_all():
    file = open("Names.txt", "r")
    for line in file:
        print(line)
    file.close()

import os

user = os.getlogin()
print(f"Hello, {user}! Hold on...")
check_file(user)
print("Curent contents of file are:")
read_all()
