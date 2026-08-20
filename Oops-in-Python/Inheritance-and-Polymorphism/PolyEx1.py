#PolyEx1.py

class Rectangle:
    def draw(self):
        print("drawing Rectangle")
class Circle(Rectangle):
    def draw(self):
        print("drawing Circle")
        super().draw()

#Main Program
c=Circle()
c.draw()