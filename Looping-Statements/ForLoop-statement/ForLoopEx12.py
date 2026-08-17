#prog for accepting Line of Text and find the number of words
#ForLoopEx12.py

s=input("Enter Line of text: ")
print("-----------------------------")
words=0
s1=s.split()
for i in s1:
    words = words + 1
    print(i)
print("-----------------------------")
print("number of words ---> ",words)