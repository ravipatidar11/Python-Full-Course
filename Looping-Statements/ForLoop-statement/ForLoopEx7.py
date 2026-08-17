#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
#ForLoopEx7.py

n=input("Enter a line of Text: ")
print("------------------------------------------------------")
print("By using for loop--Forward Direction without using Index")
for i in n:
    print(i)
print("------------------------------------------------------")

print("By using for loop--Backward Direction without using Index")
for i in n[::-1]:
    print(i)
print("------------------------------------------------------")

print("By using for loop--Forward Direction with +VE Indices")
for i in range(0,len(n)):
    print(n[i])
print("------------------------------------------------------")

print("By using for loop--Forward Direction with -VE Indices")
for i in range(-len(n),0):
    print(n[i])
print("------------------------------------------------------")

print("By using for loop--Back Direction with +VE Indices")
for i in range(len(n)-1,-1,-1):
    print(n[i])
print("------------------------------------------------------")

print("By using for loop--Back Direction with -VE Indices")
for i in range(-1,-len(n)-1,-1):
    print(n[i])
print("-------------------------------------------------------")
