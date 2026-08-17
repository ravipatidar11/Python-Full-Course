# how AMT Machine works
# OperatorEx6.py

w_amt=int(input("Enter the amount of the w_amt: "))

n500=w_amt//500
w_amt=w_amt%500

n200=w_amt//200
w_amt=w_amt%200

n100=w_amt//100
w_amt=w_amt%100

print("-"*50)
print("number of Rs 500 is {}".format(n500))
print("number of Rs 200 is {}".format(n200))
print("number of Rs 100 is {}".format(n100))
print("-"*50)