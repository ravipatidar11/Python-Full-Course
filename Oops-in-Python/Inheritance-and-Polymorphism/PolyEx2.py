#PolyEx2.py

class Rectangle:
    def draw(self):
        print("drawing Rectangle")
class Circle(Rectangle):
    def draw(self):
        print("drawing Circle")
        super().draw()
class Square(Circle):
    def draw(self):
        print("drawing Square")
        super().draw()

#Main Program
c=Square()
c.draw()