#Program for Reading the Values of Student Using Classes and Object
#InstanceMethodEx3.py

class Student:
    def read_stud_data(self,obj_info):

        print("Enter {} Object Information".format(obj_info))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        print("------------------------------------------------------")

        self.disp_stud_data(obj_info) #Calling Instance Method from another Instance Method of same class

    def disp_stud_data(self,obj_info):
        print("Display {} Object Information".format(obj_info))
        print("Student Number =",self.sno)
        print("Student Name =",self.name)
        print("Student Marks =",self.marks)


#Main Program
s1=Student()
s2=Student()

print("Content of s1 Object=", s1.__dict__)
print("Content of s2 Object=", s2.__dict__)
print("------------------------------------------------------")
s1.read_stud_data("First")
print("------------------------------------------------------")
s2.read_stud_data("Second")
print("------------------------------------------------------")

