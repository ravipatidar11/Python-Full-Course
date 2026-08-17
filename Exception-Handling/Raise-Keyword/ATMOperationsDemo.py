#ATMMainProject.py<--Main Program

from ATMExcept import WithDrawError,InSuffFundError,DepositError
from ATMOperations import deposit,withdraw,balenq
from ATMMenu import menu

while(True):
    try:
        menu()
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't Try to Deposit Zero/-ve Values")
                except ValueError:
                    print("\tDon't Enter Alnums,Strs,and Symbols")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDon't try WithDraw -VE / Zero Values-try again")
                except InSuffFundError:
                    print("\tInsufficient Fund")
                except ValueError:
                    print("\tDon't Enter Alnums,Strs,and Symbols")
            case 3:
                balenq()
            case 4:
                print("Thanx For Using this Code")
                break
            case _:
                print("Invalid Choice")
    except ValueError:
        print("\tDon't Enter Alnums,Strs,and Symbols")
