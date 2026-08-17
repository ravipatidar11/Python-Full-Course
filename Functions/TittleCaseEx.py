#program for accepting a Line fo Text and convert it into Title Case
# (Don't use title())
#TittleCaseEx.py

def read_val():
    return input("Enter Line of Text: ")

def tittle_val():
    line=read_val()
    if line=="":
        print("Invalid Input")
    else:
        tc=""
        words=line.split()
        for word in words:
            tc=tc+" "+word[0].upper()+word[1:].lower()
        else:
            print("--------------------------")
            print("Tittle Case =" ,tc)

tittle_val()
