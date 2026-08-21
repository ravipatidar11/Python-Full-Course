#program for Cal area of Different Figures
#PolyEx7.py

class Circle:
    def __init__(self): # Original Constructor
        self.r=float(input("enter the radius:"))
        self.ac=3.14*(self.r**2)
        print("Area of circle:",self.ac)
        print("-----------------------------------------")
class Square(Circle):
    def __init__(self): # Overridden Method
        self.s=float(input("enter the side:"))
        self.sa=self.s*self.s
        print("Area of square:",self.sa)
        print("------------------------------------------")
        super().__init__()
class Rectangle(Square):
    def __init__(self): # Overridden Method
        self.L=float(input("enter the length:"))
        self.B=float(input("enter the width:"))
        self.ra=(self.L*self.B)
        print("Area of rectangle:",self.ra)
        print("-----------------------------------------")
        super().__init__()

#Main Program
ro=Rectangle() #Object Creation