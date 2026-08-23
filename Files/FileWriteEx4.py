#Program for accepting the Text continously until user
# says stop By Presssing Symbol called @
#FileWriteEx4.py
def datasave():
    print("Enter UR Message and Press @ to stop:")
    with open("india.data","a") as fp:
        while(True):
            kbdata=input()
            if kbdata!="@":
                fp.write(kbdata+"\n")
            else:
                print("Data to the Written to the File--verify")
                break

#main Program
datasave()
