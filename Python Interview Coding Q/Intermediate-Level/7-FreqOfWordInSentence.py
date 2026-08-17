# Write a Python program to count the frequency of words in a sentence.
#7-FreqOfWordInSentence.py
text=input("Enter UR Sentence:").split()

"""
freq={}

for i in text:
    if i in freq:
       freq[i] = freq[i] + 1
    else:
        freq[i]=1
for ch in freq:
    print("{}---->{}".format(ch,freq[ch]))
"""

for i in range(len(text)):
    if text[i] not in text[:i]:
        print(text[i],text.count(text[i]))