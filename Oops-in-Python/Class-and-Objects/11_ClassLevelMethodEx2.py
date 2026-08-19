#program for Demonstrating the Functionality of Class Level Methods
#ClassLevelMethodEx2.py

class Student:
    @classmethod
    def get_crs(cls):
        cls.crs="PYTHON" #OR Student.crs="PYTHON
        Student.get_city()  # OR cls.getcity()
    @classmethod
    def get_city(cls):
        Student.city="HYD"

#Main Program
Student.get_crs()


print("Student Course:",Student.crs)
print("Student City: ",Student.city)