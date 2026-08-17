#Program for Accepting any value and Decide weather It is Palindrome or not
#IfElseEx1.py

val=input("Enter Any Value: ")

if val==val[::-1]:
    print("{} is palindrome".format(val))
else:
    print("{} is not palindrome".format(val))
