#Write a program to determine whether a person can enter a movie theater based on the age restriction using the if..else operator.
#TernaryOpEx28.py

age=int(input("Enter your age: "))

res = "Allow to Movie Theatre" if age>=16 else "Not Allow to Movie Theatre"

print("Person is " ,res)