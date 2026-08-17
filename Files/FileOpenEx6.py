#program for Demonstrating How to Open the File
#and Knowing about Different Properties of Modes and Files
#FileOpenEx6.py

try:
    with open("stud1.data","a+") as fp:
        print("-----------------------------")
        print("\tType of fp =",type(fp))
        print("\tName of the File =",fp.name)
        print("\tMode of File =",fp.mode)
        print("\tIs File Readable =",fp.readable())
        print("\tIs File Writable =", fp.writable())
        print("\tIs file Closed =",fp.closed)
        print("------------------------------")
    print("Is file Closed =", fp.closed)
except FileNotFoundError:
    print("File does not Exist")