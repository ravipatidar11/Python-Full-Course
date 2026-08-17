#Program for Opening a file in 'r' mode
#FileOpenEx1.py<-------"open()"

try:
    fp=open("stud.data","r")
except FileNotFoundError:
    print("File does not Exist")
else:
    print("---------------------------")
    print("File Opened in Read Mode")
    print("Type of fp =",type(fp))
    print("Is File Closed?=",fp.closed)
    print("---------------------------")
finally:
    print("I am from Finally Block")
    try:
        fp.close() #Manual Closing
    except NameError:
        print("File not Opened at all--- no need to close")
    else:
        print("Is File Closed?=",fp.closed)