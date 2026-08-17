# Write a Python program to count the frequency of each character in a string.
#12-FreqOfEachChar.py

text=(input("Enter Any String:"))
text1=sorted(text)

freq={}

for ch in text1:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1

for ch in freq:
    print(ch,freq[ch],sep="",end="")

