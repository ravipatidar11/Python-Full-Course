#Write a Python program to check whether a given string is a palindrome.
#CheckPalindrome

text=input("Enter Text: ")

#method-1
"""if text==text[::-1]:
    print("String is Palindrome")
else:
    print("Not a Palindrome")"""


#method-2
rvr=""
for i in text:
    rvr=i+rvr
if text==rvr:
    print("String is Palindrome")
else:
    print("Not a Palindrome")