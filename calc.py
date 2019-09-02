import os
import sys
import time


def start_app():
    os.system('cls')
    print("\n")
    print("Welcome to Calculator")
    print("\n")
    print("Choose from below options :")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("\n")
    return input("Enter Q to exit : ")


def add(a, b):
    return float(a) + float(b)


def substract(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b):
    return float(a) / float(b)


def restart_app(msg=''):
    if(len(msg) > 0):
        print("\n")
        print(msg)
    print("\n")
    print("Restarting ...")
    time.sleep(2)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def exit_app(msg=''):
    if(len(msg) > 0):
        print("\n")
        print(msg)
    print("\n")
    print("Exiting ...")
    time.sleep(2)
    sys.exit


operation = start_app()

if(operation.isnumeric()):
    if(float(operation) > 4):
        restart_app("Invalid option selected")
    else:
        print("\n")
        a = input("Enter value of A = ")
        if(a.isnumeric()):
            print("\n")
            b = input("Enter value of B = ")
            if(b.isalpha()):
                restart_app("Entered value is invalid")
        else:
            print("\n")
            print("Entered value is invalid")
            restart_app()

        if(float(operation) == 1):
            result = add(a, b)
        elif(float(operation) == 2):
            result = substract(a, b)
        elif(float(operation) == 3):
            result = multiply(a, b)
        elif(float(operation) == 4):
            result = divide(a, b)
        else:
            restart_app("Invalid option selected")

        restart_app("Answer is = " + str(result))
elif(str(operation).upper() == "Q"):
    exit_app()
else:
    restart_app("Invalid option selected")
