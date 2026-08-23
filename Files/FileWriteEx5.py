#Program for Creating a Python Program
# says stop By Presssing Symbol called @
#FileWriteEx4.py
def createpyFile():
    print("EnterPython Program stmts Press @ to stop:")
    with open("onlinestud.py","a") as fp:
        while(True):
            kbdata=input()
            if kbdata!="@":
                fp.write(kbdata+"\n")
            else:
                print("Python Program Written to the File--verify")
                break

#main Program
createpyFile()
