def addition(a, b):
    print(a, " + ", b, " = ", a+b)


def multiply(a, b):
    print(a, " X ", b, " = ", a*b)

def subtract(a, b):
    print(a, " - ", b, " = ", a-b)



inputa = input("enter number 1: ")
inputb = input("enter number 2: ")

print(addition(int(inputa),int(inputb)))
print(multiply(int(inputa),int(inputb)))
print(subtract(int(inputa),int(inputb)))