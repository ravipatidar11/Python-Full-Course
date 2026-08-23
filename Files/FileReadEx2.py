#program for Reading the Data from any File--readlines()
#FileReadEx2.py
def  readfiledata():
    try:
        with open("kvr1.data","r") as fp:
            filedata=fp.readlines()
            print("----------------------------------")
            for record in filedata:
                print(record,end="")
            print("----------------------------------")
    except FileNotFoundError:
        print("File Does not Exist")

#Main Program
readfiledata()

