#Program for Accepting student details from KBD and save in File as Records
#FileWriteEx2.py
def save_stud_data():
    try:
        with open("stud1.data","a") as fp:
            print("--------------------------------")
            sno=int(input("Enter Student Number:"))
            name=input("Enter Student Name:")
            marks=input("Enter Student Marks:")
            # here sno,name,marks are called objects resides in main memory
            print("--------------------------------")
            #save above details in file
            fp.write(str(sno)+"\t")
            fp.write(name+"\t")
            fp.write(marks+"\n")
            print("Student Data saved in File-verify")
            print("----------------------------------------")

    except ValueError:
        print("Dont Enter Alnums,strs,and Symbols")

    except FileNotFoundError:
        print("File does not Found")


#Main Program
save_stud_data()
