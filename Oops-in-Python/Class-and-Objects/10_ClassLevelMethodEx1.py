#program for Demonstrating the Functionality of Class Level Methods
#ClassLevelMethodEx1.py

class Student:
    @classmethod
    def get_crs(cls):
        cls.crs="PYTHON"

    @classmethod
    def get_city(cls):
        Student.city="HYD"

#Main Program
Student.get_crs()
Student.get_city()

print("Student Course:",Student.crs)
print("Student City: ",Student.city)