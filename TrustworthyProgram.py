import os

user = os.getlogin()
print(f"Hello, {user}! Hold on...")
check_file(user)
print("Curent contents of file are:")
read_all()
