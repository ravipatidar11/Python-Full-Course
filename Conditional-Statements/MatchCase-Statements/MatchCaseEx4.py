#program for Implementing Base Conversion Calculator
#MatchCaseEx5.py

s="""
===================================================
		Base Conversion calculator
===================================================
    1.	Dec to Bin------------bin()
        Dec to Oct------------oct()
        Dec to Hex------------hex()

    2.	Bin to Dec------------Automatic
        Bin to Oct------------oct()
        Bin to Hex------------hex()

    3.  Oct to Dec-------------Automatic
        Oct to Bin-------------bin()
        Oct to Hex------------hex()						

    4.	Hex to Dec------------Automatic
        Hex to Bin------------bin()
        Hex to Oct------------oct()
    5.  Exit
==================================================="""
print(s)
ch = int(input("Enter your choice: "))
match ch:
    case 1:
        dc = int(input("Enter your decimal value: "))
        bn=bin(dc)
        oc=oct(dc)
        hx=hex(dc)
        print("\tBin({})={}".format(dc, bn))
        print("\tOct({})={}".format(dc, oc))
        print("\tHex({})={}".format(dc, hx))
    case 2:
        bn = input("Enter your binary value: ")
        dc=int(bn,2)
        oc=oct(dc)
        hx=hex(dc)
        print("\tDec({})={}".format(bn, dc))
        print("\tOct({})={}".format(bn, oc))
        print("\tHex({})={}".format(bn, hx))
    case 3:
        oc = input("Enter your octal value with (0o/0O): ")
        dc=int(oc,8)
        hx=hex(dc)
        bn=bin(dc)
        print("\tDec({})={}".format(oc, dc))
        print("\tOct({})={}".format(oc, bn))
        print("\tHex({})={}".format(oc, hx))
    case 4:
        hx = input("Enter your hexa value with (0x/0X): ")
        dv=int(hx,16)
        oc=oct(dv)
        bn=bin(dv)
        print("\tDec({})={}".format(hx, oc))
        print("\tOct({})={}".format(hx, oc))
        print("\tBin({})={}".format(hx, bn))
    case 5:
        print("This program is completed")
    case _:
        print("Invalid input --- Try Again")