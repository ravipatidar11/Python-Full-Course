#Program for accepting any  File
# and display Its Content (Source Code)
#FileReadEx3.py
def displaycontent():
    try:
        filename=input("Enter Any File Name:")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("--------------------------------")
            print(filedata)
            print("--------------------------------")
    except FileNotFoundError:
        print("Files Does Not Exist")

#Main Program
displaycontent()
