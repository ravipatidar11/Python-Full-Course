#Program for Opening a file in 'r' mode
#FileOpenEx1.py<------"with open() as"

try:
    with open("stud.data","r") as fp:
        print("------------------------------------------")
        print("File Open in Read Mode")
        print("Is File Closed in 'with open() as'?=", fp.closed)
        print("------------------------------------------")
    print("Is File Closed After 'with open() as'?=",fp.closed)
except FileNotFoundError:
    print("File Does Not Exist")
