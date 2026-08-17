#Write a program to determine whether a person is eligible for a driving license based on age using the if..else operator.
#TernaryOpEx20.py

age=int(input("Enter Age: "))

res = "Eligible" if age>=18 else "Not eligible"

print("person is {}".format(res))

