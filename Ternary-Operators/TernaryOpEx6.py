#Write a program to check whether a person is eligible to vote based on age using the if..else operator.
#TernaryOpEx6.py

age=int(input("Enter a number: "))

res="eligible" if age>=18 else "not eligible"

print("Person is {} to Vote".format(res))