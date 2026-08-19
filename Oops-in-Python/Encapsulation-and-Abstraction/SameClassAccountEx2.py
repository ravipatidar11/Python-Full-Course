#SameClassAccountEx2.py

class Account:
    def __init__(self):
        self.__acno = int(input("Enter ACC Number: "))
        self.cname = input("Enter ACC Holder Name: ")
        self.__bal = float(input("Enter ACC Balance: "))
        self.__pin = int(input("Enter Your PIN: "))
        self.bname = input("Enter Branch Name: ")

    def __get_acc_det(self):
        print("---------------------------------------------")
        print("Account Number:", self.__acno)
        print("Account Holder Name:", self.cname)
        print("Account Balance:", self.__bal)
        print("Account PIN:", self.__pin)
        print("Account Branch Name:", self.bname)
        print("---------------------------------------------")

    def show_acc_det(self):
        self.__get_acc_det()

#Main Program
ac=Account()
#ac.getaccdet()--Gives AttributeError bcoz getaccdet() made as Encapsulated
ac.show_acc_det()