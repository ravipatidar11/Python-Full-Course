# how AMT Machine works
# AssignmentOpEx6.py

wamt=int(input("Enter the amount of the wamt: "))

n500=wamt//500
wamt=wamt%500

n200=wamt//200
wamt=wamt%200

n100=wamt//100
wamt=wamt%100

print("-"*50)
print("number of Rs 500 is {}".format(n500))
print("number of Rs 200 is {}".format(n200))
print("number of Rs 100 is {}".format(n100))
print("-"*50)