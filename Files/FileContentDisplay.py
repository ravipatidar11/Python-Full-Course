#program for accepting any File Name and display Its Content
#FileContentDisplay.py

try:
    filename=input("Enter File Name:")
    with open(filename,"r") as fp:
        read_file=fp.read()
        print(read_file)
except FileNotFoundError:
    print("File does not Found")