#program for Storing sno,name and marks By using Classes and Objects
#InstanceDataMemberEx2.py

class Student:pass

#Main Program
#Create Two Objects of Student class
s1=Student()
s2=Student()

print("-------------------------------------------")
print("Content of s1 =",s1.__dict__)
print("Number of Values in s1 =",len(s1.__dict__))
print("-------------------------------------------")
print("Content of s1 =",s1.__dict__)
print("Number of Values in s1 =",len(s1.__dict__))
print("-------------------------------------------")

#Add Student Details--Instance Data Members to s1 Object--Through an Object
s1.sno=100
s1.name="Ravi"
s1.marks=45.67

#Add Student Details--Instance Data Members to s2 Object--Through an Object
s2.sno=200
s2.name="Rossum"
s2.marks=55.17

#display First Student Object s1 Data
#display First Student Object s1 Data
print("-------------------------------------------")
print("First Student Data")
print("-------------------------------------------")
print("Number of Values in s1 =",len(s1.__dict__))
for key,value in s1.__dict__.items():
    print("\t{}--->{}".format(key,value))
print("-------------------------------------------")

#display First Student Object s2 Data
print("Second Student Data")
print("-------------------------------------------")
print("Number of Values in s1 =",len(s1.__dict__))
for key,value in s2.__dict__.items():
    print("\t{}--->{}".format(key,value))
print("-------------------------------------------")

