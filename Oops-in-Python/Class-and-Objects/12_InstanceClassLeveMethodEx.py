
class Student:
    @classmethod
    def get_crs(cls):
        cls.crs="PYTHON"
        cls.get_city()

    @classmethod
    def get_city(cls):
        cls.city="HYD"

    def read_stud_data(self,obj_info):
        print("Enter {} Object Information".format(obj_info))
        self.sno = int(input("Enter Student Number: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))

    def disp_stud_data(self,obj_info):

        Student.get_crs()

        print("Display {} Object Information".format(obj_info))
        print("Student Number =", self.sno)
        print("Student Name =", self.name)
        print("Student Marks =", self.marks)
        print("STUDENT COURSE =",Student.crs)
        print("STUDENT CITY =", Student.city)

#Main Program
s1=Student()
print("----------------------------------------------")
s1.read_stud_data("First")
print("----------------------------------------------")
s1.disp_stud_data("First")
print("----------------------------------------------")


s2=Student()
print("----------------------------------------------")
s2.read_stud_data("Second")
print("----------------------------------------------")
s2.disp_stud_data("Second")
print("----------------------------------------------")
