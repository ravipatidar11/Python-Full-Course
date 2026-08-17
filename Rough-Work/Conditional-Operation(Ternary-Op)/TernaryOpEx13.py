#Write a program to check whether a character is a vowel or a consonant using the if..else operator.
#TernaryOpEx13.py

char=input("Enter a character: ")

res= "vowel" if "a" in char or "e" in char or "i" in char or "o" in char or "u" in char or "A" in char or "E" in char or "I" in char or "O" in char or "U" in char else "consonant"

print("Character {}: {}".format(char,res))