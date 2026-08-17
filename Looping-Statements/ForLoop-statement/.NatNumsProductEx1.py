#program for Finding product of N Natural Nums
#NatNumsProductEx1.py

n=int(input("Enter how many Natural number u want to product: "))
if n<=0:
    print("Invalid input")
else:
    print("Natural numbers Product from 1 to {}".format(n))
    print("-"*50)
    mul=1
    for i in range(1,n+1):
        print(i)
        mul=mul*i
    else:
        print("-" * 50)
        print("Product of Natural Numbers is {}".format(mul))
        print("-" * 50)