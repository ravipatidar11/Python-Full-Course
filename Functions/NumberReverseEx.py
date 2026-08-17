#program accepting any Number and get its Reverse
#NumberReverseEx.py

def read_val():
    return int(input("Enter any number: "))
def num_rev_val():
    num=read_val()
    if num<=0:
        print("Invalid Input")
    else:
        rv=0
        while num>0:
            digit=num%10
            rv=rv*10+digit
            num=num//10
        else:
            print("Reverse Number = ",rv)

num_rev_val()