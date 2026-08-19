#program for Storing sno,name and marks By using Classes and Objects
#InstanceDataMemberEx1.py

class Student:pass

#Main Program
#Create Two Objects of Student class
s1=Student()
s2=Student()

print("Memory Address of s1 Object =",id(s1))
print("Memory Address of s2 Object =",id(s2))


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
print("-------------------------------------------")

#display First Student Object s2 Data
print("Second Student Data")
print("-------------------------------------------")
print("\tStudent Number:",s2.sno)
print("\tStudent Name:",s2.name)
print("\tStudent Marks:",s2.marks)
print("-------------------------------------------")
