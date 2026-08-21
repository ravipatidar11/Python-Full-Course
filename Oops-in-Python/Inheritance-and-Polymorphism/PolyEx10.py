#program for Cal area of Different Figures
#PolyEx10.py

class Circle:
    def area(self,r): # Original Constructor
        self.ac=3.14*(r**2)
        print("Area of circle:",self.ac)
        print("-----------------------------------------")
class Square:
    def area(self,s): # Overridden Method
        self.sa=s*s
        print("Area of square:",self.sa)
        print("------------------------------------------")
class Rectangle(Square,Circle):
    def area(self,l,b): # Overridden Method
        self.ra=l*b
        print("Area of rectangle:",self.ra)
        print("-----------------------------------------")
        super().area(float(input("enter the Side for Square:")))
        Circle.area(self,float(input("Enter the Radius for Circle:")))

#Main Program
L=float(input("enter the length:"))
B=float(input("enter the breadth:"))
ro=Rectangle() #Object Creation
ro.area(L,B)