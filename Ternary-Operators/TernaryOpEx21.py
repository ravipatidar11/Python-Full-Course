#Write a program to determine whether a temperature indicates a hot day or a cool day using the if..else operator.
#TernaryOpEx21.py

temp=float(input("Enter Temperature: "))

res = "Hot Day" if temp>=35 else "Cold Day" if temp<=25 else "Normal Day"

print("temp. {} degree is {}".format(temp,res))