# Write a Python program to count vowels and consonants in a string.
#6-VowelsAndConsInString.py

text=input("Enter Any String:")
text1=text.lower()
countV=0
countC=0
for i in text1:
    if i.isalpha():
        if i in "aeiou":
            countV=countV+1
        else:
            countC=countC+1
print("Count of Vowels =",countV)
print("Count of Consonants =",countC)
