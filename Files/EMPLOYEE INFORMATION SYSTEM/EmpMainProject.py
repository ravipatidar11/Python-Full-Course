#EmpMainProject.py<---Main Program
from EmpAdd import addEmployee
from EmpDelete import deleteEmployee
from EmpMenu import menu
from EmpView import viewAllEmployees,viewSingleEmployee
from EmpSearch import searchEmployee
from EmpUpdate import updateEmployee
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice: "))
        match(ch):
            case 1:
                addEmployee()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployees()
            case 6:
                searchEmployee()
            case 7:
                print("Thx for Using Project")
                break
            case _:
                print("\tUr Selection of Operation is Wrong--try again")
    except ValueError:
        print("\tDon'tEnter alnums,strs and symbols for Choice-Try again")