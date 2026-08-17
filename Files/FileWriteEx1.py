#program for save student data into the file
#FileWriteEx1.py

with open("stud4.data","a") as fp:
    fp.write("Ravi Patidar 6265094824"+"\t")
    print("Student Data Saved in File--Verify")