#program for Implementing all Arithmetic Operation
#MatchCaseEx1.py

print("Arithmetic Operations")
print("-"*50)
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. floor division")
print(" 6. Modulo Division")
print(" 7. Exponentiation")
print(" 8. Exit")
print("-"*50)
print("Enter your Choice:")
print("-"*50)

ch=int(input("Enter your choice: "))

match ch:
    case 1:
        print("Enter Two values for Addition:")
        a,b=float(input()),float(input())
        print("ADD ({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two values for Substraction:")
        a, b = float(input()), float(input())
        print("SUB ({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two values for Multiplication:")
        a, b = float(input()), float(input())
        print("MUL ({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two values for Division:")
        a, b = float(input()), float(input())
        print("DIV ({},{})={}".format(a, b, a / b))
    case 5:
        print("Enter Two values for Floor Division:")
        a, b = float(input()), float(input())
        print("FLOOR DIV ({},{})={}".format(a, b, a // b))
    case 6:
        print("Enter Two values for Modulo Division:")
        a, b = float(input()), float(input())
        print("MODULO DIV ({},{})={}".format(a, b, a % b))
    case 7:
        print("Enter Two values for Exponentiation:")
        a, b = float(input()), float(input())
        print("EXPO ({},{})={}".format(a, b, a ** b))
    case 8:
        print("Program is Completed")
        exit()
    case _:
        print("Invalid Input ---- Try Again")