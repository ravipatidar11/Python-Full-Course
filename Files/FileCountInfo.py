#program for Finding Number of Lines, words and chars in File
#FileCountInfo.py
filename=input("Enter Any File Name: ")
with open(filename,"r") as fp:
    filedata=fp.readlines()
    nl=0
    nw=0
    nc=0
    for line in filedata:
        nl=nl+1
        words=line.split()
        nw=nw+len(words)
        nc=nc+len(line)
    else:
        print("Number of lines in file=",nl)
        print("Number of words in file=",nw)
        print("Number of characters in file=",nc)