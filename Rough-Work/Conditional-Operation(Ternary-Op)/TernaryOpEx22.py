#Write a program to determine whether a business transaction results in profit or loss using the if..else operator.
#TernaryOpEx22.py

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

res = "Profit" if sp>cp else "Loss"

print("Business transaction results in" ,res)