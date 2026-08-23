#Program for Copying an Image
#ImageCopy.py
def filecopy():
    try:
        with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\rose.png","rb") as rp:
            with open("9amrose.png","wb") as wp:
                #read the source file Image Data
                srcfiledata = rp.read()
                #Write the source file Image data to Destination file
                wp.write(srcfiledata)
                print("Image File Copied Successfully")
    except FileNotFoundError:
        print("Source File Does Not Found")
#Main Program
filecopy()