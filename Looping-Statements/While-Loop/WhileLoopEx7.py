#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
#WhileLoopEx7.py

n = input('Enter a line of text/word: ')
print("-"*50)
print("\t\tDisplay the Text")
print("-"*50)
print("By using while loop +ve Indices in Forward Direction")

i=0
while (i<=len(n)-1):
    print("\t\t" ,n[i])
    i=i+1
print("-"*50)

print("By using while loop -ve Indices in Forward Direction")

i=-len(n)
while (i<=-1):
    print("\t\t" ,n[i])
    i=i+1
print("-"*50)

print("By using while loop +ve Indices in Backward Direction")

i=len(n)-1
while (i>=0):
    print("\t\t" ,n[i])
    i=i-1
print("-"*50)

print("By using while loop -ve Indices in Backward Direction")

i=-1
while (i>=-len(n)):
    print("\t\t" ,n[i])
    i=i-1
print("-"*50)

