#Program for Accepting any value and Decide weather It is Paindome or not
#SimpleifEx2.py

val=input("Enter a number: ")

if val==val[::-1]:
    print("Value is Palindrome")
if val!=val[::-1]:
    print("Value is not Palindrome")
print("value is executed")