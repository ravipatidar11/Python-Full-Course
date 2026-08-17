from EmpMenu import menu
from EmpAdd import EmpAdd
from EmpView import viewAllEmployee,viewSingleEmployee
from EmpDelete import deleteEmployee
from EmpSearch import searchEmployee
from EmpUpdate import updateEmployee
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice: "))
        match(ch):
            case 1:
                EmpAdd()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployee()
            case 6:
                searchEmployee()
            case 7:
                print("Thx for using Project")
                exit()
            case _:
                print("--------------------------------")
                print("\tyour Choice is Wrong")
                print("--------------------------------")
    except ValueError:
        print("\tDon't Enter Almuns,strs and Symbols---try again")