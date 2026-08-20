#PolyEx3.py

class Rectangle:
    def draw(self):
        print("drawing Rectangle")
class Circle(Rectangle):
    def draw(self):
        print("drawing Circle")
class Square(Circle):
    def draw(self):
        print("drawing Square")
        Rectangle.draw(self)
        Circle.draw(self)


#Main Program
c=Square()
c.draw()