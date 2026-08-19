
class Student:
    @classmethod
    def get_crs(cls):
        cls.crs="PYTHON"
        cls.get_city()

    @classmethod
    def get_city(cls):
        cls.city="HYD"

        s1=Student()
        s1.read_stud_data("First")

    def read_stud_data(self,obj_info):
        print("Enter {} Object Information".format(obj_info))
        self.sno = int(input("Enter Student Number: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))
        self.disp_stud_data(obj_info)

    def disp_stud_data(self,obj_info):
        print("Display {} Object Information".format(obj_info))
        print("Student Number =", self.sno)
        print("Student Name =", self.name)
        print("Student Marks =", self.marks)
        print("STUDENT COURSE =",Student.crs)
        print("STUDENT CITY =", Student.city)

#Main Program
Student.get_crs() # Calling Class Level Method
