#program for Storing a Common Value Course for all Student Objects
#ClassLevelDataMemberEx2.py

class Student:pass

#Main Program
Student.crs="PYTHON"  #Here crs,city are called Class Level Data Member
Student.city="HYD"

print("Student Course:",Student.crs)
print("Student City:",Student.city)