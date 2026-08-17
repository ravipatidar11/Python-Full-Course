#Write a program to check whether a given character is an alphabet or not using the if..else operator.
#TernaryOpEx14.py

ch=input("Enter a character: ")


res= "alphabet" if ('a'<= ch or 'z'>= ch)or('A' <= ch <= 'Z') else "not alphabet"

print("Character {} is {}".format(ch,res))