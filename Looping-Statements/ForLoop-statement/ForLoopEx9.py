#Program for Finding the Sum of Square and Cubes N Natural Nums
#ForLoopEx9.py

n=int(input("Enter natural number u want to sum of natural num. and sum of square and sum of cube: "))

if n<=0:
    print("Invalid input")

else:
    print("-" * 50)
    print("sum of Natural num.,Square and Cube from 1 to {}".format(n))
    print("-" * 50)
    s=0
    ss=0
    sc=0
    for i in range(1,n+1):
        print(i,"\t\t\t",i**2,"\t\t\t",i**3)
        s=s+i
        ss=ss+i**2
        sc=sc+i**3
    else:
        print("-"*50)
        print(s,"\t\t\t",ss,"\t\t\t",sc)
        print("-" * 50)