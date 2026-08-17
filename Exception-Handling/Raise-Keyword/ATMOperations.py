from ATMExcept import WithDrawError,InSuffFundError,DepositError

bal=500.0
def deposit():
    damt=float(input("Enter Your Deposit Amount: "))
    if (damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR AC. xxxxxx123 Credited with INR: {}".format(damt))
        print("\tNow UR Total Balance in INR: {}".format(bal))

def withdraw():
    wamt=float(input("Enter Your Withdraw Amount: "))
    global bal
    if (wamt<=0):
        raise WithDrawError
    elif wamt>bal:
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUR AC. xxxxxx123 Credited with INR: {}".format(wamt))
        print("\tNow UR Remaining Balance in INR: {}".format(bal))


def balenq():
    print("UR AC. xxxxxx123 in INR:",bal)