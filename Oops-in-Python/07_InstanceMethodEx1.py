#Program for Demonstrating Instance Method and 'self'
#InstanceMethodEx1.py

class Student:
    def read_stud_data(self):
        print("In read_stud_data, Memory Address of current Object =",id(self))

#Main Program
s1=Student()
print("Main program: Address of s1 =",id(s1))
s1.read_stud_data()
print("------------------------------------------")
s2=Student()
print("Main program: Address of s2 =",id(s2))
s2.read_stud_data()