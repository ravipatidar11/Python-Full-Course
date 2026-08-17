#Program for Reading the Values of Student Using Classes and Object
#InstanceMethodEx2.py

class Student:
    def read_stud_data(self,obj_info):
        print("-----------------------------------------------------")
        print("Enter {} Object Information".format(obj_info))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        print("-----------------------------------------------------")
    def disp_stud_data(self,obj_info):
        print("Display {} Object Information".format(obj_info))
        print("Student Number =",self.sno)
        print("Student Name =",self.name)
        print("Student Marks =",self.marks)
        print("-----------------------------------------------------")

#Main Program
s1=Student()
s2=Student()

print("Content of s1 Object=", s1.__dict__)
print("Content of s2 Object=", s2.__dict__)

s1.read_stud_data("First")
s2.read_stud_data("Second")

s1.disp_stud_data("First")
s2.disp_stud_data("Second")



"""class Student:
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number: "))
        self.name=input("\tEnter Student Name: ")
        self.marks=float(input("\tEnter Student Marks: "))
    def dispstuddata(self,objinfo):
        print("{} Object Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))

#Main Program
s1=Student()
s2=Student()
print("Content of s1 Object=",s1.__dict__)
print("Content of s1 Object=",s2.__dict__)
print("------------------------------------------")
s1.readstuddata("FIRST")
print("------------------------------------------")
s2.readstuddata("SECOND")
print("------------------------------------------")
#display the Object s1 Data
s1.dispstuddata("FIRST")
print("------------------------------------------")
#display the Object s2 Data
s2.dispstuddata("SECOND")
print("------------------------------------------")"""