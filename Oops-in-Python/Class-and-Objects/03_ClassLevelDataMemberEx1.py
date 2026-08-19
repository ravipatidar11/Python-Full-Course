#program for Storing a Common Value Course for all Student Objects
#ClassLevelDataMemberEx1.py

class Student:
    crs="PYTHON"  #Here crs,city are called Class Level Data Member
    city="HYD"

#Main Program
print("Student Course:",Student.crs)
print("Student City:",Student.city)