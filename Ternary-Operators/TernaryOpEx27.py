#Write a program to determine whether an entered salary qualifies for income tax based on a specified threshold using the if..else operator.
#TernaryOpEx27.py

slr=float(input("Enter Salary: "))

res = "Taxable" if slr>1200000 else "Not Taxable"

print("Salary is {}".format(res))
