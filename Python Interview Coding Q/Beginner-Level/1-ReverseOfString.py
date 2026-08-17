#Reverse a string.
#1-ReverseOfString.py

text=input("Enter Any String:")

#method-1
"""reverse=text[::-1]
print("Reversed of the String =",reverse)"""


#method-2
"""reverse = ""
for ch in text:
    reverse = ch + reverse  #Instead of adding the character at the end, it adds it at the beginning of reverse.
print(reverse)"""


#method-3
reverse="".join(reversed(text))
print("Reversed String =",(reverse))
