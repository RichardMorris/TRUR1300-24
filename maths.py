def addition(a, b):
    print(a, " + ", b, " = ", a+b)

def multiply(a, b):
    print(a, " X ", b, " = ", a*b)

def numbers():
    inputa = input("enter number 1: ")
    inputb = input("enter number 2: ")

print(numbers(), addition(int(inputa),int(inputb)))
print(numbers, multiply(int(inputa),int(inputb)))