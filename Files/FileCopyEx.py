#Program for Copying the content of One File into Another File
#FileCopyEx.py

def file_copy():
    try:
        source_file=input("Enter Source File: ")
        with open(source_file,"r") as rp:
            destination_file=input("Enter Destination file: ")
            with open(destination_file,"a") as wp:

                #read the source file
                read_src_file=rp.read()

                #write the source file data into destination file
                wp.write(read_src_file)
                print("Copying 1 File---Verify")
    except FileNotFoundError:
        print("File does not Exist")

#Main Program
file_copy()