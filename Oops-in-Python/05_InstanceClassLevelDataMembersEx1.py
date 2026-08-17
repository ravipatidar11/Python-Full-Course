#program for Storing sno,name ,marks along with Common Value Course and City By using Classes and Objects
#InstanceClassLevelDataMembersEx1.py

class Student:
    crs="PYTHON"  #Here crs,city are called Class Level Data Member
    city="HYD"

#Main Program
#Create Two Objects of Student class
s1=Student()
s2=Student()

#Add Student Details--Instance Data Members to s1 Object--Through an Object
s1.sno=100
s1.name="Ravi"
s1.marks=45.67

#Add Student Details--Instance Data Members to s2 Object--Through an Object
s2.sno=200
s2.name="Rossum"
s2.marks=55.17

#display First Student Object s1 Data
print("-------------------------------------------")
print("First Student Data")
print("-------------------------------------------")
print("\tStudent Number:",s1.sno)
print("\tStudent Name:",s1.name)
print("\tStudent Marks:",s1.marks)
print("\tSTUDENT COURSE:",Student.crs)
print("\tSTUDENT CITY:",Student.city)
print("-------------------------------------------")

#display First Student Object s2 Data
print("Second Student Data")
print("-------------------------------------------")
print("\tStudent Number:",s2.sno)
print("\tStudent Name:",s2.name)
print("\tStudent Marks:",s2.marks)
print("\tSTUDENT COURSE:",Student.crs)
print("\tSTUDENT CITY:",Student.city)
print("-------------------------------------------")