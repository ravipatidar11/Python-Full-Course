#program for Saving Iterable Object Data into the file
#FileWriteEx3.py

with open("stud2.data","a") as fp:
    # Take an iterable object
    itr_obj={10,20,"Ravi",34.34,True,2+12j}
    #save the iterable obj into file
    fp.writelines(str(itr_obj))
    print("Iterable Object data saved in file--verify")
