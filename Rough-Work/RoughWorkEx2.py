# prog. for accepting any string and getting all the number of Alphabets,Digits,Special Symbol,num of spaces
#RoughWorkEx2.py

s=input("Enter any string: ")
nsb=0
ab=""
dg=0
ss=""
print("-------------------------------------")
print("Given Sting -" ,s)
print("-------------------------------------")
for ch in s:
    if ch.isalpha():
        ab=ab+ch
    elif ch.isdigit():
        dg=dg+1
    elif not ch.isspace() and not ch.isdigit() and not ch.isalpha():
        ss=ss+ch
    elif ch.isspace():
        nsb=nsb+1
print("Number of spaces --->" ,nsb)
print("Alphabets ---------->" ,ab)
print("Digits-------------->" ,dg)
print("Special Symbols----->" ,ss)
print("-"*50)
