# Write a Python program to print the multiplication table of a number.
#15-MultiplicationTable.py

num=int(input("Enter which number Table U want:"))
print("----------------------------------------")
print("Multiplication Table of {}".format(num))
print("----------------------------------------")
for i in range(1,11):
    print("{} x {}   =   {}".format(num,i,num*i))
print("----------------------------------------")