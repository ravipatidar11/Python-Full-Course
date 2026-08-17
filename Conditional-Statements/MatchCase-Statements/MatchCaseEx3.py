#Program to find All the area of diff. figure given bellow
#MatchCaseEx3.py

print("Area of Diff. Figure")
print("-"*50)
print(" c. circle")
print(" r. rectangle")
print(" s. square")
print(" t. triangle")
print(" e exit")
print("-"*50)

ch=(input("Enter your choice: "))
match ch:
    case 'c'|'C':
        r=float(input("Enter the radius: "))
        ar=3.14*(r**2)
        print("Area of Circle :",ar)
    case 'r' | 'R':
        l = float(input("Enter the Length: "))
        b = float(input("Enter the Breadth: "))
        ar=l*b
        print("Area of Rect. :", ar)
    case 's' | 'S':
        a = float(input("Enter the side: "))
        ar=a*a
        print("Area of Square:",ar)
    case 't' | 'T':
        b = float(input("Enter the Breadth: "))
        h = float(input("Enter the Height: "))
        ar = 1/2*(b*h)
        print("Area of Triangle:",ar)
    case 'e' | 'E':
        print("Program is complete")
        exit()
    case _:
        print("Invalid input --- Try Again")


