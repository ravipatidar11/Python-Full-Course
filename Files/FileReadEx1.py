#program for Reading the Data from any File--read()
#FileReadEx1.py
def  readfiledata():
    try:
        with open("kvr1.data","r") as fp:
            filedata=fp.read()
            print("----------------------------------")
            print(filedata)
            print("----------------------------------")
    except FileNotFoundError:
        print("File Does not Exist")

#Main Program
readfiledata()