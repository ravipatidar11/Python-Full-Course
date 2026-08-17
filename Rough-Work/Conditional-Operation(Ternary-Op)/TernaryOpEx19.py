#Write a program to determine whether a person is eligible for a senior citizen discount using the if..else operator.
#TernaryOpEx19.py

age=int(input("Enter Age of the Person: "))

res = "Eligible for a senior citizen discount" if age>=60 else "Not Eligible"

print("Person is :" ,res)
