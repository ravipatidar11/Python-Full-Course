#program for Cal area of Different Figures
#PolyEx5.py

class Circle:
    def area(self): # Original Method
        self.r=float(input("enter the radius:"))
        self.ac=3.14*(self.r**2)
        print("Area of circle:",self.ac)
        print("-----------------------------------------")
class Square(Circle):
    def area(self): # Overridden Method
        self.s=float(input("enter the side:"))
        self.sa=self.s*self.s
        print("Area of square:",self.sa)
        print("------------------------------------------")
class Rectangle(Square):
    def area(self): # Overridden Method
        print("-----------------------------------------")
        self.L=float(input("enter the length:"))
        self.B=float(input("enter the width:"))
        self.ra=(self.L*self.B)
        print("Area of rectangle:",self.ra)
        print("-----------------------------------------")
        Square.area(self)
        Circle.area(self)



#Main Program
ro=Rectangle()
ro.area()